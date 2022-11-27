#!/usr/bin/env python
# coding: utf-8

# # **Statistical Learning for Automation Systems**
# 
#        
# ## *Prof. Simone Formentin*
# 
# ___
# 
# # Regression with Neural Networks - Case Study

# ## Problem Statement
# 
# Let's consider a dataset containing measurements related to some rare gem stones, with 2 measured features and the sale price. Our final goal would be to try to predict the sale price of a new gem stone we just mined from the ground, in order to try to set a fair price in the market.

# ## Import Data Analysis and Visualization Libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Import Dataset

# In[2]:


df = pd.read_csv('gem_stones.csv')            # Import Dataset from .csv


# In[3]:


df.head()                                     # Show header


# In[4]:


df.info()


# In[5]:


df.describe()


# ## Exploratory Data Analysis

# In[6]:


sns.pairplot(df)


# An approximated linear relationship is fairly evident between feature2 and price.

# ## Test/Train Set Split

# In[7]:


from sklearn.model_selection import train_test_split        # Import train_test_split function from Scikit-Learn


# In[8]:


# Convert columns of Pandas DataFrame to Numpy arrays

# Features
X = np.array(df[['feature1','feature2']])

# Target Variable
y = np.array(df['price'].values)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[9]:


X_train.shape


# In[10]:


X_test.shape


# In[11]:


y_train.shape


# In[12]:


y_test.shape


# ## Data Pre-Processing
# 
# Use StandardScaler() to perform input centering and input normalization.
# 
# Notice that it is sufficient to standardize just input features, while it is not necessary to standardize the target variable.

# In[13]:


from sklearn.preprocessing import StandardScaler


# In[14]:


help(StandardScaler)


# In[15]:


scaler = StandardScaler()                    # StandardScaler() object instantiation


# Notice: to prevent data leakage from the test set, we only fit our scaler on the training set.

# In[16]:


scaler.fit(X_train)                          # Fit Standard Scaler only on the training set


# In[17]:


X_train = scaler.transform(X_train)          # Apply Standardization on X_train
X_test = scaler.transform(X_test)            # Apply Standardization on X_test


# ## Neural Network Definition - TensorFlow & Keras
# 
# There are several ways you can import Keras from Tensorflow. We will use the method shown in the **official TF documentation**.

# In[18]:


import tensorflow as tf


# ## Creating a NN Model
# 
# There are two ways to create MM models through the TensorFlow - Keras API: passing in a list of layers all at once or add them one by one. Let's show both methods.

# In[19]:


from tensorflow.keras.models import Sequential               # Import Sequential() to instatiate a Feed-forward NN object
from tensorflow.keras.layers import Dense                    # Import Dense() to instatiate fully-connected layer objects


# In[20]:


help(Sequential)


# ### NN Model - Specify a list of layers

# In[21]:


model = Sequential([
    Dense(units=2),
    Dense(units=2),
    Dense(units=2)
])                              # Drawback: more difficult to modify the architecture (you should remove layers from the list)


# ### NN Model - Adding layers one by one

# In[22]:


model = Sequential()

model.add(Dense(2))
model.add(Dense(2))
model.add(Dense(2))

# Advantage: easy to modify the architecture (you can just comment out the layers that you want to remove)


# Let's go ahead and build a simple model and then compile it by defining our solver

# In[23]:


model = Sequential()

model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4 ,activation='relu'))

# Final output node for prediction
model.add(Dense(1))                           # In the output layer we just have one neuron since the target is a single variable (price)

model.compile(optimizer='rmsprop', loss='mse')      # Optimizer determines the way in which you approach gradient descent (alternative: ADAM)


# ### Choosing suitable Loss functions and Evaluation Metrics
# 
# Keep in mind what kind of problem you are trying to solve:
# 
#     # For a multi-class classification problem
#     model.compile(optimizer='rmsprop',
#                   loss='categorical_crossentropy',
#                   metrics='accuracy')
# 
#     # For a binary classification problem
#     model.compile(optimizer='rmsprop',
#                   loss='binary_crossentropy',
#                   metrics='accuracy')
# 
#     # For a mean squared error regression problem
#     model.compile(optimizer='rmsprop',
#                   loss='mse')

# ## Training NN Model
# 
# Below are some common definitions that are necessary to know and understand to correctly utilize Keras:
# 
# * Sample: one element of a dataset.
#     * Example: one image is a sample in a convolutional network
#     * Example: one audio file is a sample for a speech recognition model
# * Batch: a set of N samples. The samples in a batch are processed independently, in parallel. If training, a batch results in only one update to the model.A batch generally approximates the distribution of the input data better than a single input. The larger the batch, the better the approximation; however, it is also true that the batch will take longer to process and will still result in only one update. For inference (evaluate/predict), it is recommended to pick a batch size that is as large as you can afford without going out of memory (since larger batches will usually result in faster evaluation/prediction).
# * Epoch: an arbitrary cutoff, generally defined as "one pass over the entire dataset", used to separate training into distinct phases, which is useful for logging and periodic evaluation.
# * When using validation_data or validation_split with the fit method of Keras models, evaluation will be run at the end of every epoch.
# * Within Keras, there is the ability to add callbacks specifically designed to be run at the end of an epoch. Examples of these are learning rate changes and model checkpointing (saving).

# In[24]:


model.fit(X_train, y_train, epochs=250)        


# ## Evaluation
# 
# Let's evaluate our performance on our training set and our test set. We can compare these two performances to check for overfitting.

# In[25]:


model.history.history


# In[26]:


loss = model.history.history['loss']


# In[27]:


# Plot Training Loss per Epoch

plt.figure(figsize=(10,6))

sns.lineplot(x=range(len(loss)),y=loss)

plt.title("Training Loss per Epoch")
plt.xlabel('Epoch')
plt.ylabel('Training Loss Function (MSE)')


# ## Loss evaluation on Training set and Test set.
# 
# These should hopefully be fairly close to each other.

# In[28]:


model.metrics_names


# In[29]:


training_score = model.evaluate(X_train,y_train,verbose=0)
test_score = model.evaluate(X_test,y_test,verbose=0)


# In[30]:


training_score                   # MSE on the Training Set


# In[31]:


test_score                       # MSE on the Test Set


# ### Further Evaluations

# In[32]:


test_predictions = model.predict(X_test)


# In[33]:


test_predictions


# In[34]:


pred_df = pd.DataFrame(y_test,columns=['Test Y'])


# In[35]:


pred_df


# In[36]:


test_predictions = pd.Series(test_predictions.reshape(300,))
pred_df = pd.concat([pred_df,test_predictions],axis=1)
pred_df.columns = ['Test Y','Model Predictions']

pred_df


# ## Real Test Set Labels vs NN Model Predictions

# In[37]:


plt.figure(figsize = (10,6))

sns.scatterplot(x='Test Y',y='Model Predictions',data=pred_df)
plt.title('Real Test Set Labels vs NN Model Predictions - Scatterplot')


# In[38]:


pred_df['Error'] = pred_df['Test Y'] - pred_df['Model Predictions']    # Prediction Error Computation


# In[39]:


sns.distplot(pred_df['Error'],bins=50)                                 # Prediction Error Distribution


# In[40]:


from sklearn.metrics import mean_absolute_error,mean_squared_error


# In[41]:


mean_absolute_error(pred_df['Test Y'],pred_df['Model Predictions'])         # Prediction Error MAE


# In[42]:


mean_squared_error(pred_df['Test Y'],pred_df['Model Predictions'])          # Prediction Error MSE


# In[43]:


# Essentially the same thing, difference just due to precision
test_score


# In[44]:


test_score**0.5                                                             # Prediction Error RMSE


# # Predicting on brand new data
# 
# What if we just saw a brand new gemstone from the ground? What should we price it at? This is the **exact** same procedure as predicting on a new test data!

# In[45]:


# [[Feature1, Feature2]]
new_gem = [[998,1000]]


# In[46]:


# Don't forget to standardize the new input!
new_gem = scaler.transform(new_gem)


# In[47]:


model.predict(new_gem)


# ## Saving and Loading a Model

# In[48]:


from tensorflow.keras.models import load_model


# In[49]:


model.save('my_model.h5')                          # Creates a HDF5 file 'my_model.h5'


# In[50]:


saved_model = load_model('my_model.h5')


# In[51]:


saved_model.predict(new_gem)

