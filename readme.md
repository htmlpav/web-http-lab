
# Notes API

A simple REST API built with Python and FastAPI for creating and retrieving notes.

## Features

- `GET /health` — checks whether the API is running.
- `GET /hello` — returns a welcome message.
- `GET /notes` — returns all stored notes.
- `POST /notes` — creates a new note and returns it with HTTP status `201 Created`.
- Automatic request validation using Pydantic.
- Interactive API documentation with Swagger UI.

## Technologies

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- HTTP

## Project Structure

```text
web-http-lab/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
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

Activate it:

Windows:

```powershell
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the API

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

## API Documentation

Interactive Swagger documentation:

http://127.0.0.1:8000/docs

## Example Request

Create a note using `POST /notes`:

```json
{
  "title": "HTTP",
  "content": "request → response"
}
```

Example response:

```json
{
  "title": "HTTP",
  "content": "request → response",
  "id": 1
}
```

## Data Storage

Notes are currently stored in an in-memory Python list.

This means that all notes are lost when the application restarts.

A database may be added in a future version.
