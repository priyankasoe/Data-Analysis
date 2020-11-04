#!/usr/bin/env python
# coding: utf-8

# In[278]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv("Warzone Player Comparison.csv")


# In[4]:


df.head()


# In[9]:


df.describe()


# In[11]:


df.info()


# In[14]:


df['Top Weapon'].unique()


# In[20]:


df['Top Weapon'].value_counts().head(3)


# In[39]:


df['Most Accurate Weapon'].value_counts().head(3)


# In[74]:


topWeapons = df['Top Weapon'].value_counts().head(3).reset_index()["index"].to_list()
mostAccWeapon = df['Most Accurate Weapon'].value_counts().head(3).reset_index()["index"].to_list()


# In[75]:


print(topWeapons)
print(mostAccWeapon)


# In[240]:


fig =  plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)

#axes
plt.xlabel("Accuracy",size=15)
plt.ylabel("K/D",size=15)

#lists for corresponding colors + weapons
colors = ['r','g','b']
colorsList = colors*50
labelsList = topWeapons*50

for weapon in topWeapons:  #loop through most used weapons 
    
    accuracyList, kdList = [],[]
    
    for player in range(len(df)):   #loop through players 
        if df.iloc[player]['Top Weapon']==weapon:
            accuracyList.append(df.iloc[player]['Top Weapon Accuracy'])
            kdList.append(df.iloc[player]['Top Weapon K/D'])
            
    #change to series 
    accuracy = pd.Series(accuracyList,dtype='float64')
    kd = pd.Series(kdList,dtype='float64')
    
    #remove outliers
    accuracy = accuracy[accuracy.between(accuracy.quantile(.15),accuracy.quantile(.85))]
    kd = kd[kd.between(kd.quantile(.15),kd.quantile(.85))]
    
    #plot
    for x,y,c,l in zip(accuracy, kd, colorsList, labelsList):
        plot = ax.scatter(x,y,s=200,color=c,label=l,cmap='viridis',alpha=.2)
    
ax.legend()

plt.show()

# In[147]:


kd = df['Top Weapon K/D']
kd = kd[kd.between(kd.quantile(.15),accuracy.quantile(.85))]
print(kd)


# In[236]:


pd.Series(df.iloc[1]['Top Weapon K/D'])


# In[214]:


len(df)


# In[205]:


fig2 =  plt.figure(figsize=(12,10))
ax2 = fig2.add_subplot(111)

plt.xlabel("Weapon",size=15)
plt.ylabel("Accuracy %",size=15)

topWeaponMean = df["Top Weapon Accuracy"].mean()
accWeaponMean = df["Most Accurate Weapon Accuracy"].mean()

plt.bar(['Top Weapon','Most Accurate Weapon'], height=[topWeaponMean,accWeaponMean],color=['g','c'],alpha=0.5)

plt.show()

# In[277]:


fig3 =  plt.figure(figsize=(12,10))
ax3 = fig3.add_subplot(111)

plt.xlabel("Weapon",size=15)
plt.ylabel("K/D",size=15)

topWeaponMean = df["Top Weapon K/D"].mean()
accWeaponMean = df["Most Accurate Weapon K/D"].mean()

plt.bar(['Top Weapon','Most Accurate Weapon'], height=[topWeaponMean,accWeaponMean],color=['g','c'],alpha=0.5)

plt.show()

# In[249]:


fig4 =  plt.figure(figsize=(12,10))
ax = fig4.add_subplot(111)

#axes
plt.xlabel("Time",size=15)
plt.ylabel("Accuracy",size=15)

#lists for corresponding colors + weapons
colors = ['r','g','b']
colorsList = colors*50
labelsList = topWeapons*50

for weapon in topWeapons:  #loop through most used weapons 
    
    timeList, accuracyList = [],[]
    
    for player in range(len(df)):   #loop through players 
        if df.iloc[player]['Top Weapon']==weapon:
            timeList.append(df.iloc[player]['Time Played( Battle Royale) (days)'])
            accuracyList.append(df.iloc[player]['Top Weapon Accuracy'])
            
    #change to series 
    time = pd.Series(timeList,dtype='float64')
    accuracy = pd.Series(accuracyList,dtype='float64')
    
    #remove outliers
    time = time[time.between(time.quantile(.15),time.quantile(.85))]
    accuracy = accuracy[accuracy.between(accuracy.quantile(.15),accuracy.quantile(.85))]
    
    #plot
    for x,y,c,l in zip(time, accuracy, colorsList, labelsList):
        plot = ax.scatter(x,y,s=200,color=c,label=l,cmap='viridis',alpha=.2)
        
plt.legend()

plt.show()

# In[272]:


fig5 = plt.figure(figsize=(12,10))
ax = fig5.add_subplot(111)

#axes
plt.ylabel("K/D Ratio",size=15)

#remove outliers
twKD,maKD = df['Top Weapon K/D'],df['Most Accurate Weapon K/D']
twKD = twKD[twKD.between(twKD.quantile(.15),twKD.quantile(.75))]
maKD = maKD[maKD.between(maKD.quantile(.15),maKD.quantile(.75))]

#data and color lists
data = [twKD, maKD]
colors = ['r','c']

#plot
bp = ax.boxplot(data,patch_artist=True)

for box,color in zip(bp['boxes'],colors):
    box.set(linewidth=2)
    box.set(facecolor=color,alpha=.5)
    
ax.set_xticklabels(['Top Weapon','Most Accurate Weapon'])

plt.show()

# In[275]:


fig6= plt.figure(figsize=(12,10))
ax = fig6.add_subplot(111)

#axes
plt.ylabel("Accuracy %",size=15)

#remove outliers
twAccuracy,maAccuracy = df['Top Weapon Accuracy'],df['Most Accurate Weapon Accuracy']
twAccuracy = twAccuracy[twAccuracy.between(twAccuracy.quantile(.15),twAccuracy.quantile(.75))]
maAccuracy = maAccuracy[maAccuracy.between(maAccuracy.quantile(.15),maAccuracy.quantile(.75))]

#data and color lists
data = [twAccuracy, maAccuracy]
colors = ['r','c']

#plot
bp = ax.boxplot(data,patch_artist=True)

for box,color in zip(bp['boxes'],colors):
    box.set(linewidth=2)
    box.set(facecolor=color,alpha=.5)
    
ax.set_xticklabels(['Top Weapon','Most Accurate Weapon'])

plt.show()

# In[ ]:




