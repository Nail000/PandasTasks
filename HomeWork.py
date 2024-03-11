import pandas as pd
import os 

### meger data  ###

df = pd.read_csv("C:\\Users\\HP\\MyGitHub\\PandasTasks\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\Sales_April_2019.csv")

files = [file for file in os.listdir("C:\\Users\\HP\\MyGitHub\\PandasTasks\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data")]

all_data = pd.DataFrame()


for file in files:
    df = pd.read_csv("C:\\Users\\HP\\MyGitHub\\PandasTasks\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\"+file)
    all_data = pd.concat([all_data,df])

all_data.to_csv("all_data.csv",index=False)


#### read the merged data from the new dataframe  ###

all_data = pd.read_csv("C:\\Users\\HP\\MyGitHub\\PandasTasks\\all_data.csv")

# print(all_data.head())


### cleaning the data  ###

nan_df = all_data[all_data.isna().any(axis=1)]
# print(nan_df.head())

all_data = all_data.dropna(how='all')
# print(all_data.head())

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])

all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

### Data Augmentation  ###
## Task2: Add month column ##

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] =all_data['Month'].astype('int32')
# print(all_data.head())

## Task3: Add sales column ##

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
# print(all_data.head())


#### Q1 ####

print(all_data.groupby('Month').sum())  #answer: december was the best month for sales with 4 613 443.34 $


