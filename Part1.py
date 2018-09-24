
# coding: utf-8

# In[ ]:


import pandas as pd #pip install pandas


# In[ ]:


#get tables
city_data = pd.read_html('http://www.city-data.com/accidents/acc-Cincinnati-Ohio.html',
                    index_col=[0],
                   )[8:]


# In[ ]:


#union tables and set index starting with 1
result = pd.concat(city_data, ignore_index=True)
result.index += 1


# In[ ]:


#export to csv
result.to_csv('city_data_all_tables_1982_2014.csv', index_label='#')

