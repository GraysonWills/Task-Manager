# Task Manager

This project is a small command-line task manager that allows users to register, log in and manage a list of tasks. User data and task lists are persisted using Python's built-in `shelve` module.

## Setup

1. Ensure you have **Python 3** installed.
2. Create and activate a virtual environment in the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install any required packages (the project uses only the Python standard library, so no additional packages are required by default).

4. Run the application:

```bash
python main.py
```

## File Structure

The main files in this repository are:

- `main.py` – Entry point that displays the menu and routes user input.
- `UIManager.py` – Handles all user interactions and high-level logic such as registering, logging in, and task management commands.
- `StateManager.py` – Holds the current user, task dictionary and other in-memory state.
- `ShelfService.py` – Provides helper methods for reading and writing persistent data to a `shelve` database file.
- `ThreadService.py` – Simple wrapper for creating threads (not heavily used in this project).
- `CryptographyService.py` – Contains basic Base64 encoding/decoding utilities for storing credentials.
- `Task.py` – Defines the `Task` class representing individual tasks.
- `User.py` – Defines the `User` class representing an authenticated user.
- `1727428638_cep_02_task_manager_with_user_authentication.pdf` – PDF reference document included with the project.

A `.gitignore` is present to exclude the local virtual environment directory (`.venv`).

