
# coding: utf-8

# In[ ]:


'''
- Intersecting Street is used only if House Number and Street Name are empty or if response res[] is empty
- If there are more then one address exists in response res[] then only first pair of Latitude and Longitude is taken
'''


# In[ ]:


import pandas as pd #pip install pandas
import numpy as np #pip install numpy
import googlemaps #pip install -U googlemaps
from pprint import pprint


# In[ ]:


#setup API key
gmaps = googlemaps.Client(key='AIzaSyBr-3kEqWuwylwgO6VIWUVJMPRzq0zxQV4')


# In[ ]:


#open downloaded csv file Parking_Violations_Issued_-_Fiscal_Year_2018.csv with pandas
data = pd.read_csv('Parking_Violations_Issued_-_Fiscal_Year_2018.csv', dtype={'Violation Legal Code': object,
                                                                             'Violation Post Code': object,
                                                                             'Violation Description': object}, 
                                                                       nrows=4500) # 4500 rows


# In[ ]:


#add two columns
data.insert(26, 'Latitude', np.nan)
data.insert(27, 'Longitude', np.nan) 


# In[ ]:


for index, row in data.iterrows():
    if str(row['House Number']) == 'nan' and str(row['Street Name']) == 'nan':
        inrs_street = str(row['Intersecting Street']) if str(row['Intersecting Street']) != 'nan' else ' '
        res = gmaps.geocode(inrs_street, region='us')
    else:
        hs_number = str(row['House Number']) if str(row['House Number']) != 'nan' else ''
        str_name = str(row['Street Name']) if str(row['Street Name']) != 'nan' else ''
        res = gmaps.geocode(hs_number + ' ' + str_name, region='us')
    if res == []:
        inrs_street = str(row['Intersecting Street']) if str(row['Intersecting Street']) != 'nan' else ' '
        res = gmaps.geocode(inrs_street, region='us')
    if len(res) > 0:
        #res[0] - only first pair lat and lng is taken
        data.iloc[index, 26] = str(res[0].get('geometry').get('location').get('lat'))
        data.iloc[index, 27] = str(res[0].get('geometry').get('location').get('lng'))
    


# In[ ]:


data.to_csv('Geocode_4500_Parking_Violations_Issued_-_Fiscal_Year_2018.csv', index=False)

