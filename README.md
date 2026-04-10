# CRUD Notes App

A full-stack notes application built with Flask, SQLite, and Tailwind CSS. This project demonstrates user authentication, database modeling, and CRUD operations for notes, along with a simple and responsive UI.

## 🚀 Project Overview

This project is a personal learning application that allows users to:
- Register and log in securely
- Create, read, edit, and delete notes
- Store user accounts and notes in a SQLite database
- Use Flask templates with Jinja inheritance for reusable HTML structure
- Apply Tailwind CSS and Flowbite components for a modern UI

## 🧩 Key Features

- User registration and login with `Flask-Login`
- Protected routes for authenticated note management
- CRUD operations for notes using `Flask-SQLAlchemy`
- Database migrations support with `Flask-Migrate`
- Clean UI styling using Tailwind CSS and Flowbite
- Simple profile and note management pages

## 📚 Libraries and Frameworks Used

### Backend
- `Flask` — web framework
- `Flask-SQLAlchemy` — ORM for database access
- `Flask-Login` — user authentication and session handling
- `Flask-Migrate` — database migration support
- `SQLAlchemy` — core database toolkit
- `SQLite` — lightweight embedded database

### Frontend / UI
- `Tailwind CSS` — utility-first CSS framework
- `Flowbite` — Tailwind component library
- `Jinja2` — template engine for HTML rendering

### Development Dependencies
- `tailwindcss` — CSS build tooling
- `flowbite` — UI component library for Tailwind

## 🛠️ What I Learned

- How to build a Flask web app from scratch
- Managing database models and relationships with SQLAlchemy
- Implementing user authentication and session management
- Writing secure login and registration flows
- Creating CRUD routes for note creation, editing, and deletion
- Using Flask templates and Jinja for reusable page layouts
- Styling apps with Tailwind CSS and enhancing UI with Flowbite
- Setting up CSS build scripts with `tailwindcss`

## 📁 Project Structure

- `main.py` — Flask application and route definitions
- `templates/` — HTML templates for login, registration, notes, and profile pages
- `src/input.css` — Tailwind input CSS configuration
- `src/output.css` — generated Tailwind output CSS
- `requirements.txt` — Python dependencies
- `package.json` — Tailwind build scripts and front-end dependencies

## 🚀 Getting Started

1. Clone the repository
   ```bash
   git clone <repo-url>
   cd CRUD
   ```

2. Create and activate a Python virtual environment
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Install npm dependencies for Tailwind CSS (if not already installed)
   ```bash
   npm install
   ```

5. Build the Tailwind CSS output
   ```bash
   npm run build-css
   ```

6. Run the application
   ```bash
   python main.py
   ```

7. Open the app in your browser:
   - `http://127.0.0.1:8000`

## 🔧 Notes

- The app uses `SQLite` via `sqlite:///test.db`
- `Flask-Migrate` is configured to support database changes without data loss
- `main.py` creates the database automatically when the app starts

## 🧪 Future Improvements

- Add password hashing for better security
- Add validation and flash messages for forms
- Improve responsive layout and UX with more Tailwind components
- Add unit tests and integration tests
- Deploy the app to a platform like Heroku, Render, or Vercel

## 📌 License

This repository is for learning and demonstration purposes.
