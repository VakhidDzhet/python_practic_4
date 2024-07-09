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

plt.figure(figsize=(12, 6))
plt.plot(df['price_date'], df['price'], label = 'РФ, средняя цена')

for year in df['year'].unique():
    q3_data = df[(df['year'] == year) & (df['quarter'] == 3)]
    if not q3_data.empty:
        min_price = q3_data['price'].min()
        max_price = q3_data['price'].max()
        min_date = q3_data[q3_data['price'] == min_price]['price_date'].values[0]
        max_date = q3_data[q3_data['price'] == max_price]['price_date'].values[0]
        plt.scatter(min_date, min_price, color='blue', label='Минимальная цена' if year == df['year'].unique()[0] else"")
        plt.scatter(max_date, max_price, color='red', label='Максимальная цена' if year == df['year'].unique()[0] else"")

plt.title("Цена на горох с 2013 по 2023")
plt.xlabel("Дата")
plt.ylabel("Цена")
plt.legend()
plt.grid(True)
plt.show()