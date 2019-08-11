#simple linear regression
import  matplotlib.pyplot as plt
import pandas as pd 
import pylab as pl
import numpy as np
#%matplotlib inline
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
#reads the data
df =  pd.read_csv("FuelConsumption.csv")
df.head()