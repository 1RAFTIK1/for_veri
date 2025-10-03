import random
import string

class TechGenerator:
    def generate_ip(self):
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}." \
               f"{random.randint(0, 255)}.{random.randint(1, 255)}"
    
    def generate_mac(self):
        return ":".join([f"{random.randint(0x00, 0xff):02x}" for _ in range(6)])
    
    def generate_user_agent(self):
        browsers = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        ]
        return random.choice(browsers)
    
    def generate_domain(self):
        domains = ['com', 'org', 'net', 'io', 'dev']
        name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        return f"{name}.{random.choice(domains)}"