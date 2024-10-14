# TestContainers pgvecto.rs test

> [!IMPORTANT]
> Note that this is the fixed version. Go back to the previous commit at
> https://github.com/theS1LV3R/testcontainers-pgvecto-rs-test/commit/f608c99b3eb501f5c7bf8cde36b6447b40f6717d
> for the broken version.

This is a demo project to show that `PostgresContainer` fails to launch when using `tensorchord/pgvecto-rs:pg16-v0.3.0`. Related issue: <https://github.com/testcontainers/testcontainers-python/issues/703>

## How to run

1. Ensure pipenv is installed
2. Run `pipenv install`
3. Run `pipenv run python -m pytest`
4. Observe one test launching successfully, and the other getting stuck and eventually timing out.
