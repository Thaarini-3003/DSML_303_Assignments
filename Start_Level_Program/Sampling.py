import pandas as pd
import numpy as np

df = pd.read_csv("Health_insurance.csv")
print(df.head())

# print(df.isnull().sum())

print(df.info())
print(df.describe())

#create counts of data for plotting categorical variables
gender = np.unique(df['sex'], return_counts=True)
smoker = np.unique(df['smoker'], return_counts=True)
region = np.unique(df['region'], return_counts=True)
print('gender = {}\n'.format(gender))
print('smoker = {}\n'.format(smoker))
print('region = {}\n'.format(region))



male_charges = df[df['sex'] == 'male']['charges']
female_charges = df[df['sex'] == 'female']['charges']
# print(male_charges)
# print(female_charges)

southeast_charges = df[df['region'] == 'southeast']['charges']
northeast_charges = df[df['region'] == 'northeast']['charges']
southwest_charges = df[df['region'] == 'southwest']['charges']
northwest_charges = df[df['region'] == 'northwest']['charges']
# print(southeast_charges)
# print(northeast_charges)
# print(southwest_charges)
# print(northwest_charges)

smoker_claims = df[df['smoker'] == 'yes']['charges']
non_smoker_claims = df[df['smoker'] == 'no']['charges']
# print(smoker_claims.round(2))
# print(non_smoker_claims.round(2))

from scipy import stats

t_stat, p_value = stats.ttest_ind(male_charges, female_charges, equal_var=False)
print(t_stat)
print(p_value)


t_stat, p_value = stats.ttest_ind(southeast_charges, southwest_charges, equal_var=False)
print(t_stat)
print(p_value)

t_stat, p_value = stats.ttest_ind(northeast_charges, northwest_charges, equal_var=False)
print(t_stat)
print(p_value)


t_stat, p_value = stats.ttest_ind(smoker_claims, non_smoker_claims, equal_var=False)
print(t_stat)
print(p_value)


