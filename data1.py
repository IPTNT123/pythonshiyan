from dateutil import parser
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as numpy
import pandas as pd
import datetime

# 这是使matplotlib图形内联出现在笔记本中的一个小技巧
# %matplotlib inline

df_ferrara = pd.read_csv('main/ferrara_270615.csv')
df_milano = pd.read_csv('main/milano_270615.csv')
df_mantova = pd.read_csv('main/mantova_270615.csv')
df_ravenna = pd.read_csv('main/ravenna_270615.csv')
df_torino = pd.read_csv('main/torino_270615.csv')
df_asti = pd.read_csv('main/asti_270615.csv')
df_bologna = pd.read_csv('main/bologna_270615.csv')
df_piacenza = pd.read_csv('main/piacenza_270615.csv')
df_cesena = pd.read_csv('main/cesena_270615.csv')
df_faenza = pd.read_csv('main/faenza_270615.csv')


# 温度数据分析-以米兰为例:

# 取出我们要分析的温度和日期数据
y1 = df_milano['temp']
x1 = df_milano['day']


# 把日期数据系统转换成datetime的格式
day_milano = [parser.parse(x) for x in x1]

# 调用subplot函数,fig是图像对象,ax是坐标轴对象
fig, ax = plt.subplots()

# 调整x轴坐标刻度,使其旋转70度,方便查看
plt.xticks(rotation=70)

# 设定时间的格式
hours = mdates.DateFormatter('%H:%M')

# 设定x轴显示的格式
ax.xaxis.set_major_formatter(hours)

# 画出图像,day_milano 是x轴坐标数据,y1是y轴数据,'r'代表的是'red'hongse
ax.plot(day_milano, y1, 'r')

# 显示图像
# plt.show()

# 读取温度和日期数据
y1 = df_ravenna['temp']
x1 = df_ravenna['day']
y2 = df_faenza['temp']
x2 = df_faenza['day']
y3 = df_cesena['temp']
x3 = df_cesena['day']
y4 = df_milano['temp']
x4 = df_milano['day']
y5 = df_asti['temp']
x5 = df_asti['day']
y6 = df_torino['temp']
x6 = df_torino['day']

# 把日期从string类型转化为标准的datetime类型
day_ravenna = [parser.parse(x) for x in x1]
day_faenza = [parser.parse(x) for x in x2]
day_cesena = [parser.parse(x) for x in x3]
day_milano = [parser.parse(x) for x in x4]
day_asti = [parser.parse(x) for x in x5]
day_torino = [parser.parse(x) for x in x6]

# 调用subplos()函数,重新定义fig,ax变量
fig, ax = plt.subplots()
plt.xticks(rotation=70)

hours = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hours)

# 这里需要画出三根线,所以需要三组参数,'g'代表'green'
ax.plot(day_ravenna, y1, 'r', day_faenza, y2, 'r', day_cesena, y3, 'r')
ax.plot(day_milano, y4, 'g', day_asti, y5, 'g', day_torino, y5, 'g')

plt.show()
