import numpy as np 
import pandas as pd 

baseline = pd.read_csv('01baseline_result.csv')
action = pd.read_csv('action_20200201.csv')


print(baseline.loc[0, '6'], action.loc[0, 'expect_time'])
difference = 0
for i in range(len(baseline)):
    difference += abs(baseline.loc[i, '6']-action.loc[i, 'expect_time'])

print(difference)  # 16011596