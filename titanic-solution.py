#!/usr/bin/env python
# coding: utf-8

# # Titanic: Machine Learning from Disaster
# ### Predict survival on the Titanic
# - Defining the problem statement
# - Collecting the data
# - Exploratory data analysis
# - Feature engineering
# - Modelling
# - Testing

# ## 1. Defining the problem statement
# Complete the analysis of what sorts of people were likely to survive.  
# In particular, we ask you to apply the tools of machine learning to predict which passengers survived the Titanic tragedy.

# ![100_anniversary_titanic_sinking_by_esai8mellows-d4xbme8.jpg](attachment:100_anniversary_titanic_sinking_by_esai8mellows-d4xbme8.jpg)

# ## 2. Collecting the data
# 
# training data set and testing data set are given by Kaggle
# you can download from  
# or you can download from kaggle directly [kaggle](https://www.kaggle.com/c/titanic/data)  
# 
# ### load train, test dataset using Pandas

# ## 3. Exploratory data analysis
# Printing first 5 rows of the train dataset.

# ### Data Dictionary
# - Survived: 	0 = No, 1 = Yes  
# - pclass: 	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd  	
# - sibsp:	# of siblings / spouses aboard the Titanic  	
# - parch:	# of parents / children aboard the Titanic  	
# - ticket:	Ticket number	
# - cabin:	Cabin number	
# - embarked:	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton  

# **Total rows and columns**
# 
# We can see that there are 891 rows and 12 columns in our training dataset.

# We can see that *Age* value is missing for many rows. 
# 
# Out of 891 rows, the *Age* value is present only in 714 rows.
# 
# Similarly, *Cabin* values are also missing in many rows. Only 204 out of 891 rows have *Cabin* values.

# There are 177 rows with missing *Age*, 687 rows with missing *Cabin* and 2 rows with missing *Embarked* information.

# ### import python lib for visualization

# ### Bar Chart for Categorical Features
# - Pclass
# - Sex
# - SibSp ( # of siblings and spouse)
# - Parch ( # of parents and children)
# - Embarked
# - Cabin

# The Chart confirms **Women** more likely survivied than **Men**

# The Chart confirms **1st class** more likely survivied than **other classes**  
# The Chart confirms **3rd class** more likely dead than **other classes**

# The Chart confirms **a person aboarded with more than 2 siblings or spouse** more likely survived  
# The Chart confirms ** a person aboarded without siblings or spouse** more likely dead

# The Chart confirms **a person aboarded with more than 2 parents or children** more likely survived  
# The Chart confirms ** a person aboarded alone** more likely dead

# The Chart confirms **a person aboarded from C** slightly more likely survived  
# The Chart confirms **a person aboarded from Q** more likely dead  
# The Chart confirms **a person aboarded from S** more likely dead

# ## 4. Feature engineering
# 
# Feature engineering is the process of using domain knowledge of the data  
# to create features (**feature vectors**) that make machine learning algorithms work.  
# 
# feature vector is an n-dimensional vector of numerical features that represent some object.  
# Many algorithms in machine learning require a numerical representation of objects,  
# since such representations facilitate processing and statistical analysis.

# ### 4.1 how titanic sank?
# sank from the bow of the ship where third class rooms located  
# conclusion, Pclass is key feature for classifier

# ![TItanic-Survival-Infographic.jpg](attachment:TItanic-Survival-Infographic.jpg)

# ### 4.2 Name

# #### Title map
# Mr : 0  
# Miss : 1  
# Mrs: 2  
# Others: 3
# 

# ### 4.3 Sex
# 
# male: 0
# female: 1

# ### 4.4 Age

# #### 4.4.1 some age is missing
# Let's use Title's median age for missing Age

# #### 4.4.2 Binning
# Binning/Converting Numerical Age to Categorical Variable  
# 
# feature vector map:  
# child: 0  
# young: 1  
# adult: 2  
# mid-age: 3  
# senior: 4

# ### 4.5 Embarked

# #### 4.5.1 filling missing values

# more than 50% of 1st class are from S embark  
# more than 50% of 2nd class are from S embark  
# more than 50% of 3rd class are from S embark
# 
# **fill out missing embark with S embark**

# ### 4.6 Fare

# ### 4.7 Cabin

# ### 4.8 FamilySize

# ## 5. Modelling

# ### 6.2 Cross Validation (K-fold)

# ### 6.2.1 kNN

# ### 6.2.2 Decision Tree

# ### 6.2.3 Ramdom Forest

# ### 6.2.4 Naive Bayes

# ### 6.2.5 SVM

# ## 7. Testing
