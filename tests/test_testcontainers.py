from testcontainers.postgres import PostgresContainer
import sqlalchemy

def print_version(postgres: PostgresContainer):
  psql_url = postgres.get_connection_url()
  engine = sqlalchemy.create_engine(psql_url)
  with engine.begin() as connection:
    print(connection.execute(sqlalchemy.text("SELECT version()")).fetchone())

def test_0_2_0():
  with PostgresContainer("tensorchord/pgvecto-rs:pg16-v0.2.0") as postgres:
    print_version(postgres)

def test_0_3_0():
  with PostgresContainer("tensorchord/pgvecto-rs:pg16-v0.3.0") as postgres:
    print_version(postgres)
