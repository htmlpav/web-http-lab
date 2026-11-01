
# Notes API

A simple REST API built with Python and FastAPI for creating, storing, and retrieving notes.

## Features

- Create new notes.
- Retrieve all notes.
- Retrieve a specific note by its ID.
- Validate incoming data using Pydantic.
- Automatically assign unique IDs to notes.
- Return appropriate HTTP status codes and errors.

## Technologies

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- HTTPX

## Project Structure

```text
web-http-lab/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd web-http-lab
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the API

Start the development server:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

## API Documentation

Interactive Swagger UI documentation:

http://127.0.0.1:8000/docs

Alternative OpenAPI schema:

http://127.0.0.1:8000/openapi.json

## API Endpoints

| Method | Path | Description | Status |
|---|---|---|---|
| GET | `/health` | Check API status | 200 |
| GET | `/hello` | Get a welcome message | 200 |
| GET | `/notes` | Retrieve all notes | 200 |
| POST | `/notes` | Create a new note | 201 |
| GET | `/notes/{note_id}` | Retrieve a note by ID | 200 / 404 |

## Request and Response Examples

### 1. Create a note

**POST /notes**

Request body:

```json
{
  "title": "HTTP",
  "content": "request -> response"
}
```

Validation rules:

- `title`: required string, 1–80 characters.
- `content`: required string, 1–500 characters.

Successful response (201 Created):

```json
{
  "id": 1,
  "title": "HTTP",
  "content": "request -> response"
}
```

### 2. Get all notes

**GET /notes**

Successful response (200 OK):

```json
[
  {
    "id": 1,
    "title": "HTTP",
    "content": "request -> response"
  }
]
```

### 3. Get a note by ID

**GET /notes/1**

Successful response (200 OK):

```json
{
  "id": 1,
  "title": "HTTP",
  "content": "request -> response"
}
```

If the note does not exist, the API returns:

Status: `404 Not Found`

```json
{
  "detail": "Note not found"
}
```

### 4. Check API health

**GET /health**

Response:

```json
{
  "status": "ok"
}
```

### 5. Get welcome message

**GET /hello**

Response:

```json
{
  "message": "Hello from Notes API"
}
```

## Data Storage

Notes are currently stored in an in-memory Python list.

This means:

- Notes are available only while the application is running.
- All stored notes are lost when the server restarts.
- Data is not persisted in a database or file.

A database can be integrated in a future version.

## Version

**v0.1.0**

Initial release of Notes API with basic note creation and retrieval functionality.
