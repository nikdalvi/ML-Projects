# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace('-','Agender').value_counts()

#To Check does good overpower evil or does evil overwhelm good?
data['Alignment'].hist(bins=10)

# To check if combat relate to person's strength or it's intelligence? (Karl person or Sprearman)
newdf = data[['Intelligence','Strength']]
covariance = newdf.cov().iloc[0,1]
std_intelligence = data['Intelligence'].std()
std_strength = data['Strength'].std()
person = covariance/(std_intelligence * std_strength)
print(person)

#Find the quantile=0.99 value of 'Total' column
total_high= data['Total'].quantile(q=0.99)

super_best=data[data['Total']>total_high]

#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])

#Printing the names
print(super_best_names)



