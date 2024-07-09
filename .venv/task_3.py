import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def gorokh_prepare(path):
    df = pd.read_csv(path)
    df = df.rename(columns={
        'Месяц': 'month',
        'Квартал': 'quarter',
        'Год': 'year',
        'Центральный ФО': 'центральный',
        'Южный ФО': 'южный',
        'Северо-Кавказский ФО': 'северо-кавказский',
        'Приволжский ФО': 'приволжский',
        'Уральский ФО': 'уральский',
        'Сибирский ФО': 'сибирский',
        'РФ, средняя цена': 'средняя_цена'}
    )
    columns = ['price_date', 'month', 'quarter',
               'year', 'центральный', 'южный',
               'северо-кавказский', 'приволжский',
               'уральский', 'сибирский', 'средняя_цена']
    df['price_date'] = df[['year', 'month']].apply(lambda row: datetime(*row, 1), axis=1)
    return df[columns].to_dict(orient='records')

gorokh_path = '/Users/vakhiddzhetygenov/Downloads/горох.csv'

data = gorokh_prepare(gorokh_path)

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
df.boxplot(column=['центральный', 'южный', 'северо-кавказский',
                   'приволжский', 'уральский', 'сибирский'],
           grid=True, patch_artist=True,
           boxprops=dict(facecolor='skyblue', color='blue'),
           medianprops=dict(color='red'))

plt.title('Изменение цен на горох по федеральным округам (2012-2023)')
plt.xlabel('Федеральный округ')
plt.ylabel('Цена')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(['Цена'], loc='upper right')
plt.show()
