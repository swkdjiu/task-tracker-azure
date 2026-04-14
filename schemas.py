from pydantic import BaseModel

# Podstawowy schemat danych (wymaga podania tytułu zadania)
class TaskBase(BaseModel):
    title: str
    status: str = "todo"

# Schemat używany przy tworzeniu nowego zadania z frontendu
class TaskCreate(TaskBase):
    pass

# Pełny schemat zadania (zwracany do przeglądarki, zawiera ID z bazy)
class TaskResponse(TaskBase):
    id: int

    class Config:
        # Pozwala na automatyczną konwersję z obiektu bazy danych (SQLAlchemy) na JSON
        from_attributes = True