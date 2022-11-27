#!/usr/bin/env python
# coding: utf-8

# # **Statistical Learning for Automation Systems**
# 
#        
# ## *Prof. Simone Formentin*
# 
# ___
# 
# # K-Means Clustering with Python - Case Study
# 
# K-Means Clustering is an unsupervised learning algorithm that tries to cluster data based on their similarity. Unsupervised learning means that there is no outcome to be predicted and the algorithm just tries to find patterns in the data. 
# 
# In K-Means clustering, it is necessary to specify the number of clusters we want the data to be grouped into. The algorithm randomly assigns each observation to a cluster and finds the centroid of each cluster. Then, the algorithm iterates through two steps:
# 
# * Re-assign data points to the cluster whose centroid is the closest;
# * Calculate new centroid of each cluster.
# 
# These two steps are repeated until the within cluster variation cannot be reduced further. The within cluster variation is calculated as the sum of the euclidean distance between the data points and their respective cluster centroids.

# ## Import Data Analysis and Visualization Libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Dataset of Random Points

# ### Dataset Creation

# In[2]:


data = np.random.rand(300,2)                    # Generate a dataset of 300 random points in a 2-dimensional space (uniformly picked in the interval [0,1])


# In[3]:


data                                            # Show generated dataset


# In[4]:


data[:,0]                                  # Vector containing the first coordinate for each point in the dataset


# In[5]:


data[:,1]                               # Vector containing the second coordinate for each point in the dataset


# ### Data Visualization

# Plot the dataset points in the two-dimensional feature space.

# In[6]:


plt.scatter(data[:,0], data[:,1])

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Data Scatterplot')


# ### K-Means Clustering

# In[7]:


from sklearn.cluster import KMeans                         # Import KMeans() method from Scikit Learn


# In[8]:


kmeans = KMeans(n_clusters = 3)                            # Assign an instantiation of KMeans() to variable 'kmeans', specifying the number of clusters


# In[9]:


kmeans.fit(data)                                           # Computation of K-Means Clustering applied to the dataset points


# In[10]:


kmeans.cluster_centers_                                    # Plot the coordinates of the cluster centers in the two-dimensional feature space


# In[11]:


kmeans.labels_                                             # Plot the label of the cluster each point is associated to after K-Means Clustering application


# ### Plot Original Dataset vs K-Means Clustering Results

# In[12]:


f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,6))

ax1.scatter(data[:,0], data[:,1])
ax1.set_title("Original")
ax1.set_xlabel('Feature 1')
ax1.set_ylabel('Feature 2')

ax2.scatter(data[:,0], data[:,1], c = kmeans.labels_, cmap = 'rainbow')
ax2.set_title('K Means')
ax2.set_xlabel('Feature 1')
ax2.set_ylabel('Feature 2')


# ## Create Dataset using make_blobs() function

# ### Dataset Creation

# In[13]:


from sklearn.datasets import make_blobs                              # Import make_blobs() function from sklearn

# Create Data
data_mb = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=101)


# In[14]:


data_mb                                                                 # Show data


# In[15]:


data_mb[0]               # 2-dimensional array containing the coordinates for each generated point in the 2D feature space


# In[16]:


data_mb[1]               # 1-dimensional array containing the label (cluster) associated to each generated point


# ### Data Visualization

# In[17]:


plt.scatter(data_mb[0][:,0],data_mb[0][:,1],c=data_mb[1],cmap='rainbow')         # Data scatterplot in the 2-dimensional feature space


# ### K-Means Clustering

# In[18]:


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4)


# In[19]:


kmeans.fit(data_mb[0])


# In[20]:


kmeans.cluster_centers_


# In[21]:


kmeans.labels_


# ### Plot Original Dataset vs K-Means Clustering Results

# In[22]:


f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))

ax1.scatter(data_mb[0][:,0],data_mb[0][:,1],c=data_mb[1],cmap='rainbow')
ax1.set_title("Original")
ax1.set_xlabel('Feature 1')
ax1.set_ylabel('Feature 2')

ax2.scatter(data_mb[0][:,0],data_mb[0][:,1],c=kmeans.labels_,cmap='rainbow')
ax2.set_title('K Means')
ax2.set_xlabel('Feature 1')
ax2.set_ylabel('Feature 2')


# Observation: The colors are meaningless in reference between the two plots.

# ## Conclusion
# 
# The proposed case study represents an example of application of K-Means Clustering algorithm to a randomly generated dataset in a two-dimensional feature space. It may be interesting to repeat the analysis on different datasets, specifying different numbers of clusters.
