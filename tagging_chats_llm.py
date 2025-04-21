import os
import re
import pandas as pd

df = pd.read_feather(os.path.join(os.getcwd(), "data", "tested_results_250331_4.feather"))

val_set = set(df["gpt_val"].to_list())
print(val_set)
handled_examples = ['блабла, да', 'всякая белиберда нето дането 1. Нет  \n2. Нет', 'Rate-limit error', '1. Нет\n всякая белиберда нето дането 2. Нет', ' всякая белиберда нето дането 1. Да.\nвсякая белиберда нето дането 2. всякая белиберда нето данетоДа.', 'всякая белиберда нето дането 1. Нет  всякая белиберда нето дането \nвсякая белиберда нето дането 2.всякая белиберда нето дането  Да']

val_list = list(val_set) + handled_examples


texts = val_list + [
    'блабла, да',
    'всякая белиберда нето дането 1. Нет \n2. Нет',
    'Rate-limit error',
    '1. Нет\n всякая белиберда нето дането 2. Нет',
    ' всякая белиберда нето дането 1. Да.\nвсякая белиберда нето дането 2. всякая белиберда нето данетоДа.',
    'всякая белиберда нето дането 1. Нет всякая белиберда нето дането \nвсякая белиберда нето дането 2.всякая белиберда нето дането Да',
    'да, нет',
    'нет, да', 'всякая херня, нет', 
    'космические корабли бороздят \nда, да'
]

def process_texts(texts):
    results = []
    
    for text in texts:
        # Разделяем текст на части, сохраняя разделители
        parts_and_delimiters = re.split(r'([,\n])', text.lower())
        
        text_result = []
        position = 1  # Начинаем с позиции 1 (до первого разделителя)
        
        for part in parts_and_delimiters:
            if part in (',', '\n'):
                position += 1  # Увеличиваем позицию после разделителя
                continue
            
            # Ищем все "да" или "нет" в текущей части
            matches = re.finditer(r'\b(да|нет)\b', part)
            for match in matches:
                word = match.group(1)
                text_result.append((word, position))
        
        results.append(text_result)
    
    return results

# Обрабатываем тексты
result = process_texts(texts)

# Выводим результат
for i, res in enumerate(result, 1):
    print(f"Текст{i}: {texts[i-1]} \nИзвлечено: {res}\n")