
# Notes API

A simple REST API for creating, retrieving, and deleting notes, built with Python and FastAPI.

This project was created as a practical introduction to backend development, HTTP methods, REST API architecture, and request/response handling.

## Features

- Create notes using POST.
- Retrieve all notes using GET.
- Retrieve a single note by ID using GET.
- Check whether a note exists using HEAD.
- Delete a note by ID using DELETE.
- Validate request data using Pydantic.
- Automatically generate API documentation with Swagger UI.

## Technologies

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- HTTPX

## Project Structure

```text
web-http-lab/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd web-http-lab
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

OpenAPI schema:

```text
http://127.0.0.1:8000/openapi.json
```

## API Endpoints

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | `/health` | Check API health | 200 |
| GET | `/hello` | Welcome message | 200 |
| GET | `/notes` | Retrieve all notes | 200 |
| POST | `/notes` | Create a new note | 201 |
| GET | `/notes/{note_id}` | Retrieve a note by ID | 200 / 404 |
| HEAD | `/notes/{note_id}` | Check whether a note exists | 200 / 404 |
| DELETE | `/notes/{note_id}` | Delete a note by ID | 204 / 404 |

## Request Examples

### Create a Note

**POST** `/notes`

Request body:

```json
{
    "title": "Learning FastAPI",
    "content": "Understanding HTTP methods and REST APIs"
}
```

Successful response (201 Created):

```json
{
    "id": 1,
    "title": "Learning FastAPI",
    "content": "Understanding HTTP methods and REST APIs"
}
```

### Get All Notes

**GET** `/notes`

Example response:

```json
[
    {
        "id": 1,
        "title": "Learning FastAPI",
        "content": "Understanding HTTP methods and REST APIs"
    }
]
```

### Get a Single Note

**GET** `/notes/1`

Example response:

```json
{
    "id": 1,
    "title": "Learning FastAPI",
    "content": "Understanding HTTP methods and REST APIs"
}
```

If the note does not exist, the API returns:

```json
{
    "detail": "Note not found"
}
```

Status: `404 Not Found`.

### Check Whether a Note Exists

**HEAD** `/notes/1`

The HEAD method checks whether a note exists without returning its JSON body.

Successful response:

- Status: `200 OK`
- Header: `x-note-exists: true`
- Response body: empty

If the note does not exist, the API returns `404 Not Found`.

### Delete a Note

**DELETE** `/notes/1`

Successful response:

- Status: `204 No Content`
- Response body: empty

If the note does not exist, the API returns `404 Not Found`.

## Data Validation

The API uses Pydantic to validate incoming note data.

| Field | Type | Constraints |
|---|---|---|
| title | string | 1–80 characters |
| content | string | 1–500 characters |

Invalid request data is rejected automatically by FastAPI with a `422 Unprocessable Entity` response.

## Current Limitations

- Notes are stored in an in-memory Python list.
- Data is lost when the application restarts.
- No database integration yet.
- No authentication or authorization.
- PATCH (partial note updates) is not implemented yet.

## Project Version

**Version:** 0.1.0

**Current stage:** Basic CRUD functionality (Create, Read, Delete) with additional HEAD support.

## License

This project is intended for educational purposes.
