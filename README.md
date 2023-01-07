# KEmarket
This is an e-commerce website built using Django, a high-level Python web framework. The project is hosted on Heroku and can be accessed [here](https://kemarket-project-django.herokuapp.com/) and allows users to browse and purchase products, as well as provides a secure checkout process using Stripe for payment processing.

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

## Deployment to Heroku
- Create a Heroku account and install the Heroku CLI
- Login to Heroku: `heroku login`
- Create a new Heroku app: `heroku create APP_NAME`
- Add the PostgreSQL add-on: `heroku addons:create heroku-postgresql:hobby-dev`
- Make heroku migrations: `heroku run python manage.py migrate`
- Set the environment variables for the app: `heroku config:set SECRET_KEY=your_secret_key STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key - - - - STRIPE_SECRET_KEY=your_stripe_secret_key`
- Deploy the code to Heroku: `git push heroku master`
- Run database migrations: `heroku run python manage.py migrate`

## Configuration
You will need to set the following environment variables in order for the application to function properly:

- `SECRET_KEY`: Django secret key for security purposes
- `STRIPE_PUBLISHABLE_KEY`: Publishable key for Stripe API
- `STRIPE_SECRET_KEY`: Secret key for Stripe API

## License
This project is licensed under the MIT License. See the LICENSE file for more details.