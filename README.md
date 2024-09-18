# TestContainers pgvecto.rs test

This is a demo project to show that `PostgresContainer` fails to launch when using `tensorchord/pgvecto-rs:pg16-v0.3.0`.

## How to run

1. Ensure pipenv is installed
2. Run `pipenv install`
3. Run `pipenv run python -m pytest`
4. Observe one test launching successfully, and the other getting stuck and eventually timing out.
