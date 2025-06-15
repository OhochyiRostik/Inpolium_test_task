# Blog API

**Blog API** is an asynchronous REST API server for a blog platform, built with FastAPI, SQLAlchemy, PostgreSQL, and Docker.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/OhochyiRostik/Inpolium_test_task.git
cd Inpolium_test_task
```

### 2. Create environment file

```bash
cp .env.example .env
```

### 3. Run with Docker

```bash
docker-compose up --build
```

> Make sure Docker and Docker Compose are installed.

### 4. Access the API

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

## Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Docker + Docker Compose
- Pydantic

## Project Structure

```
.
├── app/
│   ├── crud/           # Database operations
│   ├── models/         # SQLAlchemy models
│   ├── routers/        # API routes
│   ├── schemas/        # Pydantic schemas
│   └── database.py     # DB connection and setup
│
├── app/main.py         # Application entry point
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

## API Reference

### Topics

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/topics`        | Get all topics         |
| GET    | `/topics/{id}`   | Get a topic by ID      |
| POST   | `/topics`        | Create a new topic     |
| PUT    | `/topics/{id}`   | Update a topic         |
| DELETE | `/topics/{id}`   | Delete a topic         |

### Posts

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/posts`         | Get all posts          |
| GET    | `/posts/{id}`    | Get a post by ID       |
| POST   | `/posts`         | Create a new post      |
| PUT    | `/posts/{id}`    | Update a post          |
| DELETE | `/posts/{id}`    | Delete a post          |

### Comments

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| GET    | `/comments`        | Get all comments         |
| GET    | `/comments/{id}`   | Get a comment by ID      |
| POST   | `/comments`        | Create a new comment     |
| PUT    | `/comments/{id}`   | Update a comment         |
| DELETE | `/comments/{id}`   | Delete a comment         |

### Pagination and Sorting: limit, skip, sort_by, and order

Many list endpoints support pagination and sorting using query parameters:

| Parameter | Type                   | Description                         |
|-----------|------------------------|-------------------------------------|
| `limit`   | Integer                | Number of items to return           |
| `skip`    | Integer                | Number of items to skip (offset)    |
| `sort_by` | String (field name)    | Field by which to sort the results  |
| `order`   | "asc" or "desc"        | Sort order: ascending or descending |

Example 1:

GET /posts/?skip=10&limit=5

Returns posts 11 to 15.

Example 2: Pagination with Sorting

GET /posts/?sort_by=created_at&order=desc&limit=5

Returns the latest 5 posts sorted by creation time in descending order.

## Example Requests

### Create a topic

POST /topics
```json
{
  "name": "Topic 1"
}
```

### Create a post

POST /posts
```json
{
  "title": "My first post",
  "content": "Hello",
  "topic_id": 1
}
```

### Create a comment

POST /comments
```json
{
  "content": "Very good",
  "post_id": 1
}
```

## Docker Commands

- Start: `docker-compose up --build`
- Stop: `docker-compose down`
- Clean up with volumes:  
  `docker-compose down -v`

##  Run Locally Without Docker

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```