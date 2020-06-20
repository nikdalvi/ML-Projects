# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import scipy
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here

#Confidence Interval
data_sample = data.sample(n = sample_size, random_state = 0)
sample_mean = data_sample['installment'].mean()
print('Sample Mean = ',sample_mean)
installment_std = data_sample['installment'].std()
print('S.D = ',installment_std)
margin_of_error = z_critical*(installment_std/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print('confidence_interval = ',[confidence_interval[0],confidence_interval[1]])
true_mean = data['installment'].mean()
print('true_mean = ',true_mean)
print('-'*30)

#CLT
sample_s =np.array([20,50,200])

fig,axes =plt.subplots(3,1, figsize=(10,20))

for i in range(len(sample_s)):
    l=[]
    for j in range(1000):
        mean =data['installment'].sample(sample_s[i]).mean()
        
        l.append(mean)
    mean_series =pd.Series(l)
    axes[i].hist(mean_series,normed =True)
    
plt.show()

#Small Business Interests
mean_int = data['int.rate'].apply(lambda x : float(x.strip('%'))/100).mean()
x1 = data[data['purpose']=='small_business']['int.rate'].apply(lambda x : float(x.strip('%'))/100)
z_statistic_1, p_value_1 = ztest(x1, value = mean_int, alternative = 'larger')
print(("z_statistic is:{}".format(z_statistic_1)))
print(("P_value is :{}".format(p_value_1)))
print('-'*30)

#Installment vs Loan Defaulting
z_statistic_2,p_value_2 =ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])

print(("z_statistic is:{}".format(z_statistic_2)))
print(("P_value is :{}".format(p_value_2)))
print('-'*30)

# Purpose vs Loan Defaulting
observed = pd.crosstab(data['purpose'], data['paid.back.loan'])
chi2, p, dof, ex = stats.chi2_contingency(observed)
print('Chi2 = ', chi2)



