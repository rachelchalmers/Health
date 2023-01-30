#### Do the Local Authorities in the bottom HLE decile vary from year to year? ####

# Import Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Read in data (available on ONS website)
HLE_data = pd.read_csv("/Users/Rachel/Downloads/HLE_all.csv",encoding='latin-1', header=1)
print(HLE_data.head(5))
print(HLE_data.info())

# Select necessary columns
HLE_data = HLE_data[['Period', 'Country', 'Area type', 'Sex', 'Area code', 'Area name', 'Age group',
                     'Healthy life expectancy (HLE)']]

# Filter columns (England only, HLE at birth)
HLE_data = HLE_data.loc[HLE_data["Age group"] == '<1']
HLE_data = HLE_data.loc[HLE_data["Country"] == 'England']
HLE_data = HLE_data.loc[HLE_data["Area type"] == 'Local Areas']

# Create separate dataframes for male and female
HLE_male = HLE_data[HLE_data['Sex'] == 'Male']
HLE_female = HLE_data[HLE_data['Sex'] == 'Female']

# Sort for lowest HLE
HLE_male = HLE_male.sort_values(by = ['Healthy life expectancy (HLE)'])
HLE_female = HLE_female.sort_values(by = ['Healthy life expectancy (HLE)'])

# Iterate over dataframe, for each year add the first (lowest) 13 LA's to a new dataframe

dates = ['2011-13', '2012-14', '2013-15', '2014-16', '2015-17', '2016-18', '2017-19',
 '2018-20']

year = 0
HLE_male_low = pd.DataFrame()

for i in dates:
    HLE_male_date = HLE_male[HLE_male['Period'] == dates[year]]
    print(HLE_male_date.head())
    HLE_male_low = HLE_male_low.append(HLE_male_date[0:12])
    year +=1

print(HLE_male_low)

# repeat for female data

year = 0

HLE_female_low = pd.DataFrame()

for i in dates:
    HLE_female_date = HLE_female[HLE_female['Period'] == dates[year]]
    print(HLE_female_date.head())
    HLE_female_low = HLE_female_low.append(HLE_female_date[0:12])
    year +=1

print(HLE_female_low)

# find the number of unique places in each dataframe and how many times they appear in the bottom decile

print(HLE_male_low.nunique())   # 32 unique local authorities for male HLE
print(HLE_male_low['Area name'].unique())
HLE_male_count = HLE_male_low['Area name'].value_counts()
print(HLE_male_count)

HLE_male_count.plot(kind = 'bar', color = 'lightblue',
                    title = ('Lowest HLE decile areas from 2011-13 to 2018-20 (Male)'),
                    ylabel = 'Number of appearances in bottom decile')
plt.show()

# repeat for female data

print(HLE_female_low.nunique())   # 36 unique local authorities for female HLE
print(HLE_female_low['Area name'].unique())
HLE_female_count = HLE_female_low['Area name'].value_counts()
print(HLE_female_count)

HLE_female_count.plot(kind = 'bar', color = 'lightpink',
                      title = 'Lowest HLE decile areas from 2011-13 to 2018-20 (Female)',
                      ylabel = 'Number of appearances in bottom decile')
plt.show()

