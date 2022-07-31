#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns


# In[2]:


#TASK 1: setting datasets


# In[3]:


dataset_2012 = pd.read_csv("dataset_2012.csv")
#print(dataset_2012.head())
#dataset 2012/13


# In[4]:


dataset_2013 = pd.read_csv("dataset_2013.csv")
#print(dataset_2013.head())
#dataset 2013/14


# In[5]:


dataset_2014 = pd.read_csv("dataset_2014.csv")
#dataset 2014/15


# In[6]:


dataset_2015 = pd.read_csv("dataset_2015.csv")
#dataset 2015/16


# In[7]:


dataset_2016 = pd.read_csv("dataset_2016.csv")
#dataset 2016/17


# In[8]:


dataset_2017 = pd.read_csv("dataset_2017.csv")
#dataset 2017/18


# In[9]:


dataset_2018 = pd.read_csv("dataset_2018.csv")
#dataset 2018/19


# In[10]:


dataset_2019 = pd.read_csv("dataset_2019.csv")
#dataset 2019/20


# In[11]:


dataset_2020 = pd.read_csv("dataset_2020.csv")
#dataset 2020/21


# In[12]:


#TASK 2: Counting total offences by year


# In[13]:


offences_2012 =dataset_2012["Number of Offences"].sum()
print("Total offennces in 2012 are:",offences_2012)


# In[14]:


offences_2013 =dataset_2013["Number of Offences"].sum()
print("Total offennces in 2013 are:",offences_2013)


# In[15]:


offences_2014 =dataset_2014["Offence Count"].sum()
print("Total offennces in 2014 are:",offences_2014)


# In[16]:


offences_2015 =dataset_2015["Offence Count"].sum()
print("Total offennces in 2015 are:",offences_2015)


# In[17]:


offences_2016 =dataset_2016["Offence Count"].sum()
print("Total offennces in 2016 are:",offences_2016)


# In[18]:


offences_2017 =dataset_2017["Offence Count"].sum()
print("Total offennces in 2017 are:",offences_2017)


# In[19]:


offences_2018 =dataset_2018["Offence Count"].sum()
print("Total offennces in 2018 are:",offences_2018)


# In[20]:


offences_2019 =dataset_2019["Offence Count"].sum()
print("Total offennces in 2019 are:",offences_2019)


# In[21]:


offences_2020 =dataset_2020["Offence Count"].sum()
print("Total offennces in 2020 are:",offences_2020)


# In[22]:


#TASK 3: data visualisation (by using matplotlib) of total offences by each year


# In[23]:


from matplotlib import pyplot as pl


# In[26]:


x = ["2012/13", "2013/14", "2014/15", "2015/16", "2016/17", "2017/18", "2018/19", "2019/20", "2020/21"]
y = [4064863,4028602 ,4167619, 4515808, 4976372, 5529910, 5963176, 6080793, 1242195]
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Offence Count")
plt.xticks(rotation = 25)
plt.xlabel('Year')
plt.ylabel('Count (millions)')
plt.title('Crime outcomes', fontsize = 20)
plt.grid()
plt.legend()
plt.show ()


# In[ ]:


#TASK 4: Prediction for year 2021/22 in base of https://www.gov.uk/government/statistics/crime-outcomes-in-england-and-wales-2021-to-2022/crime-outcomes-in-england-and-wales-2021-to-2022


# In[9]:


x = ["2012/13", "2013/14", "2014/15", "2015/16", "2016/17", "2017/18", "2018/19", "2019/20", "2020/21", "2021/22", "2022/23"]
y = [4064863,4028602 ,4167619, 4515808, 4976372, 5529910, 5963176, 6080793, 1242195, 5801376, 6309243 ]
plt.plot(x, y, color = 'r', linestyle = 'dashed',
         marker = 'o')
plt.xticks(rotation = 25)
plt.xlabel('Year')
plt.ylabel('Count (millions)')
plt.title('Predictions for 2022/2023', fontsize = 20)
plt.grid()
plt.show ()


# In[129]:


# TASK 5: DATA ANALYSIS OF PERIOD 2012/13


# In[32]:


print (dateset_2012)


# In[20]:


dataset_2012['Offence Group'].value_counts(ascending=False)
#count the number of offence group in the dataset


# In[123]:


df1 =dataset_2012.groupby(['Offence Group'])['Number of Offences'].sum()
df1
#count total number of offences by offence group type


# In[ ]:


#TASK 6: DATA ANALYSIS OF PERIOD 2019/20


# In[130]:


print (dateset_2019)


# In[132]:


df2 =dataset_2019.groupby(['Offence Group'])['Offence Count'].sum()
df2
#count total number of offences by offence group type


# In[ ]:


# TASK 7: Count of offences throughout the year at 4 main forces in UK


# In[38]:


df3 =dataset_2012.groupby(['Force Name'])['Number of Offences'].sum()
print("Total offennces in 2012 at West midlands",df3['West Midlands'])
print("Total offennces in 2012 at Metropolitan Police",df3 ['Metropolitan Police'])
print("Total offennces in 2012 at West Yorkshire",df3 ['West Yorkshire'])
print("Total offennces in 2012 at Greater Manchester",df3 ['Greater Manchester'])


# In[39]:


df4 =dataset_2013.groupby(['Force Name'])['Number of Offences'].sum()
print("Total offennces in 2013 at West midlands",df4['West Midlands'])
print("Total offennces in 2013 at Metropolitan Police",df4 ['Metropolitan Police'])
print("Total offennces in 2013 at West Yorkshire",df4 ['West Yorkshire'])
print("Total offennces in 2013 at Greater Manchester",df4 ['Greater Manchester'])


# In[42]:


df5 =dataset_2014.groupby(['Force Name'])['Offence Count'].sum()
print("Total offennces in 2014 at West midlands",df5['West Midlands'])
print("Total offennces in 2014 at Metropolitan Police",df5 ['Metropolitan Police'])
print("Total offennces in 2014 at West Yorkshire",df5 ['West Yorkshire'])
print("Total offennces in 2014 at Greater Manchester",df5 ['Greater Manchester'])


# In[44]:


df6 =dataset_2015.groupby(['Force Name'])['Offence Count'].sum()
print("Total offennces in 2015 at West midlands",df6['West Midlands'])
print("Total offennces in 2015 at Metropolitan Police",df6 ['Metropolitan Police'])
print("Total offennces in 2015 at West Yorkshire",df6 ['West Yorkshire'])
print("Total offennces in 2015 at Greater Manchester",df6 ['Greater Manchester'])


# In[45]:


df7 =dataset_2016.groupby(['Force Name'])['Offence Count'].sum()
print("Total offennces in 2016 at West midlands",df7['West Midlands'])
print("Total offennces in 2016 at Metropolitan Police",df7 ['Metropolitan Police'])
print("Total offennces in 2016 at West Yorkshire",df7 ['West Yorkshire'])
print("Total offennces in 2016 at Greater Manchester",df7 ['Greater Manchester'])


# In[46]:


df8 =dataset_2017.groupby(['Force Name'])['Offence Count'].sum()
print("Total offennces in 2017 at West midlands",df8['West Midlands'])
print("Total offennces in 2017 at Metropolitan Police",df8 ['Metropolitan Police'])
print("Total offennces in 2017 at West Yorkshire",df8 ['West Yorkshire'])
print("Total offennces in 2017 at Greater Manchester",df8 ['Greater Manchester'])


# In[47]:


df9 =dataset_2018.groupby(['Force Name'])['Offence Count'].sum()
print("Total offennces in 2018 at West midlands",df9['West Midlands'])
print("Total offennces in 2018 at Metropolitan Police",df9 ['Metropolitan Police'])
print("Total offennces in 2018 at West Yorkshire",df9 ['West Yorkshire'])
print("Total offennces in 2018 at Greater Manchester",df9 ['Greater Manchester'])


# In[48]:


df10 =dataset_2019.groupby(['Force Name'])['Offence Count'].sum()
print("Total offennces in 2019 at West midlands",df10['West Midlands'])
print("Total offennces in 2019 at Metropolitan Police",df10 ['Metropolitan Police'])
print("Total offennces in 2019 at West Yorkshire",df10 ['West Yorkshire'])
print("Total offennces in 2019 at Greater Manchester",df10 ['Greater Manchester'])


# In[29]:


x_1 = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"] #years
y_1 = [170747, 174525,176280, 185632, 206630, 233685, 259915, 260770 ] # west midlands police
y_2 = [770220, 698729,700886, 740586, 775476, 821553, 863408, 904932] # metropolitan police
y_3 = [164796, 174525,157811, 202653, 239082, 265703,295901, 288168] # west yorkshire
y_4 = [181146, 181828,200280, 224773, 267480, 339673,333681, 299137] #greater manchester
plt.plot(x_1, y_1, label='West Midlands Police')
plt.plot(x_1, y_2, label='Metropolitan Police')
plt.plot(x_1, y_3, label='West Yorkshire')
plt.plot(x_1, y_4, label='Greater Manchester')
plt.xlabel('Year')
plt.ylabel('Offence Count')
plt.title('Crime trend at main four forces (by population)')
plt.grid(True)
plt.legend()


# In[ ]:


#westmidlands_dataset = dataset_2019[dataset_2019['Force Name'] == "West Midlands"]
#westmidlands_dataset['Offence Count'].sum() #line to count total number of offensces within the Force

