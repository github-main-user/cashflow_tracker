# Cash Flow Tracker

An application that helps you to track your cash flow. 

The primary focus is on API, documentation, and tests.

For convenient user expirience you can use the admin panel. *(see information in `Usage` section below)*
Sample data has been loaded using fixtures for demonstration purposes in the admin panel.


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
docker compose up --build
```

Use `docker compose down` to stop the project, add `-v` to remove all postgresql data as well.

## Usage

After start, the application will be available on `http://localhost:8000/`.

- `http://localhost:8000/api/v1/docs/` - swagger documentation
- `http://localhost:8000/api/v1/redoc/` - redoc documentation

- `http://localhost:8000/admin/` - admin panel

### default admin's username and password:
username: admin
*email: admin@admin.com*
password: veryhard

## Tests

To see test coverage use this command:

```shell
docker compose run --rm web bash -c "coverage run -m pytest && coverage report"
```
