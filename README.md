# Auto Details E-commerce Website

## Introduction
This e-commerce website is designed for selling auto parts and accessories. It's built with Django and provides features like product listings, shopping cart, checkout process, user authentication, and order management.

## Features
Here is a list of features included in the project:
(Processing)
- User authentication system (sign up, log in, password reset)
- Product catalog (with categories, filters, and search functionality)
- Shopping cart and checkout process
- Payment gateway integration
- Order tracking and management
- Review and rating system
- Responsive design for mobile and desktop browsers

## Tech Stack
- **Backend:** Django
- **Frontend:** HTML, CSS, Vue.js
- **Database:** PostgreSQL
- **Payment Processing:** Soon...

## Getting Started

### Prerequisites
Make sure you have Python, pip, and virtualenv installed on your system. 

### Installation

To set up the project environment for development, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Murtazokh/beziamag.git
```

2. Navigate to the project directory:
```bash
cd beziamag
```

3. Create a virtual environment:
```bash
virtualenv venv
```

4. Activate the virtual environment:
   - On Windows:
   ```cmd
   .\venv\Scripts\activate
   ```
   - On MacOS/Linux:
   ```bash
   source venv/bin/activate
   ```

5. Install the project dependencies:
```bash
pip install -r requirements.txt
```

6. Set up the local configurations:
   - Make a copy of `.env.example` to `.env` and update the environment variables with your local settings.

7. Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

8. Create a superuser for Django admin:
```bash
python manage.py createsuperuser
```

9. Run the development server:
```bash
python manage.py runserver
```

10. Open the browser and navigate to `http://127.0.0.1:8000/`.

## Testing
Soon...

## Deployment
Soon...
