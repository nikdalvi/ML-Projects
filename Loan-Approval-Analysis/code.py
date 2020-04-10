# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank = pd.DataFrame(bank_data)
#Categorical values
categorical_var = bank.select_dtypes(include ='object')
print(categorical_var.shape)
#Numerical variable
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.shape)

#New DataFrame
banks = bank.drop(columns ='Loan_ID')

#check all the missing values filled
print(banks.isnull().sum())

#apply mode
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace = True)
# check again all the missing values filled
print(banks.isnull().sum())

#Avg Loan Amount of person
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)

#code for loan approved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes") & (banks["Loan_Status"]=="Y"),["Loan_Status"]].count()
print(loan_approved_se)

#code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No") & (banks["Loan_Status"]=="Y"),["Loan_Status"]].count()
print(loan_approved_nse)

#Percentage of loan approved for SE
percentage_se = (loan_approved_se*100/614)
percentage_se = percentage_se[0]
print(percentage_se)

#Percentage of loan approved NSE
percentage_nse = (loan_approved_nse*100/614)
percentage_nse = percentage_nse[0]
print(percentage_nse)

#Loan amount term
loan_term = banks['Loan_Amount_Term'].apply(lambda x :int(x)/12)
big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)

#Long loan amount term
long_term = banks['Loan_Amount_Term'].apply(lambda x : int(x)/12)
big_loan_term = long_term>=25
print(big_loan_term)

#Avg loan provided based on income
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']
mean_values = loan_groupby.agg([np.mean])
print(mean_values)


