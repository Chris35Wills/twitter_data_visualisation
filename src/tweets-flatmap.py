
# coding: utf-8

# In[80]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets # interactive controls in browser


# In[81]:

tweets_time = np.arange('2015-12-31T00Z', '2016-01-02T00Z', 30, dtype='datetime64[s]') # YYMMDD T00Z == midnight, [s] is seconds


# In[82]:

tweets = np.random.rand(len(tweets_time),2)


# In[83]:

tweets_lon = tweets[:,0]*180-90


# In[84]:

tweets_lat = tweets[:,1]*360-180


# In[85]:

tweets=np.array([tweets_lon,tweets_lat,tweets_time]).transpose() # transpose to get it in correct orientation


# In[105]:

tweets[:,0]


# In[86]:

plt.plot(tweets_lon,tweets_lat,'ro',markersize=1.8)


# In[87]:

len(tweets)


# In[88]:

from mpl_toolkits.basemap import Basemap


# In[113]:

def tweet_merc(i=0):
    my_map=Basemap(projection='merc', resolution='c',
                  lat_0=0,lon_0=0,
                  llcrnrlon=-189,llcrnrlat=-80,
                  urcrnrlon=189,urcrnrlat=80)

    my_map.drawcoastlines()

    my_map.drawcountries()
    my_map.fillcontinents(color='gray',lake_color='b')

    my_map.drawmapboundary()

    my_map.drawmeridians(np.arange(0,360,15))
    my_map.drawparallels(np.arange(-90,90,30))
    
    lon=tweets_lon[i]
    lat=tweets_lat[i]

    x,y=my_map(lat,lon)
    my_map.plot(x,y,'bo',markersize=12)
                    
    plt.show()


# In[114]:

tweets_len = len(tweets_lon)
interact(tweet_merc,i=(0,tweets_len,1))


# In[93]:

tweets_lon[1]


# In[ ]:



