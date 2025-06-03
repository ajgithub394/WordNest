# WordNest - Blog Application

WordNest is a modern blogging platform built with Django where users can create, edit, and share their thoughts with the world.

## Features

- User Authentication (Register, Login, Logout)
- User Profile Management
- Create, Edit, and Delete Blog Posts
- Responsive Design
- Modern UI with Bootstrap

## Technologies Used

- Python 3.x
- Django
- Bootstrap 5
- Font Awesome
- SQLite (Database)

## Installation

1. Clone the repository
```bash
git clone <your-repository-url>
cd WordNest
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Create a superuser (Admin)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the application.

## Usage

1. Register a new account or login with existing credentials
2. Create new posts from your profile or the navigation bar
3. Edit or delete your posts as needed
4. View all posts on the home page

## Security

- CSRF protection enabled
- Secure password hashing
- User authentication required for creating/editing posts
- Protected user profiles

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 