# Mini-Paste

Mini-Paste is a microservice that allows users to paste data into a simple storage area and additionally do some minor transformations. Pastes can later be retrieved via the unique paste-id.

# Requirements

- Python 3.9
- Poetry package installed

# Installation

(Optional) Point poetry to python3.9 location if different from installed
```
> poetry env use C:\<python 3.9 folder>\python
```

Install dependencies

```
> poetry install
```

Activate virtual env

```
# Windows
> ./.venv/Scripts/activate

# Linux
> ./.venv/bin/activate
```

Initialize and run (Dev)

```
# Windows
> $env:FLASK_ENV = "development"
> $env:FLASK_APP = "minipaste.wsgi"
> flask database init dev
created dev db
> python -m minipaste.wsgi

# Linux
> export FLASK_ENV=development
> export FLASK_APP=minipaste.wsgi
> flask database init dev
created dev db
> python -m minipaste.wsgi
```

Test

```
> pytest tests
```

# References

## Routes

- `GET /` - healthcheck endpoint
- `POST /paste` - endpoint to store pastes
- `GET /paste/<id>` - endpoint to get stored pastes


## Commands

### Database

Commands relating to the db

- `init <STAGE>` - creates initial db for dev or prod