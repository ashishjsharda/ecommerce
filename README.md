# E-commerce Website

This is a simple e-commerce website built using Django, a Python web framework.

## Features

- Product catalog with name, description, price, and image
- Product listing page
- Basic styling with HTML and CSS
- Database integration for storing products
- Simple routing and URL configuration

## Requirements

- Python 3.x
- Django 3.x

## Installation and Usage

1. Clone the repository:

git clone https://github.com/ashishjsharda/ecommerce.git


2. Navigate to the project directory:


3. Create a virtual environment (optional but recommended):


4. Install the dependencies:


5. Apply database migrations:


6. Run the development server:


7. Open your browser and visit `http://localhost:8000/products/` to see the product listing page.

## Project Structure

The project follows a standard Django project structure:

- `ecommerce/`: The project root directory
- `catalog/`: The Django app for the product catalog
 - `migrations/`: Database migration files
 - `templates/catalog/`: HTML templates for the catalog app
 - `models.py`: Defines the `Product` model
 - `views.py`: Defines the `product_list` view
- `ecommerce/`: The main Django project settings
- `manage.py`: Django management script

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


