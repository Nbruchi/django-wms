# Waste Management System (WMS)

## 📚 Overview

**Waste Management System (WMS)** is a web application designed for organizing waste collection schedules, tracking recycling activities, and generating detailed reports. Developed using **Django**, it streamlines the management of waste collection operations for different user roles, including administrators and general users.

## ✨ Features

- **🔐 User Authentication and Authorization**
  - Register, login, and logout functionality.
  - Role-based access control (admins, staff, and users).
- **📅 Scheduling Management**
  - Create, update, and view waste collection schedules.
- **♻️ Recycling Logs**
  - Record and track recycling activities.
- **📊 Reports Generation**
  - Generate detailed reports on waste collection and recycling.
- **👥 User Management**
  - View user lists with relevant details.
  - Custom template filters for user data presentation.

## 🗂️ Project Structure

```plaintext
wms/
├── wms/                # Project configuration
│   ├── settings.py     # Main settings file
│   ├── urls.py         # Main URL configuration
│   ├── wsgi.py         # WSGI configuration for deployment
│   └── asgi.py         # ASGI configuration for async support
├── users/              # User management application
│   ├── templates/      # Login and registration templates
│   ├── views.py        # User view logic
│   ├── urls.py         # User-related routes
│   └── templatetags/   # Custom template filters
├── schedule/           # Schedule management application
├── recycle_logs/       # Recycling logs management application
├── reports/            # Reports generation application
├── static/             # Static assets (CSS, JavaScript, images)
│   └── css/            # Stylesheets
├── templates/          # Project-wide templates
└── media/              # Media files (e.g., images)
```

## 🛠️ Installation

### Prerequisites

- Python 3.10+
- PostgreSQL

### Setup Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/username/wms.git
   cd wms
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database**:

   - Create a PostgreSQL database named `wms`.
   - Update `wms/settings.py` with your database credentials.

5. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**:

   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

## 🚀 Usage

- **Register/Login**: Access user management via `/users/register/` or `/users/login/`.
- **Schedules**: Manage schedules at `/schedules/`.
- **Recycling Logs**: Record activities at `/recycle-logs/`.
- **Reports**: Generate and access reports at `/reports/`.

## 🛡️ Security Considerations

- Keep `SECRET_KEY` in `settings.py` private.
- Set `DEBUG` to `False` for production.
- Configure `ALLOWED_HOSTS` and secure cookie settings (`CSRF_COOKIE_SECURE`).

## 📈 Future Improvements

- Integrate data visualization tools for reports.
- Add notification features for schedule updates.
- Enhance UI with modern frontend frameworks.

## ⚖️ License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [PostgreSQL](https://www.postgresql.org/)

## 📧 Contact

For questions or collaborations, reach out at `nkundabagenzibruce@gmail.com`.

```

Feel free to make additional edits or add any specific details related to your project.
```
