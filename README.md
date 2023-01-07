# KEmarket
This is an e-commerce website built using Django, a high-level Python web framework. The project allows users to browse and purchase products, as well as provides a secure checkout process using Stripe for payment processing.

## Features
- Browse products by category or search for specific items
- View product details and add items to cart
- Secure checkout process with Stripe integration
- Order history and tracking for users
- Admin panel for managing products, orders, and user information

## Installation
- Clone the repository: `git clone https://github.com/Jonnybuoy/EMarket/`
- Install dependencies: `pip install -r requirements.txt`
- Set up the database: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Collect static files: `python manage.py collectstatic`
- Run the development server: `python manage.py runserver`

## Configuration
You will need to set the following environment variables in order for the application to function properly:

- `SECRET_KEY`: Django secret key for security purposes
- `STRIPE_PUBLISHABLE_KEY`: Publishable key for Stripe API
- `STRIPE_SECRET_KEY`: Secret key for Stripe API

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.