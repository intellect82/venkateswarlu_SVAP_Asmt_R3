
# coding: utf-8

# In[69]:


# imports
import pandas as pd
import matplotlib.pyplot as plt

# this allows plots to appear directly in the notebook
get_ipython().magic('matplotlib inline')


# In[70]:


# read data into a DataFrame
data = pd.read_csv("DataSet1000N.csv", index_col=0) 
data.head()


# In[71]:


data.columns


# In[72]:


data.dtypes


# In[73]:


data_final=data.drop(['PitchTankTemp','PitchTankVol', 'SterolTankTemp', 'SterolTankVol' ], axis=1)


# In[74]:


data_final.columns


# In[75]:


data_final.columns = ['Steam_Demand','Temperature','Humidity','Rain','Wind']


# In[9]:


data_final.dtypes


# In[10]:


data_final.shape


# In[76]:


# visualize the relationship between the features and the response using scatterplots
fig, axs = plt.subplots(1, 4, sharey=True)
data_final.plot(kind='scatter', x='Temperature', y='Steam_Demand', ax=axs[0], figsize=(16, 8))
data_final.plot(kind='scatter', x='Humidity', y='Steam_Demand', ax=axs[1])
data_final.plot(kind='scatter', x='Rain', y='Steam_Demand', ax=axs[2])
data_final.plot(kind='scatter', x='Wind', y='Steam_Demand', ax=axs[3])


# In[78]:


# create X and y
feature_cols = ['Temperature']
X = data_final[feature_cols]
y = data_final.Steam_Demand

# follow the usual sklearn pattern: import, instantiate, fit
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

# print intercept and coefficients
print(lm.intercept_)
print(lm.coef_)


# In[79]:


# manually calculate the prediction
29584.7267317533 + -33.48756013*50


# In[80]:


# you have to create a DataFrame since the Statsmodels formula interface expects it
X_new = pd.DataFrame({'Temperature': [50]})
X_new.head()


# In[81]:


# use the model to make predictions on a new value
lm.predict(X_new)


# In[82]:


# create a DataFrame with the minimum and maximum values of Temperature
X_new = pd.DataFrame({'Temperature': [data_final.Temperature.min(), data_final.Temperature.max()]})
X_new.head()


# In[83]:


# make predictions for those x values and store them
preds = lm.predict(X_new)
preds


# In[84]:


# first, plot the observed data
data_final.plot(kind='scatter', x='Temperature', y='Steam_Demand')
plt.title('Steam demand  Vs Temperature ', fontsize=14)
# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=2)


# In[86]:


plt.scatter(data_final['Temperature'], data_final['Steam_Demand'], color='red')
plt.title('Steam_Demand Vs  Temperature', fontsize=14)
plt.xlabel('Temperature', fontsize=14)
plt.ylabel('Steam_Demand', fontsize=14)
plt.grid(True)
plt.show()


# In[88]:


import statsmodels.formula.api as smf
lm = smf.ols(formula='Steam_Demand ~ Temperature', data=data_final).fit()
lm.conf_int()


# In[89]:


# print the p-values for the model coefficients
lm.pvalues


# In[22]:


# print the R-squared value for the model
lm.rsquared


# In[90]:


# create X and y
feature_cols = ['Humidity']
X = data_final[feature_cols]
y = data_final.Steam_Demand

# follow the usual sklearn pattern: import, instantiate, fit
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

# print intercept and coefficients
print(lm.intercept_)
print(lm.coef_)


# In[91]:


# manually calculate the prediction
28548.452505109413 + -10.22349707*50


# In[92]:


# you have to create a DataFrame since the Statsmodels formula interface expects it
X_new = pd.DataFrame({'Humidity': [50]})
X_new.head()


# In[93]:


# use the model to make predictions on a new value
lm.predict(X_new)


# In[94]:


# create a DataFrame with the minimum and maximum values of Temperature
X_new = pd.DataFrame({'Humidity': [data_final.Humidity.min(), data_final.Humidity.max()]})
X_new.head()


# In[95]:


# make predictions for those x values and store them
preds = lm.predict(X_new)
preds


# In[96]:


# first, plot the observed data
data_final.plot(kind='scatter', x='Humidity', y='Steam_Demand')

# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=3)


# In[98]:


plt.scatter(data_final['Humidity'], data_final['Steam_Demand'], color='green')
plt.title('Steam_Demand Vs  Humidity', fontsize=14)
plt.xlabel('Humidity', fontsize=14)
plt.ylabel('Steam_Demand', fontsize=14)
plt.grid(True)
plt.show()


# In[100]:


import statsmodels.formula.api as smf
lm = smf.ols(formula='Steam_Demand ~ Humidity', data=data_final).fit()
lm.conf_int()


# In[101]:


# print the p-values for the model coefficients
lm.pvalues


# In[33]:


# print the R-squared value for the model
lm.rsquared


# In[102]:


# create X and y
feature_cols = ['Rain']
X = data_final[feature_cols]
y = data_final.Steam_Demand

# follow the usual sklearn pattern: import, instantiate, fit
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

# print intercept and coefficients
print(lm.intercept_)
print(lm.coef_)


# In[103]:


# manually calculate the prediction
27786.9003310945 + 4390.81255881*50


# In[104]:


# you have to create a DataFrame since the Statsmodels formula interface expects it
X_new = pd.DataFrame({'Rain': [50]})
X_new.head()


# In[105]:


# use the model to make predictions on a new value
lm.predict(X_new)


# In[106]:


# create a DataFrame with the minimum and maximum values of Temperature
X_new = pd.DataFrame({'Rain': [data_final.Rain.min(), data_final.Rain.max()]})
X_new.head()


# In[107]:


# make predictions for those x values and store them
preds = lm.predict(X_new)
preds


# In[108]:


# first, plot the observed data
data_final.plot(kind='scatter', x='Rain', y='Steam_Demand')

# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=3)


# In[110]:


import statsmodels.formula.api as smf
lm = smf.ols(formula='Steam_Demand ~ Rain', data=data_final).fit()
lm.conf_int()


# In[111]:


# print the p-values for the model coefficients
lm.pvalues


# In[43]:


# print the R-squared value for the model
lm.rsquared


# In[112]:


# create X and y
feature_cols = ['Wind']
X = data_final[feature_cols]
y = data_final.Steam_Demand

# follow the usual sklearn pattern: import, instantiate, fit
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

# print intercept and coefficients
print(lm.intercept_)
print(lm.coef_)


# In[113]:


# manually calculate the prediction
27261.06505821561 + 107.67733039*50


# In[114]:


# you have to create a DataFrame since the Statsmodels formula interface expects it
X_new = pd.DataFrame({'Wind': [50]})
X_new.head()


# In[115]:


# use the model to make predictions on a new value
lm.predict(X_new)


# In[116]:


# create a DataFrame with the minimum and maximum values of Temperature
X_new = pd.DataFrame({'Wind': [data_final.Wind.min(), data_final.Wind.max()]})
X_new.head()


# In[117]:


# make predictions for those x values and store them
preds = lm.predict(X_new)
preds


# In[118]:


# first, plot the observed data
data_final.plot(kind='scatter', x='Wind', y='Steam_Demand')

# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=2)


# In[120]:


import statsmodels.formula.api as smf
lm = smf.ols(formula='Steam_Demand ~ Wind', data=data_final).fit()
lm.conf_int()


# In[121]:


# print the p-values for the model coefficients
lm.pvalues


# In[122]:


# print the R-squared value for the model
lm.rsquared


# In[123]:


print ("asfa",10)


# In[124]:


# create X and y
feature_cols = ['Temperature', 'Humidity','Rain','Wind']
X = data_final[feature_cols]
y = data_final.Steam_Demand

lm = LinearRegression()
lm.fit(X, y)

# print intercept and coefficients
print("intercept : ",lm.intercept_)
print("coefficients : ",lm.coef_)


# In[126]:


#Stream_Demand = (Intercept) + (Temperature)*X1 + (Humidity)*X2 + (Rain)*X3 + (Wind)*X4
Steam_Demand = (29562.847075500533) + (Temperature coefficient)*X1 + (Humidity coefficient)*X2 + (Rain coefficient)*X3 + (Wind coefficient)*X4


# In[127]:


lm = smf.ols(formula='Steam_Demand ~ Temperature + Humidity ', data=data_final).fit()
lm.conf_int()
lm.summary()


# In[129]:


lm = smf.ols(formula='Steam_Demand ~ Temperature + Humidity ', data=data_final).fit()
lm.rsquared


# In[131]:


# create X and y
feature_cols = ['Temperature', 'Humidity','Rain','Wind']
X = data_final[feature_cols]
y = data_final.Steam_Demand

lm = LinearRegression()
lm.fit(X, y)

# print intercept and coefficients
print("intercept : ",lm.intercept_)
print("coefficients : ",lm.coef_)


# In[132]:


lm = smf.ols(formula='Steam_Demand ~ Temperature + Humidity+ Rain+Wind ', data=data_final).fit()
lm.rsquared


# In[133]:


lm = smf.ols(formula='Steam_Demand ~ Temperature + Humidity + Rain + Wind ', data=data_final).fit()
lm.conf_int()
lm.summary()


# In[134]:


lm = smf.ols(formula='Steam_Demand ~ Temperature + Humidity + Rain + Wind ', data=data_final).fit()
lm.rsquared


# In[135]:


29562.847075500533 + -3.97750965e+01*64.50 


# In[67]:


-3.05173578e+00*99.0+4.20839003e+03*0.0+1.14234164e+02*4.30


# In[68]:


26997.353351250535+189.08506297999998

