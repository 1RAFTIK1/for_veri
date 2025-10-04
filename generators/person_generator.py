import random
from datetime import datetime, timedelta

class PersonGenerator:
    def __init__(self, locale='en'):
        self.locale = locale
        self.first_names_ru = ['Алексей', 'Мария', 'Иван', 'Ольга', 'Дмитрий', 'Елена']
        self.last_names_ru = ['Иванов', 'Петрова', 'Сидоров', 'Кузнецова', 'Смирнов']
        self.first_names_en = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah']
        self.last_names_en = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
    
    def generate_person(self):
        if self.locale == 'en':
            first_name = random.choice(self.first_names_ru)
            last_name = random.choice(self.last_names_ru)
            city = random.choice(['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'])
        else:
            first_name = random.choice(self.first_names_en)
            last_name = random.choice(self.last_names_en)
            city = random.choice(['New York', 'London', 'Tokyo', 'Berlin'])
        
        birth_date = datetime.now() - timedelta(days=random.randint(18*365, 70*365))
        
        return {
            'first_name': first_name,
            'last_name': last_name,
            'email': f"{first_name.lower()}.{last_name.lower()}@example.com",
            'phone': self._generate_phone(),
            'birth_date': birth_date.strftime('%Y-%m-%d'),
            'city': city
        }
    
    def _generate_phone(self):
        if self.locale == 'en':
            return f"+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}"
        else:
            return f"+1{random.randint(200, 999)}{random.randint(200, 999)}{random.randint(1000, 9999)}"