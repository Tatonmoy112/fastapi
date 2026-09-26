# FastAPI Reference Project Structure

This directory contains a FastAPI reference application with authentication, database ORM integration, Pydantic schemas, modular routing, voting, and Alembic migrations.

---

## 📂 Project Architecture

```
fastapi/
│
├── .env                  # Environment configuration (DB credentials, secret keys)
├── requirements.txt      # Python package dependencies
│
└── app/                  # Main Application Package
    ├── main.py           # Application entrypoint & route inclusions
    ├── config.py         # Environment settings using Pydantic BaseSettings
    ├── database.py       # SQLAlchemy engine & session setup (get_db dependency)
    ├── models.py         # SQLAlchemy ORM Database Models (Tables)
    ├── schemas.py        # Pydantic Schemas (Request/Response validation)
    ├── utils.py          # Utility functions (Password hashing & verification)
    ├── oauth2.py         # JWT creation, validation, and current-user dependency
    │
    └── routers/          # Modular API Route Handlers
        ├── auth.py       # Authentication router (/login -> JWT generation)
        ├── vote.py       # Vote creation and removal
        ├── post.py       # CRUD operations for Posts (/posts)
        └── user.py       # User registration & user profiles (/users)
```

---

## 🚀 How Each File Works

### 1. `app/main.py`
The central entry point of the FastAPI application.
- Initializes the FastAPI app: `app = FastAPI()`.
- Uses Alembic migrations to manage database tables; run `python -m alembic upgrade head` before starting the app.
- Mounts modular routers (`user.router`, `post.router`, `auth.router`, `vote.router`).

### 2. `app/config.py`
Uses `pydantic-settings` to load environment variables safely from `.env`.
- Defines the `Settings` class mapped to `.env` variables (`database_hostname`, `secret_key`, etc.).

### 3. `app/database.py`
Manages PostgreSQL database connections via SQLAlchemy.
- Creates `engine` using connection string built from `settings`.
- Provides `get_db()` dependency for database session management with yield/cleanup.

### 4. `app/models.py`
Defines database tables using SQLAlchemy ORM (e.g. `User`, `Post`).

### 5. `app/schemas.py`
Defines Pydantic data schemas for API request validation and response formatting.

### 6. `app/utils.py`
Contains helper functions for security:
- `hash_password(password)`: Hashes passwords using `pwdlib` and Argon2.
- `verify_password(plain, hashed)`: Validates user passwords against stored hashes.

### 7. `app/routers/`
Houses modular router modules:
- `auth.py`: Handles POST `/auth/login` credentials check and returns JWT bearer tokens.
- `app/oauth2.py`: Handles JWT token encoding, decoding, and `get_current_user` dependency for protected endpoints.
- `post.py`: RESTful endpoints for CRUD on posts.
- `user.py`: RESTful endpoints for creating users and fetching profiles.

---

## 🛠️ How to Run

1. **Set up virtual environment & install dependencies**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows Git Bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Copy `.env.example` to `.env` (`Copy-Item .env.example .env` in PowerShell,
   or `cp .env.example .env` in Git Bash). Fill in your PostgreSQL connection
   settings and generate a secret key using the command in the template.
   Create the PostgreSQL database named by `DATABASE_NAME` before migrating.

3. **Start PostgreSQL, then apply migrations and start the server**:
   ```bash
   python -m alembic upgrade head
   python -m uvicorn app.main:app --reload
   ```
   Press `Ctrl+C` to stop the server. In PowerShell, you can use
   `.\venv\Scripts\python.exe` in place of `python` without activating the environment.

4. **Interactive API Documentation**:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc UI: `http://127.0.0.1:8000/redoc`



## check current dependency
pip freeze

## for dependency install
pip install -r file_name

## Git reference

The repository includes all application source, both database migrations,
Alembic configuration and templates, pinned dependencies, and setup documentation.
Your private `.env`, installed `venv/`, and generated Python caches stay local.
Use `.env.example` and `requirements.txt` to recreate the environment.
The existing local environment uses Python 3.14.

To work from a fresh copy:

```powershell
git clone https://github.com/Tatonmoy112/fastapi.git
cd fastapi
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
# Fill in .env and create the PostgreSQL database, then:
.\venv\Scripts\python.exe -m alembic upgrade head
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

To save and push future changes from this project:

```powershell
git status
git add .
git diff --cached
git commit -m "Describe your changes"
git push
```

To connect a new project to a new, empty GitHub repository:

```powershell
# Add a .gitignore and safe environment template before staging files.
git init -b main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git add .
git diff --cached
git commit -m "Initial project"
git push -u origin main
```
