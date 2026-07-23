from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


# Part 1: Setup
engine = create_engine("sqlite:///shop.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Part 2: Define Tables
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    # A User can have many Orders
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # A Product can appear in many Orders
    orders = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    # Part 6 Bonus: shipped status
    status = Column(Boolean, default=False)

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")


# Part 3: Create Tables
Base.metadata.create_all(engine)


# Part 4: Insert Data
user_1 = session.query(User).filter_by(email="john.ford@example.com").first()
if not user_1:
    user_1 = User(name="John Ford", email="john.ford@example.com")
    session.add(user_1)

user_2 = session.query(User).filter_by(email="jane.smith@example.com").first()
if not user_2:
    user_2 = User(name="Jane Smith", email="jane.smith@example.com")
    session.add(user_2)

product_1 = session.query(Product).filter_by(name="Keyboard").first()
if not product_1:
    product_1 = Product(name="Keyboard", price=45)
    session.add(product_1)

product_2 = session.query(Product).filter_by(name="Mouse").first()
if not product_2:
    product_2 = Product(name="Mouse", price=25)
    session.add(product_2)

product_3 = session.query(Product).filter_by(name="Monitor").first()
if not product_3:
    product_3 = Product(name="Monitor", price=180)
    session.add(product_3)

session.commit()

seed_orders = [
    (user_1.id, product_1.id, 1, False),
    (user_1.id, product_3.id, 2, True),
    (user_2.id, product_2.id, 3, False),
    (user_2.id, product_1.id, 1, True),
]

for user_id, product_id, quantity, status in seed_orders:
    existing_order = session.query(Order).filter_by(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity,
        status=status,
    ).first()
    if not existing_order:
        session.add(
            Order(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity,
                status=status,
            )
        )
session.commit()

user_to_delete = session.query(User).filter_by(email="temp.user@example.com").first()
if not user_to_delete:
    user_to_delete = User(name="Temp User", email="temp.user@example.com")
    session.add(user_to_delete)
    session.commit()


# Part 5: Queries
print("\nAll Users")
for user in session.query(User).all():
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

print("\nAll Products")
for product in session.query(Product).all():
    print(f"Name: {product.name}, Price: {product.price}")

print("\nAll Orders")
for order in session.query(Order).all():
    print(
        f"User: {order.user.name}, Product: {order.product.name}, "
        f"Quantity: {order.quantity}"
    )

print("\nUpdate Product Price")
product_to_update = session.query(Product).filter_by(name="Mouse").first()
if product_to_update:
    product_to_update.price = 30
    session.commit()
    print(f"Updated {product_to_update.name} to {product_to_update.price}")

print("\nDelete User By ID")
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print(f"Deleted user with ID {user_to_delete.id}")


# Part 6: Bonus Queries
print("\nOrders Not Shipped")
for order in session.query(Order).filter_by(status=False).all():
    print(
        f"Order ID: {order.id}, User: {order.user.name}, "
        f"Product: {order.product.name}, Quantity: {order.quantity}"
    )

print("\nTotal Orders Per User")
for user in session.query(User).all():
    print(f"{user.name}: {len(user.orders)} order(s)")


session.close()
