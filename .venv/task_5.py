import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

cars_df = sns.load_dataset('mpg')
cars_df['brand'] = cars_df.name.str.split().str[0].str.lower()
brands = ['bmw', 'ford', 'chrysler', 'volkswagen']
cars_sub_df = cars_df[cars_df.brand.isin(brands)]

print(cars_sub_df.info())
print(cars_sub_df.head())
print(cars_sub_df.describe())

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.boxplot(x='brand', y='horsepower', data=cars_sub_df, ax=axes[0, 0])
axes[0, 0].set_title('Horsepower by Brand')
axes[0, 0].set_xlabel('Brand')
axes[0, 0].set_ylabel('Horsepower')

sns.boxplot(x='brand', y='acceleration', data=cars_sub_df, ax=axes[0, 1])
axes[0, 1].set_title('Acceleration by Brand')
axes[0, 1].set_xlabel('Brand')
axes[0, 1].set_ylabel('Acceleration')

sns.boxplot(x='brand', y='cylinders', data=cars_sub_df, ax=axes[1, 0])
axes[1, 0].set_title('Cylinders by Brand')
axes[1, 0].set_xlabel('Brand')
axes[1, 0].set_ylabel('Cylinders')

sns.boxplot(x='brand', y='mpg', data=cars_sub_df, ax=axes[1, 1])
axes[1, 1].set_title('MPG by Brand')
axes[1, 1].set_xlabel('Brand')
axes[1, 1].set_ylabel('MPG')

fig.suptitle('Comparison of Car Attributes by Brand')
fig.tight_layout(pad=3.0)

plt.show()