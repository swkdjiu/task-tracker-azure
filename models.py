from sqlalchemy import Column, Integer, String
from database import Base

# Model reprezentujący tabelę "tasks" w naszej bazie danych
class TaskDB(Base):
    __tablename__ = "tasks"

    # Kolumny w tabeli
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    # Status zadania: domyślnie "todo" (Do zrobienia)
    status = Column(String, default="todo")