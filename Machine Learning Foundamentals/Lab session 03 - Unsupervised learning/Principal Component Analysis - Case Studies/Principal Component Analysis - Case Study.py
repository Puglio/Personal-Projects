#!/usr/bin/env python
# coding: utf-8

# # **Statistical Learning for Automation Systems**
# 
#        
# ## *Prof. Simone Formentin*
# 
# ___

# # Principal Component Analysis with Python - Case Study
# 
# 
# 
# ## PCA Review
# 
# PCA consists in a linear transformation of the available input data and attempts to find out which features mostly explain the variance in the data. 

# <img src='PCA.png' />

# ## Import Data Analysis and Visualization Libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Import Dataset
# 
# We'll work with the built-in Breast Cancer dataset from Scikit Learn since it has a very high number of features.

# In[2]:


from sklearn.datasets import load_breast_cancer                # Import load_breast_cancer


# In[3]:


cancer = load_breast_cancer()                                  # Assign breast cancer dataset to variable 'cancer'


# In[4]:


cancer                                                         # 'cancer' is a variable of type 'Dictionary'


# In[5]:


cancer.keys()


# In[6]:


print(cancer['DESCR'])


# In[7]:


cancer['target_names']


# In[8]:


cancer['target']


# In[9]:


df = pd.DataFrame(cancer['data'], columns = cancer['feature_names'])            # Create a Pandas DataFrame containing cancer data with columns named as features


# In[10]:


df.head()                                                                       # Show DataFrame header


# In[11]:


df.info()


# In[12]:


df.describe()


# ## Principal Component Analysis
# 
# As intuitive, it is difficult to visualize high dimensional data, so we can use PCA for dimensionality reduction. 
# 
# Before doing this, we need to remove bias and scale our data so that each feature has unit variance.

# ### Data Pre-Processing
# 
# Scikit-Learn function named StandardScaler() standardizes features by removing the bias and scaling to unit variance (it automatically performs input centering and input normalization). 

# In[13]:


from sklearn.preprocessing import StandardScaler      # StandardScaler() import


# In[14]:


scaler = StandardScaler()                             # StandardScaler() instantiation
scaler.fit(df)                                        # fit() method computes the mean and std. dev. to be used for later scaling


# In[15]:


scaled_data = scaler.transform(df)                    # transform() method performs standardization by centering and scaling original input data


# ### Singular Value Decomposition

# In[16]:


U, gamma, V = np.linalg.svd(scaled_data, full_matrices=False)          # Compute SVD for scaled_data matrix, obtaining as output the matrices for its factorization: scaled_data = U * diag(gamma) * V'


# In[17]:


gamma                           # gamma is an array of dimension 30 containing the ordered singular values of scaled_data matrix


# In[18]:


gamma.shape


# In[19]:


Gamma = np.diag(gamma)           # Diagonal matrix of dimension 30 * 30 with ordered singular values on the main diagonal
Gamma.shape


# In[20]:


# Plot ordered singular values

plt.figure(figsize = (12,8))

plt.scatter(range(1, len(gamma)+1), gamma)

plt.grid()
plt.ylabel('Singular values')
plt.xlabel('Feature index i')
plt.title('Singular Values Plot')


# Most of the information is contained in the first two principal components. We can use PCA to find the first two principal components and visualize the data in this new, two-dimensional space, with a single scatter plot.

# ### PCA Algorithm

# Instantiate a PCA object, find the principal components using the fit() method, then apply the rotation and dimensionality reduction by calling transform().
# 
# It is also possible to specify how many components we want to keep when creating the PCA object.

# In[21]:


from sklearn.decomposition import PCA                 # PCA() import


# In[22]:


pca = PCA(n_components = 2)                           # PCA() object instantiation (specifying the number of desired components)


# In[23]:


pca.fit(scaled_data)                                  # fit(X) method fits the model with X (it finds the principal components)


# Now we can transform data to the first 2 principal components.

# In[24]:


x_pca = pca.transform(scaled_data)                     # transform(X) method applies dimensionality reduction to X


# In[25]:


scaled_data.shape                                      # Dimensions of standardized dataset before PCA application


# In[36]:


x_pca.shape                                            # Dimensions of dataset after PCA application


# In[41]:


x_pca_df = pd.DataFrame(x_pca, columns=['PC1', 'PC2'])        # Pandas Dataframe containing data in the reduced Feature Space
x_pca_df.head()


# In[42]:


x_pca_df.info()


# Observation: We've reduced 30 dimensions to just 2! Let's plot these two dimensions out!

# ## Plot Data in the Reduced Feature Space

# In[27]:


plt.figure(figsize=(12,8))

sns.scatterplot(x_pca[:,0] , x_pca[:,1], hue = cancer['target'], s = 60)

plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('Input Data Scatterplot in the Reduced Feature Space')
plt.xlim([-10, 20])
plt.ylim([-10, 15])


# By using these two principal components, we can easily separate the two classes (target = 0, target = 1).
# 
# ## Interpreting the components 
# 
# Unfortunately, with this great power of dimensionality reduction, comes the cost of being able to easily understand what these components represent.
# 
# The components correspond to linear combinations of the original features. The components themselves are stored as an attribute of the fitted PCA object:

# In[28]:


pca.components_


# In this numpy matrix array, each row represents a principal component and each column relates back to the original features. 
# 
# We can visualize this relationship with a heatmap.

# In[29]:


df_comp = pd.DataFrame(pca.components_ , columns = cancer['feature_names'])                      # Create a Pandas DataFrame containing the two principal components


# In[30]:


df_comp                                                      # Show df_comp


# In[31]:


# Heatmap Plot
plt.figure(figsize=(12,6))
sns.heatmap(df_comp , cmap='plasma')


# This heatmap and the color bar basically represent the correlation between the various features and the principal component itself.
# 
# ## Conclusion
# 
# The presented case study is an example of application of PCA to a dataset characterized by a very high-dimensional feature space. The drawback relates to the poor interpretability of what principal components represent.
