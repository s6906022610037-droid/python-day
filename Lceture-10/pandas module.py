import pandas as pd
data = {
    'Name': ['Alice', 'Bod', 'Charlie'], 
    'Age': [25, 30, 35], 
    'City': ['New York', 'Los Angles', 'Chicago']}
df = pd.DataFrame(data)
print("dataFrame:\n", df)

average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

filter_df = df[df['Age'] > 28]
print("\nFiltered DataFrame (Age > 28 ) :\n", filter_df)

df['Salary'] = [50000, 60000, 70000] 
print("\nDataFrame with Salary column:\n", df)
