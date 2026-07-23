# SQLAlchemy Relational Database Assignment

This project demonstrates how to build and manage a relational database using Python and SQLAlchemy with SQLite.

## What This Script Covers

- Setup SQLAlchemy engine, base, session
- Define `User`, `Product`, and `Order` tables
- Define relationships:
  - One `User` to many `Order`
  - One `Product` to many `Order`
- Create tables
- Insert sample data (2 users, 3 products, 4 orders)
- Run CRUD-style operations:
  - Read users/products/orders
  - Update a product price
  - Delete a user by ID
- Bonus:
  - `Order.status` (shipped or not)
  - Query unshipped orders
  - Count orders per user

## Files

- `SQL-ALC.py` - main assignment script
- `shop.db` - SQLite database file created and used by the script

## Setup

1. Create/activate a virtual environment (optional but recommended).
2. Install dependencies:

```bash
pip install SQLAlchemy
```

## Run

```bash
python SQL-ALC.py
```

The script prints the results of all required queries and operations to the terminal.
