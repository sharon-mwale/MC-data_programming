import pandas as pd
import numpy as np

data = pd.read_csv('dataset.csv')

print(data.head())

filtered_data = data[data['Age'] > 30]

sorted_data = data.sort_values('Salary', ascending=False)

data['Salary'] = data['Salary'].apply(lambda x: x * 1.1)  

data.dropna(inplace=True)  
data['Age'].fillna(data['Age'].median(), inplace=True)  

#data['Height'] = (data['Height'] - data['Height'].mean()) / data['Height'].std()

data = pd.get_dummies(data, columns=['Gender'], drop_first=True)

print(data.describe())

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns


plt.scatter(data['Age'], data['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()

for index, row in data.iterrows():
    if row['Age'] > 40:
        data.loc[index, 'Category'] = 'Senior'
    else:
        data.loc[index, 'Category'] = 'Junior'


data.to_csv('processed_data.csv', index=False)

sales_data = pd.read_csv('sales_data.csv')  # Replace 'sales_data.csv' with the actual filename

print(sales_data.head())

total_sales = sales_data.groupby('Product Category')['Quantity'].sum()

sales_data['Sales Price'] = sales_data['Revenue'] / sales_data['Quantity']
average_sales_price = sales_data.groupby('Product')['Sales Price'].mean()

top_selling_products = sales_data.groupby('Product')['Quantity'].sum().nlargest(5)

plt.figure(figsize=(8, 6))
sns.barplot(x='Product Category', y='Revenue', data=sales_data)
plt.xlabel('Product Category')
plt.ylabel('Total Revenue')
plt.title('Sales by Product Category')
plt.show()