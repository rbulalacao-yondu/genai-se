from dataclasses import dataclass

@dataclass
class Payment:
    id: str
    amount: float
    currency: str
    timestamp: str