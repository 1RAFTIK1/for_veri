import json
import csv
from io import StringIO

def format_output(data, format_type):
    if format_type == 'json':
        return json.dumps(data, indent=2, ensure_ascii=False)
    
    elif format_type == 'csv':
        if not data:
            return ""
        
        if isinstance(data, list):
            if data and isinstance(data[0], dict):
                # Список словарей
                output = StringIO()
                writer = csv.DictWriter(output, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                return output.getvalue()
            else:
                # Простой список
                output = StringIO()
                writer = csv.writer(output)
                for item in data:
                    writer.writerow([item])
                return output.getvalue()
        else:
            # Одиночное значение
            return str(data)
    
    elif format_type == 'table':
        return format_as_table(data)

def format_as_table(data):
    if not data:
        return "Нет данных"
    
    if isinstance(data, str):
        return data
    
    if isinstance(data, list):
        if not data:
            return "Пустой список"
            
        if isinstance(data[0], dict):
            # Форматирование списка словарей как таблицы
            headers = data[0].keys()
            rows = [[str(item.get(header, '')) for header in headers] for item in data]
            
            # Вычисление ширины колонок
            col_widths = []
            for i, header in enumerate(headers):
                max_cell_width = max(len(str(row[i])) for row in rows) if rows else 0
                col_widths.append(max(len(str(header)), max_cell_width))
            
            # Построение таблицы
            table = []
            header_row = " | ".join(f"{header:<{width}}" for header, width in zip(headers, col_widths))
            separator = "-+-".join("-" * width for width in col_widths)
            
            table.append(header_row)
            table.append(separator)
            
            for row in rows:
                table.append(" | ".join(f"{cell:<{width}}" for cell, width in zip(row, col_widths)))
            
            return "\n".join(table)
        else:
            # Простой список
            return "\n".join(str(item) for item in data)
    else:
        return str(data)