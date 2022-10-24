import pandas

# #creating the d_frame from list lst

# lst = ['Geeks', 'for', 'Geeks', 'is', 'portal', 'for', 'Geeks']
# df_from_list = pandas.DataFrame(lst)
# print(df_from_list)

# #using dicts

# data = {'name': ['John', 'Mwaura', 'Nafula', 'Mkamburi'], 'age': [20, 12, 18, 22]}
# df_from_dict = pandas.DataFrame(data)
# print(df_from_dict)

#accessing column names thru dict keys

# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# df = pandas.DataFrame(data)
# print(df)
# print('\n')
# print(df[['Name', 'Qualification']])

# working with rows in csv files and columns

# data = pandas.read_csv('nba.csv', index_col='Name')
# # first = data.loc['Avery Bradley']
# # second = data.loc['R.J. Hunter']
# # print(first, '\n\n\n', second)
# row2 = data.iloc[30]
# print(row2)

# checking null values
# import numpy as np
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
# pd = pandas.DataFrame(dict)
# print(pd.dropna())

# iterating rows with functions
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

df = pandas.DataFrame(dict)
# for i in df.iterrows():
#     print(i)
#     print()

columns = list(df)
print(columns)
for i in columns:
    print(df[i][2])


# hashed the whole thing coz its really a mixture, a result of learning.

