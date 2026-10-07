\# Task Management System



A REST API for managing tasks using FastAPI and PostgreSQL.



\## Features



\- Create tasks

\- View all tasks

\- View a single task

\- Update tasks

\- Delete tasks

\- PostgreSQL database integration

\- RESTful API

\- Swagger API documentation



\## Technologies



\- Python

\- FastAPI

\- SQLAlchemy

\- PostgreSQL

\- Pydantic

\- Psycopg2

\- Uvicorn

\- Git and GitHub



\## API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | / | Check API status |

| POST | /tasks | Create a task |

| GET | /tasks | Get all tasks |

| GET | /tasks/{task\_id} | Get a task |

| PUT | /tasks/{task\_id} | Update a task |

| DELETE | /tasks/{task\_id} | Delete a task |



\## Project Structure



task-management-system/

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   └── schemas.py

├── .gitignore

├── requirements.txt

└── README.md



\## How to Run



Install dependencies:



pip install -r requirements.txt



Start the server:



uvicorn app.main:app --reload



Open Swagger UI:



http://127.0.0.1:8000/docs



\## Database



The application uses PostgreSQL and SQLAlchemy ORM.



The tasks table contains:



\- id

\- title

\- description

\- completed



\## Author



Vaibhav

