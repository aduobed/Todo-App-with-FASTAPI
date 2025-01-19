# FastAPI Todo App

A todo app using FastAPI.

## Table of Contents

-   [Installation](#installation)
-   [Setting Up the Environment](#setting-up-the-environment)
-   [Running the Application](#running-the-application)
-   [Fix for Passlib Bcrypt Error Warning](#fix-for-passlib-bcrypt-error-warning)
-   [Data Migration with Alembic](#data-migration-with-alembic)
-   [API Endpoints](#api-endpoints)

## Installation

### Prerequisites

-   Python 3.9 or higher
-   Pipenv
-   PostgreSQL (or any other supported database)

### Setting Up the Environment

1. **Clone the repository:**

```sh
git clone https://github.com/your-username/todo_app.git
cd todo_app
```

2. **Create a virtual environment and install dependencies**

```
pipenv install
```

3. **Activate the virtual environment:**

```
pipenv shell
```

4. **Set up environment variables:**
   Create a .env file in the project root and add the necessary environment variables. For example:

```
DATABASE_URL=postgresql://user:password@localhost/todo_app
SECRET_KEY=your_secret_key
```

## Running the Application

1. **Start the FastAPI server:**

```
uvicorn auth.user:app --reload
```

The application will be available at *http://127.0.0.1:8000*.

## Fix for Passlib Bcrypt Error Warning

```
version = _bcrypt.__about__.__version__
```

In the **.venv/Lib/site-packages/passlib/handlers/bcrypt.py** file, change the line:

```
version = _bcrypt.__about__.__version__
```

to:

```
version = _bcrypt.__version__
```

### Generate requirements.txt from Pipenv

To generate a **requirements.txt** file from Pipenv, run:

```
pipenv lock -r > requirements.txt
```

## Data Migration with Alembic

Alembic is a powerful tool that allows us to modify database schemas.

Alembic Installation

```
pip install alembic
```

#### Alembic Use

1. Initialize Alembic:

```
alembic init alembic
```

This prepares and creates necessary files for database migrations.

2. Create a new migration:

```
alembic revision -m "create user phone number col"
```

This creates a new file to modify the database.

3. Run the migration:

```
alembic upgrade <revision_number>
```

This runs the migration specific file using the revision number.

## API Endpoints

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
