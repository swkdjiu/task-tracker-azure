from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ścieżka do naszej bazy danych SQLite (zostanie utworzony plik sql_app.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Tworzymy silnik bazy danych (engine)
# connect_args={"check_same_thread": False} jest potrzebne tylko dla SQLite w FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Fabryka sesji - posłuży nam do komunikacji z bazą wewnątrz endpointów
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Klasa bazowa, po której będą dziedziczyć nasze modele tabel
Base = declarative_base()