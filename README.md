# Cash Flow Tracker

An application that helps you to track your cash flow. 

The primary focus is on API, architecture, documentation, and tests.

For convenient user experience you can use the admin panel *(see the information in `Usage` section below)*.


## Tech Stack

- Python 3.13
- Django 5+
- Django Rest Framework
- PostgreSQL
- Docker, Docker Compose

## Installation

First, you need to have `docker` and `docker compose` installed on your machine.

1. Clone the repo:
```shell
git clone https://github.com/github-main-user/cashflow_tracker.git
```

2. Enter the directory
```shell
cd cashflow_tracker
```

3. Setup environment
```shell
cp .env.example .env
```

4. Start the project
```shell
docker compose up --build -d
```

Use `docker compose down` to stop the project, add `-v` to remove all postgresql data as well.

## Usage

After start, the application will be available on `http://localhost:8000/`.

- `http://localhost:8000/api/v1/docs/` - swagger documentation
- `http://localhost:8000/api/v1/redoc/` - redoc documentation
- `http://localhost:8000/admin/` - admin panel

### Admin panel
To create an admin user use this command:
```shell
docker compose exec web python manage.py createsuperuser
```

For demonstration purposes some sample data has been prepared in fixtures.
You can load them using this command:
```shell
docker compose exec web python manage.py loaddata fixtures.json
```

## Tests

Command to run tests:
```shell
docker compose run --rm web pytest
```

### Test Coverage

The project has 99% test coverage, including:

- Models and business logic validations
- API endpoints (CRUD operations, filtering)
- Validation of invalid scenarios and error handling

You can see coverage using the command below:
```shell
docker compose run --rm web bash -c "coverage run -m pytest && coverage report"
```
