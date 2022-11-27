#!/usr/bin/env python
# coding: utf-8

# # **Statistical Learning for Automation Systems**
# 
#        
# ## *Prof. Simone Formentin*
# 
# ___
# 
# # Classification with Neural Networks - Case Study
# 
# Let's consider an example of classification problem solved by using Neural Networks.
# 
# ## Dataset Description
# 
# ### Breast cancer wisconsin (diagnostic) dataset
# --------------------------------------------
# 
# **Data Set Characteristics:**
# 
#     :Number of Instances: 569
# 
#     :Number of Attributes: 30 numeric, predictive attributes and the class
# 
#     :Attribute Information:
#         - radius (mean of distances from center to points on the perimeter)
#         - texture (standard deviation of gray-scale values)
#         - perimeter
#         - area
#         - smoothness (local variation in radius lengths)
#         - compactness (perimeter^2 / area - 1.0)
#         - concavity (severity of concave portions of the contour)
#         - concave points (number of concave portions of the contour)
#         - symmetry 
#         - fractal dimension ("coastline approximation" - 1)
# 
#         The mean, standard error, and "worst" or largest (mean of the three
#         largest values) of these features were computed for each image,
#         resulting in 30 features.  For instance, field 3 is Mean Radius, field
#         13 is Radius SE, field 23 is Worst Radius.
# 
#         - class:
#                 - WDBC-Malignant
#                 - WDBC-Benign
# 
#     :Summary Statistics:
# 
#     ===================================== ====== ======
#                                            Min    Max
#     ===================================== ====== ======
#     radius (mean):                        6.981  28.11
#     texture (mean):                       9.71   39.28
#     perimeter (mean):                     43.79  188.5
#     area (mean):                          143.5  2501.0
#     smoothness (mean):                    0.053  0.163
#     compactness (mean):                   0.019  0.345
#     concavity (mean):                     0.0    0.427
#     concave points (mean):                0.0    0.201
#     symmetry (mean):                      0.106  0.304
#     fractal dimension (mean):             0.05   0.097
#     radius (standard error):              0.112  2.873
#     texture (standard error):             0.36   4.885
#     perimeter (standard error):           0.757  21.98
#     area (standard error):                6.802  542.2
#     smoothness (standard error):          0.002  0.031
#     compactness (standard error):         0.002  0.135
#     concavity (standard error):           0.0    0.396
#     concave points (standard error):      0.0    0.053
#     symmetry (standard error):            0.008  0.079
#     fractal dimension (standard error):   0.001  0.03
#     radius (worst):                       7.93   36.04
#     texture (worst):                      12.02  49.54
#     perimeter (worst):                    50.41  251.2
#     area (worst):                         185.2  4254.0
#     smoothness (worst):                   0.071  0.223
#     compactness (worst):                  0.027  1.058
#     concavity (worst):                    0.0    1.252
#     concave points (worst):               0.0    0.291
#     symmetry (worst):                     0.156  0.664
#     fractal dimension (worst):            0.055  0.208
#     ===================================== ====== ======
# 
#     :Missing Attribute Values: None
# 
#     :Class Distribution: 212 - Malignant, 357 - Benign
# 
#     :Creator:  Dr. William H. Wolberg, W. Nick Street, Olvi L. Mangasarian
# 
#     :Donor: Nick Street
# 
#     :Date: November, 1995
# 
# This is a copy of UCI ML Breast Cancer Wisconsin (Diagnostic) datasets.
# https://goo.gl/U2Uwz2
# 
# Features are computed from a digitized image of a fine needle
# aspirate (FNA) of a breast mass.  They describe
# characteristics of the cell nuclei present in the image.
# 
# Separating plane described above was obtained using
# Multisurface Method-Tree (MSM-T) [K. P. Bennett, "Decision Tree
# Construction Via Linear Programming." Proceedings of the 4th
# Midwest Artificial Intelligence and Cognitive Science Society,
# pp. 97-101, 1992], a classification method which uses linear
# programming to construct a decision tree.  Relevant features
# were selected using an exhaustive search in the space of 1-4
# features and 1-3 separating planes.
# 
# The actual linear program used to obtain the separating plane
# in the 3-dimensional space is that described in:
# [K. P. Bennett and O. L. Mangasarian: "Robust Linear
# Programming Discrimination of Two Linearly Inseparable Sets",
# Optimization Methods and Software 1, 1992, 23-34].
# 
# This database is also available through the UW CS ftp server:
# 
# ftp ftp.cs.wisc.edu
# cd math-prog/cpo-dataset/machine-learn/WDBC/
# 
# .. topic:: References
# 
#    - W.N. Street, W.H. Wolberg and O.L. Mangasarian. Nuclear feature extraction 
#      for breast tumor diagnosis. IS&T/SPIE 1993 International Symposium on 
#      Electronic Imaging: Science and Technology, volume 1905, pages 861-870,
#      San Jose, CA, 1993.
#    - O.L. Mangasarian, W.N. Street and W.H. Wolberg. Breast cancer diagnosis and 
#      prognosis via linear programming. Operations Research, 43(4), pages 570-577, 
#      July-August 1995.
#    - W.H. Wolberg, W.N. Street, and O.L. Mangasarian. Machine learning techniques
#      to diagnose breast cancer from fine-needle aspirates. Cancer Letters 77 (1994) 
#      163-171.

# ## Import Data Analysis and Visualization Libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Import Dataset

# In[2]:


df = pd.read_csv('cancer_classification.csv')          # Import Dataset from .csv file


# In[3]:


df.head()                                              # Show header


# In[4]:


df.info()


# In[5]:


df.describe().transpose()


# ## Exploratory Data Analysis

# In[6]:


sns.countplot(x='benign_0__mal_1',data=df)                  # Show entries count for each class malignant/benign


# In[7]:


plt.figure(figsize=(12,8))                                  # Create a figure object with a specified figure size

sns.heatmap(df.corr())                                      # Plot Correlation Matrix as heatmap


# In[8]:


df.corr()['benign_0__mal_1'].sort_values(ascending = False)                # Sort correlation coefficients computed between each feature and target variable (class)


# In[9]:


plt.figure(figsize=(12,8))                                        # Create a figure object with a specified figure size

df.corr()['benign_0__mal_1'].sort_values().plot(kind='bar')       # Barplot for the sorted correlation coefficients


# In[10]:


plt.figure(figsize=(12,8))                                              # Create a figure object with a specified figure size

df.corr()['benign_0__mal_1'][:-1].sort_values().plot(kind='bar')        # Barplot for the sorted correlation coefficients (excluding autocorrelation for target variable)


# ## Train/Test Set Split

# In[11]:


from sklearn.model_selection import train_test_split            # Import train_test_split function from Scikit-Learn


# In[12]:


# Convert columns of Pandas DataFrame to Numpy arrays

# Features
X = df.drop('benign_0__mal_1',axis=1).values

# Target Variable
y = df['benign_0__mal_1'].values


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)         # Train-Test Split


# In[14]:


X_train.shape


# In[15]:


X_test.shape


# In[16]:


y_train.shape


# In[17]:


y_test.shape


# ## Data Pre-Processing
# 
# Use StandardScaler() to perform input centering and input normalization.
# 
# Notice that it is sufficient to standardize just input features, while it is not necessary to standardize the target variable.

# In[18]:


from sklearn.preprocessing import StandardScaler


# In[19]:


scaler = StandardScaler()                # StandardScaler() object instantiation


# Notice: to prevent data leakage from the test set, we only fit our scaler on the training set.

# In[20]:


scaler.fit(X_train)                      # Fit Standard Scaler only on the training set


# In[21]:


X_train = scaler.transform(X_train)          # Apply Standardization on X_train
X_test = scaler.transform(X_test)            # Apply Standardization on X_test


# ## Neural Network Definition - TensorFlow & Keras

# ## Creating NN Model

# In[22]:


import tensorflow as tf

from tensorflow.keras.models import Sequential                         # Import Sequential() to instatiate a Feed-forward NN object
from tensorflow.keras.layers import Dense                              # Import Dense() to instatiate fully-connected layer objects


# In[23]:


model = Sequential()

model.add(Dense(units=30,activation='relu'))
model.add(Dense(units=15,activation='relu'))

# Final output node for prediction
model.add(Dense(units=1,activation='sigmoid'))                          # In the output layer we just have one neuron since the target is a single variable (class)
 
# For a binary classification problem
model.compile(loss='binary_crossentropy', optimizer='adam')             # Optimizer determines the way in which you approach gradient descent (alternative: ADAM)


# ## Training the Model 
# 
# ### Example One: Choosing too many epochs and overfitting!

# In[24]:


model.fit(x=X_train, y=y_train, epochs=600, validation_data=(X_test, y_test), verbose=1)


# In[25]:


model_loss = pd.DataFrame(model.history.history)    # Save Training and Validation Loss in a Pandas DataFrame


# In[26]:


model_loss.head()                                   # Show header (loss = Training Loss, val_loss = Validation Loss)


# In[27]:


# Plot Training / Validation Loss vs Epochs

plt.figure(figsize = (12,8))

plt.plot(range(len(model_loss)), model_loss['loss'], label = 'Training Loss')
plt.plot(range(len(model_loss)), model_loss['val_loss'], label = 'Validation Loss')

plt.xlim([-10, len(model_loss)])
plt.xlabel('Epoch')
plt.ylabel('Training / Validation Loss')
plt.title('Training / Validation Loss vs Epochs')
plt.legend()


# ## Example Two: Early Stopping
# 
# We obviously trained too much! Let's use early stopping to track the val_loss and stop training once it begins increasing too much!

# In[28]:


model = Sequential()

model.add(Dense(units=30,activation='relu'))
model.add(Dense(units=15,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')


# In[29]:


from tensorflow.keras.callbacks import EarlyStopping                 # Import EarlyStopping method


# Stop training when a monitored quantity has stopped improving.
# 
#     Arguments:
#         monitor: Quantity to be monitored.
#         min_delta: Minimum change in the monitored quantity
#             to qualify as an improvement, i.e. an absolute
#             change of less than min_delta, will count as no
#             improvement.
#         patience: Number of epochs with no improvement
#             after which training will be stopped.
#         verbose: verbosity mode.
#         mode: One of `{"auto", "min", "max"}`. In `min` mode,
#             training will stop when the quantity
#             monitored has stopped decreasing; in `max`
#             mode it will stop when the quantity
#             monitored has stopped increasing; in `auto`
#             mode, the direction is automatically inferred
#             from the name of the monitored quantity.

# In[30]:


early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25)       # Define EarlyStopping object and assign it to variable "early_stop"


# In[31]:


model.fit(x=X_train, y=y_train, epochs=600, validation_data=(X_test, y_test), verbose=1, callbacks=[early_stop])     # Fit NN model, including early stopping 


# In[32]:


model_loss = pd.DataFrame(model.history.history)           # Save Training and Validation Loss in a Pandas DataFrame 


# In[33]:


# Plot Training / Validation Loss vs Epochs

plt.figure(figsize = (12,8))

plt.plot(range(len(model_loss)), model_loss['loss'], label = 'Training Loss')
plt.plot(range(len(model_loss)), model_loss['val_loss'], label = 'Validation Loss')

plt.xlim([-10, len(model_loss)])
plt.xlabel('Epoch')
plt.ylabel('Training / Validation Loss')
plt.title('Training / Validation Loss vs Epochs')
plt.legend()


# ## Example Three: Adding in DropOut Layers

# In[34]:


from tensorflow.keras.layers import Dropout                       # Import Dropout method


# In[35]:


help(Dropout)


# In[36]:


model = Sequential()

model.add(Dense(units=30,activation='relu'))
model.add(Dropout(0.5))                                    # Add Dropout option to NN layers

model.add(Dense(units=15,activation='relu'))
model.add(Dropout(0.5))                                    # Add Dropout option to NN layers
  
model.add(Dense(units=1,activation='sigmoid'))
          
model.compile(loss='binary_crossentropy', optimizer='adam')


# In[37]:


model.fit(x=X_train, y=y_train, epochs=600, validation_data=(X_test, y_test), verbose=1, callbacks=[early_stop])


# In[38]:


model_loss = pd.DataFrame(model.history.history)    # Save Training and Validation Loss in a Pandas DataFramemodel_loss.plot()


# In[39]:


# Plot Training / Validation Loss vs Epochs

plt.figure(figsize = (12,8))

plt.plot(range(len(model_loss)), model_loss['loss'], label = 'Training Loss')
plt.plot(range(len(model_loss)), model_loss['val_loss'], label = 'Validation Loss')

plt.xlim([-10, len(model_loss)])
plt.xlabel('Epoch')
plt.ylabel('Training / Validation Loss')
plt.title('Training / Validation Loss vs Epochs')
plt.legend()


# # Model Evaluation

# In[40]:


predictions = model.predict_classes(X_test)               # Create an array containing NN model predictions on the Test Set    


# In[41]:


from sklearn.metrics import classification_report, confusion_matrix             # Import model evaluation Metrics


# In[42]:


print(classification_report(y_test,predictions))


# In[43]:


print(confusion_matrix(y_test,predictions))

