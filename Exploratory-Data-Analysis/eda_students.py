#PEOJECT 01


import pandas as pd #Pandas is a library used to work with tables

#Reads CSV file
data=pd.read_csv("students.csv")

#Displays the full dataset
print("The Full Dataset is : ")
print(data)
'''Understanding Data Size and Structures'''
print(" ")
print("Understanding Data Size and Structures : ")
print("The shape(Number of Columns, Number of Rows) of the data is : ")
print(data.shape)
print("The Variable names of each column is : ")
print(data.columns)
'''Check Data Types and Quality'''
print("")
print("The info(Data Types and Quality) of the Data is : ")
print(data.info())
'''Check for missing values'''
print("")
print("Column wise missing values inside the Data is : ")
print(data.isnull().sum())
'''Basic Statistical analysis'''
print("")
print("The Basic Statistiacal analysis(Total Number, Mean, Minimum, Maximum Number, etc.) is : ")
print(data.describe())

'''Visualization of Data'''
print("")
print("Visualization of Data is : ")
import matplotlib.pyplot as plt
plt.hist(data["math_score"])
plt.title("Distribution of Maths Scores")
plt.xlabel("Maths Score")
plt.ylabel("Number of Students")
plt.show()
'''Relation between Variables'''
print("")
print("Relation Between Variables is : ")
plt.scatter(data["study_hours"], data["math_score"])
plt.title("Study Hours vs Math Score")
plt.xlabel("Study Hours")
plt.ylabel("Maths Score")
plt.show()
