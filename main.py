#!/usr/bin/env python3
import argparse
import sys
from generators.person_generator import PersonGenerator
from generators.finance_generator import FinanceGenerator
from generators.text_generator import TextGenerator
from generators.tech_generator import TechGenerator
from utils.formatters import format_output

def main():
    parser = argparse.ArgumentParser(description='DataGen CLI - Генератор тестовых данных')
    
    # Common arguments - ДОБАВЛЯЕМ ИХ ПЕРВЫМИ
    parser.add_argument('--format', '-f', choices=['json', 'csv', 'table'], 
                       default='table', help='Формат вывода')
    parser.add_argument('--output', '-o', help='Файл для сохранения')
    
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')
    
    # Person commands
    person_parser = subparsers.add_parser('person', help='Генерация персональных данных')
    person_parser.add_argument('--count', '-c', type=int, default=1, help='Количество записей')
    person_parser.add_argument('--locale', '-l', default='ru', help='Локаль (ru/en)')
    
    # Finance commands
    finance_parser = subparsers.add_parser('finance', help='Финансовые данные')
    finance_parser.add_argument('--type', '-t', choices=['card', 'iban', 'transaction'], 
                               default='card', help='Тип финансовых данных')
    finance_parser.add_argument('--count', '-c', type=int, default=1)
    
    # Text commands
    text_parser = subparsers.add_parser('text', help='Генерация текста')
    text_parser.add_argument('--type', '-t', choices=['lorem', 'password', 'uuid'], 
                            default='lorem', help='Тип текста')
    text_parser.add_argument('--length', '-l', type=int, default=10)
    
    # Tech commands
    tech_parser = subparsers.add_parser('tech', help='Технические данные')
    tech_parser.add_argument('--type', '-t', 
                            choices=['ip', 'mac', 'useragent', 'domain'], 
                            default='ip', help='Тип технических данных')
    tech_parser.add_argument('--count', '-c', type=int, default=1)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        result = execute_command(args)
        output = format_output(result, args.format)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Данные сохранены в {args.output}")
        else:
            print(output)
            
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def execute_command(args):
    """Выполнение команды на основе аргументов"""
    if args.command == 'person':
        generator = PersonGenerator(args.locale)
        return [generator.generate_person() for _ in range(args.count)]
    
    elif args.command == 'finance':
        generator = FinanceGenerator()
        if args.type == 'card':
            return [generator.generate_credit_card() for _ in range(args.count)]
        elif args.type == 'iban':
            return [generator.generate_iban() for _ in range(args.count)]
        else:
            return [generator.generate_transaction() for _ in range(args.count)]
    
    elif args.command == 'text':
        generator = TextGenerator()
        if args.type == 'lorem':
            return generator.generate_lorem_ipsum(args.length)
        elif args.type == 'password':
            return [generator.generate_password(args.length) for _ in range(5)]
        else:
            return [generator.generate_uuid() for _ in range(args.length)]
    
    elif args.command == 'tech':
        generator = TechGenerator()
        if args.type == 'ip':
            return [generator.generate_ip() for _ in range(args.count)]
        elif args.type == 'mac':
            return [generator.generate_mac() for _ in range(args.count)]
        elif args.type == 'useragent':
            return [generator.generate_user_agent() for _ in range(args.count)]
        else:
            return [generator.generate_domain() for _ in range(args.count)]

if __name__ == '__main__':
    main()