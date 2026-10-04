from sqlalchemy import inspect

from app.database.db import engine


def main():
    inspector = inspect(engine)

    tables = inspector.get_table_names()

    print("Tabelas encontradas:")

    for table in tables:
        print(f"- {table}")


if __name__ == "__main__":
    main()