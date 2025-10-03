import random
import uuid
import string

class TextGenerator:
    def __init__(self):
        self.lorem_words = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 
                           'adipiscing', 'elit', 'sed', 'do', 'eiusmod']
    
    def generate_lorem_ipsum(self, word_count=10):
        words = [random.choice(self.lorem_words) for _ in range(word_count)]
        text = ' '.join(words)
        return text.capitalize() + '.'
    
    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(characters) for _ in range(length))
    
    def generate_uuid(self):
        return str(uuid.uuid4())