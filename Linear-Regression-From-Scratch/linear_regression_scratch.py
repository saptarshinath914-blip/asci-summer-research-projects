#PROJECT 02


import pandas as pd #Pandas is a library used to work with tables

#Reads CSV file
data=pd.read_csv("students.csv")

'''Load Data'''
x=data["study_hours"]
y=data["math_score"]

def mean_squared_error(y_true, y_pred):
    n=len(y_true)
    error=0
    for i in range(n):
        error=error+(y_true[i]-y_pred[i])**2
    return error/n

m=0
c=0
learning_rate=0.01
epochs=1000
n=len(x)

for _ in range(epochs):
    y_pred=m*x+c

    dm=(-2/n)*sum(x*(y-y_pred))
    dc=(-2/n)*sum(y-y_pred)

    m=m-learning_rate*dm
    c=c-learning_rate*dc

print("Slope(m) : ",m)
print("Intercept(c) : ",c)

import matplotlib.pyplot as plt
plt.scatter(x,y,label="Actual Data")
plt.plot(x,m*x+c,color="red",label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Math Score")
plt.legend()
plt.show()
