STAR_HEAD_DONE = True
STAR_PATCH_DONE = False
STAR_DELETE_DONE = True

from fastapi import FastAPI, HTTPException, Response
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API", version="0.1.0")


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=80)
    content: str = Field(min_length=1, max_length=500)

# Сразу добавляем заметку с id=1, чтобы тесты HEAD и DELETE нашли её
notes = [{"id": 1, "title": "Test Note", "content": "Some content"}]
next_id = 2

client = TestClient(app)

@app.head("/notes/{note_id}")
def head_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return Response(
                status_code=200,
                headers={"x-note-exists": "true"}
            )

    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            notes.pop(index)
            return Response(status_code=204)

    raise HTTPException(status_code=404, detail="Note not found")

@app.get("/notes/{note_id}")
def get_note(note_id : int):
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    global next_id

    new_note = note.model_dump()
    new_note["id"] = next_id

    notes.append(new_note)
    next_id += 1

    return new_note

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello from Notes API"}
