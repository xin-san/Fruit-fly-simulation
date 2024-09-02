#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objects as go 
import nestgpu as ngpu
import numpy as np
import ast
from scipy.interpolate import griddata
from scipy.interpolate import SmoothBivariateSpline
from scipy.interpolate import LinearNDInterpolator
from scipy.ndimage import gaussian_filter


# In[2]:


positions = pd.read_csv('../connectome_materials/coordinates.csv.gz')
neroInfo = pd.read_csv('../connectome_materials/classification.csv.gz')



# In[3]:


# convert position to three columns x,y,z

def split_coordinates(coord_string):
    return [int(x) for x in coord_string.strip('[]').split()]

positions['position'] = positions['position'].apply(split_coordinates)

positions['x'] = positions['position'].apply(lambda x: x[0])
positions['y'] = positions['position'].apply(lambda x: x[1])
positions['z'] = positions['position'].apply(lambda x: x[2])

position_Info_List = ['root_id', 'x', 'y', 'z']
positions = positions[position_Info_List]


# In[4]:


Optic_neurons_Right = neroInfo[(neroInfo['super_class'] == 'optic') & (neroInfo['side'] == 'right')]
Sensory_neurons_Right = neroInfo[(neroInfo['super_class'] == 'sensory') & (neroInfo['side'] == 'right')]
# Sensory_neurons_Right['cell_type'].unique()


# In[5]:


#Retina
# R1-R6
R1_6_Right_Info = Sensory_neurons_Right[Sensory_neurons_Right['cell_type'] == 'R1-6'] 
R1_6_Right_Info = R1_6_Right_Info[['root_id']]

# R7-8
R7_8_List = ['R7', 'R8']
R7_8_Right_Info = Sensory_neurons_Right[Sensory_neurons_Right['cell_type'].isin(R7_8_List)]
R7_8_Right_Info = R7_8_Right_Info[['root_id']]

#ocellar_retinula_cell
ocellar_retinula_Right_Info = Sensory_neurons_Right[Sensory_neurons_Right['cell_type'] == 'ocellar_retinula_cell']
ocellar_retinula_Right_Info = ocellar_retinula_Right_Info[['root_id']]

#Lamina
# L1-5
L1_5_Right_Info = Optic_neurons_Right[Optic_neurons_Right['sub_class'] == 'L1-5'] 
L1_5_Right_Info = L1_5_Right_Info[['root_id']]

# ***T1-3***
T1_3_List = ['T1', 'T2', 'T3']
T1_3_Right_Info = Optic_neurons_Right[Optic_neurons_Right['cell_type'].isin(T1_3_List)]
T1_3_Right_Info = T1_3_Right_Info[['root_id']]

# amacrine
Am_Right_Info = Optic_neurons_Right[Optic_neurons_Right['cell_type'] == 'Am'] 
Am_Right_Info = Am_Right_Info[['root_id']]

#C2-3
C2_3_List = ['C2', 'C3']
C2_3_Right_Info = Optic_neurons_Right[Optic_neurons_Right['cell_type'].isin(C2_3_List)]
C2_3_Right_Info = C2_3_Right_Info[['root_id']]




# In[ ]:




