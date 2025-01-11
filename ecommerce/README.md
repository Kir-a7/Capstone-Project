
# E-Commerce API

This is a backend API for an e-commerce platform built using Django and Django REST Framework. The project provides functionalities to manage products, categories, orders, and wishlists, and integrates user authentication and role-based access control.

## Features

- **Product Management**: Allows users to view, create, update, and delete products.
- **Wishlist Management**: Users can add products to their wishlist.
- **Order Management**: Users can place, update, and delete orders.
- **Role-based Authentication**: Users can interact with the API based on their roles.
- **Stock Management**: Adjust product stock when orders are placed.

## Technologies Used

- **Django**: A Python web framework for rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **MySQL**: Used for data storage and management.
- **Postman**: For testing API endpoints.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/e-commerce-api.git
cd e-commerce-api
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the virtual environment

#### On macOS/Linux:

```bash
source env/bin/activate
```

#### On Windows:

```bash
env\Scriptsctivate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Set up the database

Create a MySQL database for the project and configure it in `settings.py`.

```bash
python manage.py migrate
```

### 6. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create the superuser.

### 7. Run the server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.


## API Endpoints

### Product Endpoints
- **GET**: `/products/` – List all products
- **POST**: `/products/` – Create a new product
- **GET**: `/products/{id}/` – Get details of a specific product
- **PUT/PATCH**: `/products/{id}/` – Update a specific product
- **DELETE**: `/products/{id}/` – Delete a specific product

### Wishlist Endpoints
- **GET**: `/wishlist/` – List all wishlist items
- **POST**: `/wishlist/` – Add a product to the wishlist
- **DELETE**: `/wishlist/{id}/` – Remove a product from the wishlist

### Order Endpoints
- **GET**: `/orders/` – List all orders
- **POST**: `/orders/` – Create a new order
- **GET**: `/orders/{id}/` – Get details of a specific order
- **PATCH**: `/orders/{id}/` – Update the status of an order
- **DELETE**: `/orders/{id}/` – Delete an order (only if the order is not completed or canceled)

## Authentication

- Authentication is required for most actions involving orders and wishlists. 
- Use **JWT (JSON Web Token)** for authorization. You can obtain the token by logging in with your credentials.

### Example Header for Authenticated Requests:

```bash
Authorization: Bearer <your_token_here>
```

## Project Structure

```
e-commerce-api/
│
├── manage.py
├── requirements.txt
├── e_commerce/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── serializers.py
│
├── products/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
│
└── templates/
```

## Testing with Postman

You can test the API using Postman by sending requests to the following endpoints (make sure to authenticate before accessing restricted endpoints):

### Example POST request to create an order:

```json
POST /api/orders/
{
  "user": 1,
  "items": [
    {
      "product": 1,
      "quantity": 2
    }
  ]
}
```

### Example DELETE request to delete an order:

```json
DELETE /api/orders/1/
```

## Contributing

Feel free to fork the repository, submit issues, and open pull requests. Please follow best practices for contributing and respect the project’s code of conduct.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
