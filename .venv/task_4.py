import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('mpg')
df['brand'] = df.name.str.split().str[0]
brands = ['bmw', 'ford', 'chrysler', 'volkswagen']
sub_df = df[df.brand.isin(brands)]

print(sub_df.info())
print(sub_df.head())
print(sub_df.describe())

sns.pairplot(sub_df, vars=['horsepower', 'acceleration', 'cylinders'], hue='brand', palette='Set1')
plt.suptitle('Сравнение параметров BMW, Ford, Chrysler и Volkswagen', y=1.02)
plt.show()