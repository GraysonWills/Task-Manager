# Task Manager Writeup

This repository contains a command-line task manager implemented in Python. The program allows users to register, log in, and maintain a personal list of tasks that are persisted across sessions. Below is an overview of the major components and how they interact.

## Components

- **main.py** – Entry point for the application. It presents a menu-driven interface for login/registration and task management actions.
- **UIManager.py** – Handles user input/output and coordinates application logic such as registering, authenticating, and manipulating tasks.
- **StateManager.py** – Keeps track of the currently logged-in user and an in-memory dictionary of tasks.
- **ShelfService.py** – Wraps Python's `shelve` module for persisting user data and associated task lists.
- **ThreadService.py** – Simplified thread helper (not heavily used but included for completeness).
- **CryptographyService.py** – Provides Base64 encoding/decoding utilities for storing credentials.
- **Task.py** and **User.py** – Define the data models for tasks and users.
- **UIPrompts.py** – Centralizes all user-facing messages and prompts.

## How It Works

1. **Register / Login**
   - Users create an account by choosing a unique username and password. Credentials are encoded using Base64 for basic obfuscation before being stored.
   - Returning users log in by providing their credentials, which loads their stored tasks from the shelf database.

2. **Managing Tasks**
   - After authentication, users can add new tasks, view the list of tasks, mark tasks as complete, or delete them.
   - All modifications are saved back to the shelf so the state persists between sessions.

3. **Data Persistence**
   - Each username maps to a shelf entry containing the encoded password and a dictionary of task objects. This data is stored in the `userInfo` shelf file.

## Running the Application

Ensure you have Python 3 available, then execute:

```bash
python main.py
```

Follow the prompts to register or log in and begin managing your tasks.

