import requests
from sqlalchemy.dialects.postgresql import insert
from models.customer import Customer

FLASK_URL = "http://mock-server:5000/api/customers"


def fetch_all_customers():
    page = 1
    limit = 10
    result = []

    while True:
        response = requests.get(FLASK_URL, params={"page": page, "limit": limit})
        data = response.json()

        result.extend(data["data"])

        if len(result) >= data["total"]:
            break

        page += 1

    return result


def save_customers(db, customers):
    for customer in customers:
        stmt = insert(Customer).values(**customer)
        stmt = stmt.on_conflict_do_update(
            index_elements=["customer_id"],
            set_=customer
        )
        db.execute(stmt)

    db.commit()
