#!/usr/bin/env python
# coding: utf-8

# In[1]:


# the program to  define a simple Series object in the following example by instantiating a Pandas Series object with a list 
import pandas as pd
    S = pd.Series([11,22, 7,33, 55, 8])
    S


# In[2]:


#the code that can directly access the index and the values of our Series S ?
print(S.index)
print(S.values)  



# In[17]:


#two series are taken S and S2 then write the code for addition of these two series with printing the same index 
fruits = ['watermellon', 'lychee', 'cherries', 'pears']
S = pd.Series([10, 63, 2, 10], index=fruits)
S2 = pd.Series([17, 3, 1, 22], index=fruits)
print(S + S2)
print("sum of S: ", sum(S))


# In[18]:


#the program code for the above question if the indices do not have to be the same for the Series addition If an index doesn't occur in both Series, the value for this Series will be NaN
fruits = ['peaches', 'blueberries', 'cherries', 'pears']
fruits2 = ['raspberries', 'oranges', 'cherries', 'pears']
S = pd.Series([20, 33, 52, 10], index=fruits)
S2 = pd.Series([17, 13, 31, 32], index=fruits2)
print(S + S2)


# In[21]:


#a code for Manipulating Pandas Data frame using Applying lambda function to a column
import pandas as pd
values = [['Rhoni', 455], ['lucy', 250], ['grey', 495],
          ['elsa', 400], ['zeref', 350], ['luna', 450]]
  
df = pd.DataFrame(values, columns=['Name', 'Univ_Marks'])
df = df.assign(Percentage=lambda x: (x['Univ_Marks'] / 500 * 100))
df


# In[22]:


#create a Series object in pandas for the resulting Series to contain the dict's keys as the indices and the values as the values
cities = {"London":    8615246, 
          "Berlin":    3562166, 
          "Madrid":    3165235, 
          "Rome":      2874038, 
          "Paris":     2273305, 
          "Vienna":    1805681, 
          "Bucharest": 1803425, 
          "Hamburg":   1760433,
          "Budapest":  1754000,
          "Warsaw":    1740119,
          "Barcelona": 1602386,
          "Munich":    1493900,
          "Milan":     1350680}
city_series = pd.Series(cities)
print(city_series)


# In[24]:


#Three series are defined using pandas write the code to concantenate and show the output display
import pandas as pd
years = range(2014, 2018)
shop1 = pd.Series([2409.14, 2941.01, 3496.83, 3119.55], index=years)
shop2 = pd.Series([1203.45, 3441.62, 3007.83, 3619.53], index=years)
shop3 = pd.Series([3412.12, 3491.16, 3457.19, 1963.10], index=years)
pd.concat([shop1, shop2, shop3])


# In[26]:


#Give an example to derive a dataframe from a dictionary using pandas library function 
cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania", 
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"]}
city= pd.DataFrame(cities)
city


# In[28]:


#Give an example to derive a dataframe from a dictionary using pandas function
import pandas
data = {'ive': {'Age': 15, 'subject': 'java', 'Address': 'Hyderabad'},
        'venai':  {'Age': 9, 'subject': 'python', 'Address': 'Hyderabad'},
        'ziya':  {'Age': 15, 'subject': 'c/c++', 'Address': 'Guntur'},
        'zylith':  {'Age': 21, 'subject': 'html', 'Address': 'ponnur'},
        'sandra':  {'Age': 15, 'subject': 'c/c++', 'Address': 'delhi'}}
  
data = pandas.DataFrame(data)
data


# In[29]:


# the program to change both the column order and the ordering of the index with the function reindex 
city.reindex(index=[0, 2, 4, 6,  8, 10, 12, 1, 3, 5, 7, 9, 11], 
                   columns=['country', 'name', 'population'])


# In[30]:


#the code to rename a dataframe using pandas library function
city.rename(columns={"name":"Soyadı","country":"Ülke","population":"Nüfus"},inplace=True)
city


# In[31]:


# the program for accessing row via indexing value ie select the  German cities in the following example by using 'loc'
city = pd.DataFrame(cities, 
                          columns=("name", "population"), 
                          index=cities["country"])
print(city.loc["Germany"])


# In[33]:


#a program to perform a pivot table format by reshaping a dataframe in pandas library function
import pandas as pd
d = {'A': ['k', 'u', 'm', 'ı', 'l', 'm'],
     'B': ['b', 'i', 'r',  'i',  'r', 'k'],
     'C': [345, 325, 898, 989, 23, 143],
     'D': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(d)
df


# In[34]:


#a program where a Series object with an index of size nvalues. The index will not be unique, because the strings for the index are taken from the list fruits, which has less elements than nvalues
import pandas as pd
import numpy as np
import random
nvalues = 30
values = np.random.randint(1, 20, (nvalues,))
fruits = ["bananas", "oranges", "apples", "clementines", "cherries", "pears"]
fruits_index = np.random.choice(fruits, (nvalues,))
s = pd.Series(values, index=fruits_index)
print(s[:10])


# In[35]:


#a program to get the given series in sorted label form using groupby function so that the solution is gropby iterable form
grouped = s.groupby(s.index)
for fruit, s_obj in grouped:
    print(f"===== {fruit} =====")
    print(s_obj)


# In[48]:


#Write the code for multilevel indexing using Pandas data structures. It's an efficient way to store and manipulate arbitrarily high dimension data in 1-dimensional (Series) and 2-dimensional tabular (DataFrame) structures
import pandas as pd

cities = ["Vienna", "Vienna", "Vienna",
          "Hamburg", "Hamburg", "Hamburg",
          "Berlin", "Berlin", "Berlin",
          "Zürich", "Zürich", "Zürich"]
index = [cities, ["country", "area", "population",
                  "country", "area", "population",
                  "country", "area", "population",
                  "country", "area", "population"]]
print(index)




# In[52]:


#the program to sort the index using slicing operation for the given series in pandas function
city_series = city_series.sort_index()
print("city_series with sorted index:")
print(city_series)
print("\n\nSlicing the city_series:")
city_series["Berlin":"Vienna"]


# In[54]:


#a tuple data =[100, 120, 140, 180, 200, 210, 214] ,using pandas   series  function plot a line plot for the data
import pandas as pd
data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data, index=range(len(data)))
s.plot()



# In[55]:


#the  defined  dcitionary with the population and area figures. This dictionary can be used to create the DataFrame, which we want to use for plotting a line plot
import pandas as pd
cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "area" : [1572, 891.85, 605.77, 1285, 
                    105.4, 414.6, 228, 755, 
                    525.2, 517, 101.9, 310.4, 
                    181.8]
}
city_frame = pd.DataFrame(cities,
                          columns=["population", "area"],
                          index=cities["name"])
print(city_frame)


# In[56]:


# a program for pie chart diagram in pandas for the given series using plot function 
import pandas as pd
fruits = ['apples', 'pears', 'cherries', 'bananas']
series = pd.Series([20, 30, 40, 10], 
                   index=fruits, 
                   name='series')
series.plot.pie(figsize=(6, 6))


# In[57]:


#a program to print the date and time using pandas date-time function
from datetime import date
x = date(1993, 12, 14)
print(x)


# In[58]:


from datetime import date
print(date.min)
print(date.max)


# In[59]:


#a program to show an output a dataframe of data and time 
import pandas as pd
data = pd.date_range('1/1/2011', periods = 10, freq ='H')
 
data


# In[60]:


#time series in pandas write the program to find the index consisting of time stamps
import numpy as np
import pandas as pd
from datetime import datetime, timedelta as delta
ndays = 10
start = datetime(2017, 3, 31)
dates = [start - delta(days=x) for x in range(0, ndays)]
values = [25, 50, 15, 67, 70, 9, 28, 30, 32, 12]
ts = pd.Series(values, index=dates)
ts


# In[61]:


#a program to using a function to return the values lying in the given time duration
import pandas as pd
sr = pd.Series([11, 21, 8, 18, 65, 18, 32, 10, 5, 32, None])
index_ = pd.date_range('2010-10-09 08:45', periods = 11, freq ='H')
sr.index = index_
print(sr)



# In[ ]:




