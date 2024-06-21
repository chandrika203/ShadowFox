#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


delhi_data=pd.read_csv(r"C:\Users\Chandrika\Desktop\shadowfox datascience\(task2)delhiaqi.csv")


# In[5]:


delhi_data.head()


# In[6]:


delhi_data.shape


# In[7]:


delhi_data.isnull().sum()


# In[8]:


delhi_data.describe()


# In[9]:


'''it performs two operations
1)This line converts the 'date' column in the DataFrame to a datetime object , and
2)it sets the 'date' column as the index of the DataFrame'''


delhi_data['date']=pd.to_datetime(delhi_data['date'])
delhi_data.set_index('date',inplace=True)


# In[10]:


delhi_data.info()


# In[11]:


cor_mat=delhi_data.corr()


# In[12]:


plt.figure(figsize=(10, 5))
sns.boxplot(data=delhi_data, orient='v')
plt.title('BOX PLOT (POLLUTANTS)')
plt.show()


# In[14]:


values = delhi_data[['co','no','no2','o3','so2','pm2_5','pm10','nh3']].sum(axis=0) #columns in dataset
pol = list(['co','no','no2','o3','so2','pm2_5','pm10','nh3'])
plt.figure(figsize =(10,5))
plt.pie(values, labels = pol)
plt.title('Distribution of pollutants (Pie chart)')
plt.show()


# In[15]:


#correlation matrix
plt.figure(figsize=(10, 5))
sns.heatmap(cor_mat, annot=True, cmap='coolwarm')
plt.title('Air Pollutants in Delhi(Heat map)')
plt.show()


# In[17]:


# Time series plots
fig, axs = plt.subplots(4, 2, figsize=(10, 15))
pols = delhi_data.columns
for i, pol in enumerate(pols):
    axs[i//2, i%2].plot(delhi_data.index, delhi_data[pol], label=pol)
    axs[i//2, i%2].set_title('pollutant')
    axs[i//2, i%2].set_xlabel('Date')
    axs[i//2, i%2].set_ylabel('Concentration')
    axs[i//2, i%2].legend()
plt.tight_layout()
plt.show()


# In[18]:


sns.pairplot(delhi_data)
plt.suptitle('Pair Plot', y=1.02)
plt.show()


# In[19]:


# AQI calculation for pm10
def cal_aqi(pm10):
    if pm10 <= 12:
        return pm10 * 50 / 12
    elif pm10 <= 35.4:
        return 50 + (pm10 - 12) * 50 / (35.4 - 12)
    elif pm10 <= 55.4:
        return 100 + (pm10 - 35.4) * 50 / (55.4 - 35.4)
    elif pm10 <= 150.4:
        return 150 + (pm10 - 55.4) * 100 / (150.4 - 55.4)
    elif pm10 <= 250.4:
        return 200 + (pm10 - 150.4) * 100 / (250.4 - 150.4)
    elif pm10 <= 350.4:
        return 300 + (pm10 - 250.4) * 100 / (350.4 - 250.4)
    elif pm10 <= 500.4:
        return 400 + (pm10 - 350.4) * 100 / (500.4 - 350.4)
    else:
        return 500

delhi_data['AQi_pm10'] = delhi_data['pm10'].apply(cal_aqi)

plt.figure(figsize=(10, 5))
plt.plot(delhi_data.index, delhi_data['AQi_pm10'], label='AQi_pm10')
plt.title('AQI Over Time based on the pm10')
plt.xlabel('Date')
plt.ylabel('AQI')
plt.legend()
plt.show()


# In[20]:


# now we convert the date column to datetime
if 'date' in delhi_data.columns:
    delhi_data['date'] = pd.to_datetime(delhi['date'])
    delhi_data.set_index('date', inplace=True)
else:
    print("The 'date' column is not found in the dataset.")

delhi_data.head()

if 'date' in delhi_data.columns:
    features = delhi_data.drop(columns=['date'])
else:
    features = delhi_data

features.hist(bins=24, figsize=(14,8), edgecolor='black')
plt.suptitle('Histograms of Air Quality Parameters', y=1.02)
plt.tight_layout()

sns.set_palette('Set2')
plt.show()

daily_data = delhi_data.resample('D').mean()
print(daily_data.shape)


# In[27]:


from statsmodels.tsa.seasonal import seasonal_decompose
decomp = seasonal_decompose(daily_data['pm10'], model='additive', period=7)
trend = decomp.trend
seasonal = decomp.seasonal
residual = decomp.resid

# Plot the decomposed components
plt.figure(figsize=(10, 6))
plt.subplot(411)
plt.plot(daily_data['pm10'], label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonal')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residual')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Apply a 7-day rolling mean to smooth out the data (adjust as needed)
rolling_mean = daily_data['pm10'].rolling(window=7).mean()

# Plot the original data and the rolling mean
plt.figure(figsize=(15, 5))
plt.plot(daily_data['pm10'], label='Daily pm10')
plt.plot(rolling_mean, label='7-Day Rolling Mean', color='green')
plt.title('pm10 Trend with 7-Day Rolling Mean')
plt.xlabel('Date')
plt.ylabel('pm10 Concentration')
plt.legend()
plt.show()


# In[28]:


def stl_decomp(delhi_data):
    decomp = seasonal_decompose(delhi_data, model='additive', period=7)
    trend = decomp.trend
    seasonal = decomp.seasonal
    residual = decomp.resid

    plt.figure(figsize=(12, 8))
    plt.subplot(411)
    plt.plot(delhi_data, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonal')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residual')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()


# In[34]:


def apply_mean(delhi_data, window):
    rolling_mean = delhi_data.rolling(window=window).mean()
    return rolling_mean

def cal_aqi(row):
    return cal_aqi

def aqi_analysis(delhi_data):
    return aqi_analysis

def day_nig_aqi_compar(delhi_data):
    return day_nig_aqi_compar

def check_convert_date_col(delhi_data):
    if 'date' in delhi_data.columns:
        delhi_data['date'] = pd.to_datetime(delhi_data['date'])
        delhi_data.set_index('date', inplace=True)
    else:
        print("The 'date' column is not found")

def extract_hour_date(delhi_data):
    if 'date' in delhi_data.columns:
        delhi_data['hour'] = delhi_data['date'].dt.hour
    else:
        print("The 'date' column is not found")

def check_convert_date_col(delhi_data):
    return check_convert_date_col

def extract_hr_date(delhi_data):
    return extract_hr_date
def cal_aqi_and_plot(delhi_data):
       return cal_aqi_and_plot

def cal_avg_aqi_day_nig(delhi_data):
      return cal_avg_aqi_day_nig

def day_vs_night_aqi_compar(delhi_data):
      return day_vs_night_aqi_compar


# In[35]:


stl_decomp(delhi_data['pm10'])

delhi_data['rolling_mean_pm10'] = apply_mean(delhi_data['pm10'], window=7)

delhi_data['AQI'] = delhi_data.apply(cal_aqi, axis=1)

aqi_analysis(delhi_data)
day_nig_aqi_compar(delhi_data)
check_convert_date_col(delhi_data)
extract_hr_date(delhi_data)
cal_aqi_and_plot(delhi_data)
cal_avg_aqi_day_nig(delhi_data)
day_vs_night_aqi_compar(delhi_data)


# #  Conclusion
# 
# The analysis of Delhi's air quality highlights several important points and suggests strategies to improve the situation
# 
# 1. **Air Quality Levels**:
#    - Delhi mostly experiences "Very Poor" and "Severe" air quality, which happens 97.33% of the time.
#    - Only 2.67% of the time does the city have "Good" or "Satisfactory" air quality.
# 
# 2. **Hourly Trends**:
#    - AQI levels are slightly higher at night compared to the daytime.
#    - The daily AQI extremes range from a high of 421.63 to a low of 330.37.
# 
# 3. **Pollutant Correlations**:
#    - Some pollutants show strong correlations, indicating they might come from the same sources or spread in similar ways. This suggests that addressing one pollutant may help reduce others as well.
# 
# ### Strategies to Improve Air Quality
# 
# 1. **Reduce Carbon Monoxide (CO) Levels**:
#    - Enforce strict vehicle emission standards.
#    - Promote cleaner fuels like CNG and electric vehicles.
#    - Improve traffic management to reduce congestion and idling.
#    - Implement strict emissions regulations for industries.
#    - Integrate urban planning that prioritizes mixed land-use and green spaces.
# 
# 2. **Overall Air Quality Improvement**:
#    - Promote renewable energy sources.
#    - Adopt green building standards.
#    - Enhance waste management practices.
#    - Expand afforestation and urban greening initiatives.
#    - Foster public awareness and education on air quality.
#    - Encourage collaboration across different sectors to develop and implement comprehensive air quality management plans.
# 
# By taking these steps together, Delhi can significantly improve its air quality, protect public health, and create a more sustainable environment for everyone.
