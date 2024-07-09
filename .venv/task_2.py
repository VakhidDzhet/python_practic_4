import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def gorokh_prepare(path):
    df = pd.read_csv(path)
    df = df.rename(columns={
        'Месяц': 'month',
        'Квартал': 'quarter',
        'Год': 'year',
        'РФ, средняя цена': 'price'}
    )
    df['price_date'] = df[['year', 'month']].apply(lambda row: datetime(*row, 1), axis=1)
    return df[['month', 'quarter', 'year', 'price_date','price']].to_dict(orient='records')

gorokh_path = '/Users/vakhiddzhetygenov/Downloads/горох.csv'
data = gorokh_prepare(gorokh_path)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Изменение цен на горох с января 2012 по январь 2023')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(True)
plt.legend(['РФ, средняя цена'])
plt.show()