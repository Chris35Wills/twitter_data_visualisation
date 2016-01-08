
# coding: utf-8

# In[21]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap, shiftgrid
from matplotlib.backends import backend_agg as agg # raster backend
from pylab import rcParams


# In[22]:

from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets # interactive controls in browser
get_ipython().magic('matplotlib inline')
rcParams['figure.figsize'] = 8,8


# In[23]:

# Dummy data
tweets_time= np.arange('2015-12-31T00Z', '2016-01-02T00Z', 30, dtype='datetime64[s]') #YYMMDD T00z == midnight, [s] is seconds
tweets = np.random.rand(len(tweets_time),2)
tweets_lon = tweets[:,0]*180-90
tweets_lat = tweets[:,0]*360-180
tweets=np.array([tweets_lat,tweets_lon,tweets_time]).transpose() #transpose data to get correct format

tweets


# In[24]:

# Spinning globe code

# Set up the data
data = tweets
t_lat = data[:,0] 
t_lon = data[:,1]
time = data[:,2]


# In[26]:

def globe_tweet(rot=0,time=0):
    m = Basemap(projection='ortho', lon_0=rot, lat_0=20, resolution='c')
    m.shadedrelief(scale=0.1)
    m.drawcoastlines(color='0.4')
    m.drawcountries(color='0.4')
    m.fillcontinents(color='white',lake_color='gray')
    m.drawparallels(np.arange(-90.,91.,30.))
    m.drawmeridians(np.arange(0., 360., 60.))
    m.drawmapboundary(fill_color='0.8')

    lon=t_lon[time]
    lat=t_lat[time]

    x,y=m(lon,lat)
    m.plot(x,y,'bo',markersize=9)
    plt.show()


# In[27]:

interact(globe_tweet,rot=(-180,180,45),time=(0,1000,1))


# In[ ]:




# In[ ]:



