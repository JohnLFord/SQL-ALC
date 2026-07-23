# SQLAlchemy Order Demo

This project is a small SQLAlchemy + SQLite demo that models users, products, and orders in a shop database.

## What It Does

- Creates `users`, `products`, and `orders` tables with SQLAlchemy ORM
- Defines one-to-many relationships from users to orders and products to orders
- Seeds sample users, products, and orders
- Prints all users, products, and orders
- Updates the product price for `Mouse`
- Demonstrates deleting a temporary user record
- Shows unshipped orders
- Counts total orders per user

## Notes About The Seed Data

The script seeds orders idempotently. That means you can run it more than once without creating duplicate sample orders.

Database files such as `shop.db` are ignored by git so local runs do not get committed.

## Project Files

- `SQL-ALC.py` - main application script
- `requirements.txt` - Python dependencies
- `push.ps1` - helper script for add/commit/push

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
python .\SQL-ALC.py
```

## Git Workflow

For a normal push:

```powershell
.\push.ps1 "Describe your change"
```

That script runs:

- `git add .`
- `git commit -m "..."`
- `git push`

If there is nothing new to commit, git will tell you and no push will be created.
