from models import Payment
from repository import PaymentRepository

class PaymentProcessor:
    def __init__(self, repo: PaymentRepository):
        self.repo = repo

    def process(self, payment: Payment) -> bool:
        # simulate fraud check
        if payment.amount <= 0:
            return False
        return self.repo.save(payment)