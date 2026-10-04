from app.database.db import Base, engine
from app.schemas.profile import Profile
from app.schemas.project import Project


def main():
    Base.metadata.create_all(bind=engine)
    print("Banco de dados inicializado!")


if __name__ == "__main__":
    main()
