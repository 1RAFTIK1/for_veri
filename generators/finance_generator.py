import random
from datetime import datetime, timedelta

class FinanceGenerator:
    def __init__(self):
        self.banks = ['SberBank', 'VTB', 'Alfa-Bank', 'Tinkoff', 'Gazprombank']
    
    def generate_credit_card(self):
        card_number = ' '.join([str(random.randint(1000, 9999)) for _ in range(4)])
        expiry = (datetime.now() + timedelta(days=random.randint(365, 3650))).strftime('%m/%y')
        
        return {
            'card_number': card_number,
            'expiry_date': expiry,
            'cvv': str(random.randint(100, 999)),
            'card_holder': f"CARDHOLDER {random.randint(1000, 9999)}",
            'bank': random.choice(self.banks)
        }
    
    def generate_iban(self):
        country = random.choice(['RU', 'US', 'DE', 'GB'])
        iban = f"{country}{random.randint(10, 99)} {random.randint(1000, 9999)}" \
               f"{random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}"
        
        return {
            'iban': iban,
            'country': country,
            'bic': f"BANK{random.randint(100000, 999999)}"
        }
    
    def generate_transaction(self):
        amount = round(random.uniform(10, 10000), 2)
        date = datetime.now() - timedelta(days=random.randint(0, 30))
        
        return {
            'transaction_id': f"TXN{random.randint(100000000, 999999999)}",
            'amount': amount,
            'currency': random.choice(['USD', 'EUR', 'RUB']),
            'date': date.strftime('%Y-%m-%d %H:%M:%S'),
            'type': random.choice(['debit', 'credit']),
            'description': f"Payment to {random.choice(['Store', 'Online', 'Service'])}"
        }