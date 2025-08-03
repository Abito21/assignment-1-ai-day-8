dev:
	uv run uvicorn app.main:app --reload --port 8000

format:
	uv run ruff format
	uv run ruff check --fix

migration:
	uv run alembic revision --autogenerate -m "Update schema"

migrate-up:
	uv run alembic upgrade head