import sqlite3
from models import Payment

class PaymentRepository:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

    def save(self, payment: Payment) -> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO payments (id, amount, currency, timestamp) VALUES (?, ?, ?, ?)",
            (payment.id, payment.amount, payment.currency, payment.timestamp)
        )
        self.conn.commit()
        cursor.close()
        return True