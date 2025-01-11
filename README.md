# E-commerce Product API

## Overview
The **E-commerce Product API** is a backend application built with Django and Django REST Framework (DRF). It provides functionality for managing products, users, and orders for an e-commerce platform. The API supports CRUD operations for products, categories, and users, along with authentication and search capabilities.

## Features

### Product Management
- Create, read, update, and delete (CRUD) operations for products.
- Products include fields such as:
  - Name
  - Description
  - Price
  - Category
  - Stock Quantity
  - Image URL
  - Created Date

### Category Management
- Manage product categories with unique names.

### User Management
- CRUD operations for user accounts.
- Authentication using JWT (JSON Web Token).

### Wishlist
- Allows users to add products to a personal wishlist.

### Orders
- Create orders with products and quantities.
- Automatically calculate the total price of an order.

### Product Reviews
- Users can submit reviews and ratings for products.

### Search and Filtering
- Search for products by name or category.
- Filter products by:
  - Category
  - Price range
  - Stock availability.

### Pagination
- Paginate product listings and search results to handle large datasets efficiently.

## Installation

### Prerequisites
- Python 3.9+
- Django 4.0+
- PostgreSQL (or any preferred database)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Kir-a7/Capstone-project.git
   cd Capstone-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database in `settings.py`:
   Update the `DATABASES` section with your database credentials.

5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- Obtain JWT Token:
  ```
  POST /api/jwt/login/
  ```
- Refresh JWT Token:
  ```
  POST /api/jwt/refresh/
  ```

### Products
- List and create products:
  ```
  GET /api/products/
  POST /api/products/
  ```
- Retrieve, update, and delete a product:
  ```
  GET /api/products/<id>/
  PUT /api/products/<id>/
  DELETE /api/products/<id>/
  ```

### Categories
- List and create categories:
  ```
  GET /api/categories/
  POST /api/categories/
  ```

### Wishlist
- List and add products to wishlist:
  ```
  GET /api/wishlist/
  POST /api/wishlist/
  ```

### Orders
- List and create orders:
  ```
  GET /api/orders/
  POST /api/orders/
  ```

### Reviews
- List and create reviews:
  ```
  GET /api/reviews/
  POST /api/reviews/
  ```

### Search and Filtering
- Search products by name or category:
  ```
  GET /api/products/?search=<query>
  ```
- Filter products:
  ```
  GET /api/products/?category=<category>&price_min=<min>&price_max=<max>&in_stock=<true|false>
  ```

## Additional Features
- **Error Handling**: Proper error messages with HTTP status codes.
- **Validation**: Ensures required fields are filled and valid.
- **Security**: Authentication using JWT, permission classes for role-based access.

## Deployment
This project can be deployed on platforms like Heroku or PythonAnywhere. Ensure environment variables are set for:
- `DATABASE_URL`
- `SECRET_KEY`
- `DEBUG`

Example deployment steps:
```bash
heroku login
heroku create
heroku config:set DATABASE_URL=<your-database-url>
heroku config:set SECRET_KEY=<your-secret-key>
heroku config:set DEBUG=False
```

Push the code to Heroku:
```bash
git push heroku main
```

## Testing
Use Postman to test the API. Import the following endpoints:
- Authentication: `/api/jwt/login/`
- CRUD for products, categories, wishlist, and orders.
- Search and filtering for products.

### Example Request
- **POST /api/products/**
  ```json
  {
    "name": "Laptop",
    "description": "High-performance gaming laptop",
    "price": 1500.00,
    "category": 1,
    "stock_quantity": 10,
    "image_url": "http://example.com/laptop.jpg"
  }
  ```

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, contact kirubelteshome6202@gmail.com

