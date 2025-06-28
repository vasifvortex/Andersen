# Task Management API

This is a RESTful API for managing tasks, built with Django REST Framework and PostgreSQL.
It includes custom user authentication using JWT and Swagger documentation.

---
##Features
- JWT Authentication (Login/Token)
- Custom User model with registration endpoint
- Task CRUD operations (Create, Read, Update, Delete)
- Task completion endpoint
- Task filtering by status and user
- Swagger UI documentation
- Docker & PostgreSQL support
  
## Installation
1. Clone the repository
```
   git clone https://github.com/your-repo/task-api.git
   cd task-api
```
2. Configure environment variables

   Create a `.env` file in the root directory and add:
```
   DEBUG=True
   SECRET_KEY=your-secret-key
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   POSTGRES_DB=django_db
   POSTGRES_USER=django_user
   POSTGRES_PASSWORD=django_pass
   DB_HOST=db
   DB_PORT=5432
```
3. Build and run with Docker
```
   docker compose up --build
```
4. Apply migrations
```
   docker compose exec web python manage.py migrate
```
5. Run tests
```
   docker compose exec web python manage.py test tasks
```

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
    `<task_status>` should be one of the following:  
  - `new`  
  - `in_progress`  
  - `completed`  
```
GET /api/tasks/?status=<task_status>

```

- Mark Task as Completed:
```
PATCH /api/tasks/<task_id>/complete/
```

---
## Swagger Documentation
Once the server is running, access Swagger UI at:
```
http://localhost:8000/swagger/
```
You can authorize using the Bearer Token in the top-right by entering:
```
Bearer your-jwt-token
```

## License

This project is licensed by Vasif Orujzade.
