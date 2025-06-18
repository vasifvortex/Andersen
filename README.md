# Task Management API

This is a Django REST Framework project for managing tasks with user authentication and JWT.

---

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-folder>
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure PostgreSQL database:
- Install PostgreSQL
- Create a database and a user with privileges
- Update `settings.py` DATABASES section accordingly

5. Apply migrations:
```bash
python manage.py migrate
```

6. Run the server:
```bash
python manage.py runserver
```

---

## API Documentation

### Authentication

- Obtain JWT Token:
```
POST /api/token/
{
  "username": "<username>",
  "password": "<password>"
}
```

- Refresh JWT Token:
```
POST /api/token/refresh/
{
  "refresh": "<refresh_token>"
}
```

### User Registration

```
POST /api/register/
{
  "username": "<username>",
  "password": "<password>",
  "first_name": "<first_name>",       
  "last_name": "<last_name>"          # optional
}
```

### Tasks

- Create Task:
```
POST /api/tasks/create/
{
  "title": "Task Title",
  "description": "Task Description",
  "user_id":"User Id"
}
```

- List All Tasks:
```
GET /api/tasks/
```

- List Tasks by User:
```
GET /api/user/<user_id>/tasks/
```

- Task Details:
```
GET /api/tasks/<task_id>/
```

- Update Task (owner only):
```
PUT /api/tasks/<task_id>/update/
{
  "title": "Updated Title",
  "description": "Updated Description",
  "status": "in_progress",     # or other allowed status
  "user_id": "User Id"
}
```

- Delete Task:
```
DELETE /api/tasks/<task_id>/delete/
```

- Filter Task:
```
GET /api/tasks/filter
```

- Mark Task as Completed:
```
PATCH /api/tasks/<task_id>/complete/
```

---

## Running Tests

```bash
python manage.py test
```

---

## Notes

- Make sure to include the JWT Bearer token in the `Authorization` header for authenticated endpoints:
```
Authorization: Bearer <access_token>
```

- Use PostgreSQL as the database for better reliability and performance.

---

## License

This project is licensed by Vasif Orujzade.
