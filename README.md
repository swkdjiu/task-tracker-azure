# 📌 Task Tracker (Kanban Board)

Nowoczesna i interaktywna tablica Kanban do zarządzania zadaniami, zrealizowana w architekturze Full-Stack. Projekt zaliczeniowy demonstrujący integrację backendu w Pythonie z asynchronicznym frontendem i bazą danych.

🌍 **[Wersja Live (Azure)](https://moj-task-tracker-fyb2csgyateqg2hk.germanywestcentral-01.azurewebsites.net)**

---

## ✨ Funkcjonalności

* **Pełny cykl CRUD:** Dodawanie, wyświetlanie, aktualizowanie statusu i usuwanie zadań.
* **Drag & Drop:** Intuicyjne przenoszenie zadań pomiędzy kolumnami ("Do zrobienia", "W trakcie", "Gotowe") za pomocą myszki.
* **Nowoczesny interfejs:** Interfejs użytkownika zaprojektowany w modnym stylu **Glassmorphism** (efekt matowego szkła) z responsywnym układem.
* **Trwałość danych:** Wszystkie zadania i ich statusy są na bieżąco zapisywane w relacyjnej bazie danych.
* **CI/CD:** Projekt jest automatycznie wdrażany do chmury Microsoft Azure przy użyciu GitHub Actions.

---

## 🛠️ Technologie

**Backend:**
* [FastAPI](https://fastapi.tiangolo.com/) - Nowoczesny, bardzo szybki framework webowy do budowania API w Pythonie.
* [SQLAlchemy](https://www.sqlalchemy.org/) - Biblioteka ORM do komunikacji z bazą danych.
* **SQLite** - Lekka, plikowa baza danych.

**Frontend:**
* HTML5 / CSS3 (Flexbox, Glassmorphism, CSS Transitions).
* Vanilla JavaScript (ES6+, Fetch API, HTML5 Drag and Drop API).

**Infrastruktura:**
* **Microsoft Azure App Service** (Linux) - Hosting aplikacji.
* **GitHub Actions** - Automatyzacja wdrożeń (Deployment Center).
