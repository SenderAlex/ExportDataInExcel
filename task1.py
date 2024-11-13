import pandas as pd

# Считываем данные из Excel файла
df = pd.read_excel('весь ассортимент с полуфабрикатами 388.xlsx')

# Создаем новый DataFrame для экспорта
export_data = []

# Группируем данные по столбцу "Материал"
grouped = df.groupby('Материал')

for material, group in grouped:
    # Фильтруем компоненты, которые начинаются со слова "Смесь"
    mixture_components = group[group['Краткий текст материала'].str.startswith('Смесь', na=False)]['Компонент'].tolist()

    # Если нет компонентов, пропускаем
    if not mixture_components:
        continue

    # Подготовка строки для экспорта
    export_row = {
        'Код продукта SAP': material,
        'Код полуфабриката 1': mixture_components[0] if len(mixture_components) > 0 else '',
        'Код полуфабриката 2': mixture_components[1] if len(mixture_components) > 1 else '',
        'Код полуфабриката 3': mixture_components[2] if len(mixture_components) > 2 else ''
    }

    export_data.append(export_row)

# Превращаем список словарей в DataFrame
export_df = pd.DataFrame(export_data)

# Экспортируем в новый Excel файл
export_df.to_excel('export_data.xlsx', index=False)