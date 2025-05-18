# phase3-CodeChallenge

# Coffee Shop Management System ☕

A Python-based object-oriented system for managing coffee orders, customers, and inventory.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Class Structure](#class-structure)
- [Testing](#testing)
- [Example Code](#example-code)
- [Error Handling](#error-handling)
- [Contributing](#contributing)

## Features

- **Customer Management**: Create and track customer orders
- **Coffee Menu**: Manage different coffee types and sizes
- **Order Processing**: Handle order status (pending, preparing, ready, completed)
- **Analytics**: Track popular coffees and customer spending
- **Extras System**: Add custom extras to drinks

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/coffee-shop.git
   cd coffee-shop
Set up virtual environment:

bash
pipenv install
pipenv shell
Install dependencies:

bash
pipenv install pytest  # For testing
Usage
Run the interactive debug console:

bash
python coffeeshop/debug.py
Or import modules in your Python code:

python
from coffeeshop.customer import Customer
from coffeeshop.coffee import Coffee
from coffeeshop.order import Order
Class Structure
Coffee Class
Represents coffee drinks with customizable options

Methods:

add_extra(): Add toppings/flavors

average_price(): Calculate average order price

num_orders(): Get total orders count

Customer Class
Manages customer data and order history

Methods:

create_order(): Place new orders

coffees(): Get unique coffees ordered

orders(): Get all customer orders

Order Class
Handles order processing and status

Methods:

update_status(): Change order state

Price validation (1.0-10.0 range)

Testing
Run unit tests:

bash
pytest tests/
Test coverage:

bash
pytest --cov=coffeeshop tests/
Example Code
python
# Create a customer
customer = Customer("Alice")

# Create coffee
espresso = Coffee("Espresso")
latte = Coffee("Vanilla Latte", size="large")

# Place orders
order1 = customer.create_order(espresso, 2.50)
order2 = customer.create_order(latte, 4.75)

# Add extras
latte.add_extra("caramel", 0.50)
latte.add_extra("whipped cream", 0.75)

# Check analytics
print(f"Most ordered coffee: {customer.most_ordered_coffee()}")
Error Handling
The system validates all inputs:

Customer names: 1-15 characters

Coffee names: Minimum 3 characters

Order prices: 1.0-10.0 range

Status changes: Only valid transitions


Fork the repository

Create a feature branch

Submit a pull request

Please ensure all tests pass before submitting changes.

License
MIT License - See LICENSE file for details