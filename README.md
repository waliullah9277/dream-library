# 📚 Dream Library

A full-stack online book borrowing and reviewing system built with **Django** and **Tailwind CSS**. Users can explore books by category, view detailed book information, submit star-based reviews, and borrow books directly through the platform.

🔗 **Live Demo**: [https://dream-library.onrender.com](https://dream-library.onrender.com)

---

## 🚀 Features

- 📖 Browse and filter books by category  
- 🔍 View detailed book information  
- 📝 Authenticated users can borrow books and post reviews  
- ⭐ Star-based rating system  
- 🔐 Login and registration with password show/hide toggle  
- 💬 Review system with user-specific comments and ratings  
- ⚙️ Fully responsive design for all devices  

---

## 🛠️ Tech Stack

- **Backend**: Django  
- **Frontend**: Tailwind CSS, HTML, JavaScript  
- **Database**: SQLite (can be changed to PostgreSQL)  
- **Deployment**: Render  

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/dream-library.git
cd dream-library
```

### 2. Create and activate virtual environment

```bash
python -m venv env
```

- **Windows:**
  ```bash
  env\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source env/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

### 6. Create a superuser (optional)

To access Django admin panel:

```bash
python manage.py createsuperuser
```

Then log in at `http://127.0.0.1:8000/admin/`

---

## 👤 Author

- **Md. Waliullah**  
  GitHub: [@waliullah9277](https://github.com/waliullah9277)  
  Email: waliullah9252@gmail.com  

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.
