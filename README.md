# CareBridge

Multi-tenant virtual care portal. Organizations run their own branded patient
portal on shared infrastructure; patients book appointments with providers,
providers confirm and reschedule, org admins manage staff.

A practice project — see `docs/PROJECT.md` for scope and `docs/decisions/` for
why things are the way they are.

## Running it

```bash
cp .env.example .env
docker compose up
```

App on http://localhost:8000, health check at `/health/`.

First run, in another terminal:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Admin at http://localhost:8000/admin/

## Running without Docker

Postgres must be reachable on localhost:5432.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements/local.txt
pre-commit install
python manage.py migrate
python manage.py runserver
```

## Development

```bash
pytest                      # tests
pytest --cov                # with coverage
ruff check . --fix          # lint
ruff format .               # format
mypy apps config            # types
python manage.py makemigrations --check --dry-run   # missing migrations?
```

CI runs all of the above on every push and pull request.

## Settings

Split by environment under `config/settings/`:

| Module | Used by |
|---|---|
| `base.py` | shared, imported by the others; no secrets, no DEBUG |
| `local.py` | development — the `manage.py` default |
| `test.py` | pytest — fast hashing, deterministic |
| `production.py` | deployed environments |

Defaults to `local` via `manage.py`. Deployed processes set
`DJANGO_SETTINGS_MODULE` explicitly.

## Layout

```
config/          Django project — settings, root urls, wsgi/asgi
apps/            Django apps, one per bounded area
  users/         custom user model (email login)
tests/           pytest suite, mirrors apps/
docs/decisions/  architecture decision records
requirements/    base / local / production
```
