
# coding: utf-8

# ### ipynb Setting

# In[1]:


# jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000000


# #### Imports

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')

import matplotlib.pylab as pylab
from matplotlib import cm # color


# #### Style Setting

# In[4]:


sns.set_style('whitegrid')

import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True

from matplotlib import rcParams
rcParams['figure.figsize'] = 13.6, 13.6 # figure size in inches


# ### Load at pickle file
QC all_time has some blank columns, but
basically QC group added 2 columns to Illunina Breakdown Report to XLSX
total_cols (170)
* Prefix
* Group

I have corrected one value (Total MB from 'wrong DNA' to 0) and added 2 more columns
total_cols (174)
* Application
* Numeric Total MB
# In[5]:


df_at = pd.read_pickle('../data/at.pickle.gzip')


# In[6]:


df_at.shape


# In[7]:


df_at.info()


# In[8]:


# column names
df_at.columns


# In[9]:


# row number
df_at.index


# #### Create df_ats from df_at

# In[10]:


# QC group care about 'Run Finished Date'

cols_keep = ['Lane Barcode',
             'Metaproject',
             'Midpool Library',
             'Library',
             'Run Finished Date',
             'Total MB',
             'Prefix',
             'Group',
             'Application',
             'Numeric Total MB']

df_ats = df_at[cols_keep]


# In[11]:


df_ats.shape


# In[12]:


df_ats.head(3)


# ####   groupby Application

# In[13]:


df_appl = df_ats.groupby('Application')


# In[14]:


len(df_appl)


# In[15]:


# to view groupby object
df_appl.count()


# In[16]:


len(df_appl)


# In[17]:


df_appl2 = (df_ats.groupby('Application')['Numeric Total MB'].sum()).reset_index()


# In[18]:


df_appl2


# In[19]:


df_appl2['Total TB'] = (df_appl2['Numeric Total MB'] / 1000000)


# In[20]:


df_appl2


# In[21]:


appl = df_appl2['Application']
appl_sizes = df_appl2['Total TB']
print(len(appl), len(appl_sizes))


# In[22]:


def make_explode(num_rows, explode_index):
    base = make_base(num_rows)
    base[explode_index] = 0.05
    return tuple(base)


def make_base(length):
    return [0,]*length


# In[23]:


from matplotlib import cm


# In[24]:


#5

def make_pie(title, labels, sizes, angle, num_rows, explode_index):

    # explode index of the pie slice
    explode = make_explode(num_rows, explode_index)
    
    fig1, ax1 = plt.subplots()
    
    # turn off explode: explode=None
    ax1.pie(sizes,
            labels=labels,
            explode=explode,
            labeldistance=1.2,
            autopct='%1.1f%%',
            shadow=True, 
            startangle=angle)
    
    # figure size
    params = {'figure.figsize': (12.6, 12.6)}
    pylab.rcParams.update(params)
      
    # set title
    fig1.suptitle(title, fontsize=20)
    
    # add legend
    plt.legend(labels, loc="upper right")
    
    # set color
    cs=cm.Set1(np.arange(40)/40.)
    
    # equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal');
    
    # TODO:
    # vertical callout label
    
    # TODO: 
    # correct overlap labels


# #### Chart by Application

# In[41]:


import matplotlib.pyplot as plt
# p2, ax = plt.subplots();


# In[65]:


title = 'HGSC Illumina Distribution of Applications (2007-Present)'
labels = appl
sizes = appl_sizes

# appl_pie
make_pie(title, labels, sizes, 120, 9, 7)


# In[71]:


plt.savefig('p3.png')


# In[72]:


ll p3.png


# In[74]:


get_ipython().system("open -a 'Google Chrome' p3.png")


# In[58]:


# TODO: save fig

# fig = plt.figure()
# fig.savefig('p2.png')

fig = plt.gcf()
plt.draw()
fig.savefig('p2.png')
plt.show()


# In[59]:


get_ipython().system('open p2.png')


# #### groupby Group

# In[ ]:


df_ats.columns


# In[ ]:


df_grp = df_ats.groupby('Group')


# In[ ]:


len(df_grp)


# In[ ]:


df_grp.count()


# In[ ]:


grp = df_grp['Group']
len(grp)


# In[ ]:


df_grp2 = (df_ats.groupby('Group')['Numeric Total MB'].sum()).reset_index()


# In[ ]:


df_grp2


# In[ ]:


df_grp2['Total TB'] = (df_grp2['Numeric Total MB'] / 1000000)


# In[ ]:


df_grp2


# In[ ]:


grp = df_grp2['Group']
grp_sizes = df_grp2['Total TB']


# #### Chart by Group

# In[ ]:


title = 'HGSC Illumina Distribution of Projects (2007-Present)'
labels = grp
sizes = grp_sizes

# grp_pie
p3 = make_pie(title,labels, sizes, 160, 20, 17)


# In[ ]:


p3.figure.savefig("p3.png")

