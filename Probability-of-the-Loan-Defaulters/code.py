# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
#Task 1
total = len(df)
p_a = len(df[df['fico']>700])/total
print(p_a)
p_b = len(df[df['purpose']=='debt_consolidation'])/total
print(p_b)
p_a_b = len(df[(df['fico'] > 700) & (df['purpose'] == 'debt_consolidation')]) / total
print(p_a_b)
result = (p_a_b == p_a)
print(result)
print('-'*20)

#Task 2
prob_lb = len(df[df['paid.back.loan']=='Yes'])/total
print(prob_lb)
prob_cs = len(df[df['credit.policy']=='Yes'])/total
print(prob_cs)
prob_pd_cs = (len(df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')])/total)/prob_lb
print(prob_pd_cs)
bayes = ((prob_pd_cs)*(prob_lb))/(prob_cs)
print(bayes)
print('-'*20)
#Task 3
df['purpose'].value_counts().plot(kind='bar')
plt.show()
df1 = df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind='bar')
print('-'*20)

#Task 4
inst_median = df['installment'].median()
print(inst_median)
inst_mean = df['installment'].mean()
print(inst_mean)

df['installment'].hist(bins=50)
plt.axvline(x = inst_median, color ='red')
plt.axvline(x= inst_mean, color = 'green')
plt.show()

df['log.annual.inc'].hist(bins=50)
plt.show()



