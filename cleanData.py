import pandas as pd
import matplotlib.pyplot as plt

# 数据清理逻辑

date_name=['date','comment']
df = pd.read_csv('./comment.csv',header=None,names=date_name,encoding= 'gbk')
df['date'] = pd.to_datetime(df['date'])
print(df['date'].value_counts())
data6 = df['2017-11-06':'2017-11-08']
data6.to_csv('6.txt', encoding = 'utf-8', index = False)
print(data6.size)
data9 = df['2017-11-09':'2017-11-17']
data9.to_csv('9.txt', encoding = 'utf-8', index = False)
print(data9.size)