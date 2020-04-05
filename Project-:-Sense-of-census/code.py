# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
print("="*20)
#Code starts here
census = np.concatenate((data,new_record))
print(census)
print("="*20)
#New array age
age = np.array(census[:,0])
print(age)
print("="*20)
#Max Age
max_age = age.max()
print(max_age)
print("="*20)
#Minimum age
min_age = age.min()
print(min_age)
print("="*20)
#Mean of age
age_mean = age.mean()
print(age_mean)
print("="*20)
#Standard deviation of age
age_std = np.std(age)
print (age_std)
print("="*20)

#Subsetting race column
race = np.array(census[:,2])
print(race)
race_0 = (race == 0)
race_1 = (race == 1)
race_2 = (race == 2)
race_3 = (race == 3)
race_4 = (race == 4)
len_0 = len(race[race_0])
print(len_0)
len_1 = len(race[race_1])
print(len_1)
len_2 = len(race[race_2])
print(len_2)
len_3 = len(race[race_3])
print(len_3)
len_4 = len(race[race_4])
print(len_4)
#Minority race
minority_race = len_3
print(minority_race)
print("="*20)
#Calculate working hours
senior_citizens = census[age>60]
print(senior_citizens)

working_hours_sum = senior_citizens.sum(axis =0)[6]
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

# Average Pay
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis =0)[7]
print(avg_pay_high)
print(avg_pay_low)


