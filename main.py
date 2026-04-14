from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

# Importujemy nasze własne pliki
import models
import schemas
from database import engine, SessionLocal

# 1. Tworzenie tabel w bazie danych (jeśli jeszcze nie istnieją)
# Ta linijka tworzy plik sql_app.db na dysku
models.Base.metadata.create_all(bind=engine)

# Inicjalizacja aplikacji
app = FastAPI(title="Task Tracker API")

# 2. Zależność (Dependency) - funkcja, która otwiera i zamyka połączenie z bazą
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Montowanie plików statycznych (frontendu)
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- ENDPOINTY (Trasy API) ---

@app.get("/")
def read_root():
    # Zwraca główną stronę HTML
    return FileResponse("static/index.html")

# READ: Pobieranie wszystkich zadań
@app.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    # SQL: SELECT * FROM tasks
    return db.query(models.TaskDB).all()

# CREATE: Tworzenie nowego zadania
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    # Tworzymy nowy obiekt bazy danych na podstawie danych od użytkownika
    db_task = models.TaskDB(title=task.title, status=task.status)
    db.add(db_task)     # Dodajemy do sesji
    db.commit()         # Zapisujemy w bazie
    db.refresh(db_task) # Odświeżamy, aby uzyskać wygenerowane ID
    return db_task

# UPDATE: Zmiana statusu zadania (np. przeniesienie do innej kolumny)
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task_status(task_id: int, status: str, db: Session = Depends(get_db)):
    # Szukamy zadania po ID
    db_task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()
    if not db_task:
        # Jeśli nie ma, zwracamy błąd 404
        raise HTTPException(status_code=404, detail="Nie znaleziono zadania")
    
    # Zmieniamy status i zapisujemy
    db_task.status = status
    db.commit()
    db.refresh(db_task)
    return db_task

# DELETE: Usuwanie zadania
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    # Szukamy zadania po ID
    db_task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Nie znaleziono zadania")
    
    # Usuwamy z bazy
    db.delete(db_task)
    db.commit()
    return {"message": "Zadanie usunięte pomyślnie"}