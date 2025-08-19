import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Importing the required libraries

# Providing the url which acts as the source
url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"

# Read the file
df = pd.read_csv(url, skiprows=8)

# Previewing the data to make sure and examining the source
print(df.head())

# Cleaning and preprocessing the data
def cleaning_nasa_data(data):
    # Making a copy to avoid any complications with the original dataset
    df_clean = data.copy()
    # Replacing all the missing value indicators with nan
    df_clean = df_clean.replace('****', np.nan)
    # Converting the columns into appropriate data types
    # Converting the column year into an integer
    df_clean.iloc[:, 0] = pd.to_numeric(df_clean.iloc[:, 0], errors = 'coerce')
    # Monthly and annual columns into float 
    for col in df_clean.columns[1:]:
        df_clean[col] = pd.to_numeric(df_clean[col], errors = 'coerce')
    df_clean = df_clean.dropna(how = 'all')

     # Rename columns for clarity
    new_names = {
        df_clean.columns[0]: 'Year',
        df_clean.columns[1]: 'Jan', 
        df_clean.columns[2]: 'Feb',
        df_clean.columns[3]: 'Mar',
        df_clean.columns[4]: 'Apr',
        df_clean.columns[5]: 'May',
        df_clean.columns[6]: 'Jun',
        df_clean.columns[7]: 'Jul',
        df_clean.columns[8]: 'Aug',
        df_clean.columns[9]: 'Sep',
        df_clean.columns[10]: 'Oct',
        df_clean.columns[11]: 'Nov',
        df_clean.columns[12]: 'Dec',
        df_clean.columns[13]: 'J-D',  # Annual average
        df_clean.columns[14]: 'D-N',  # Dec-Nov average
        df_clean.columns[15]: 'DJF',  # Winter average
        df_clean.columns[16]: 'MAM',  # Spring average
        df_clean.columns[17]: 'JJA',  # Summer average
        df_clean.columns[18]: 'SON'   # Fall average
    }
    df_clean = df_clean.rename(columns=new_names)
    
    return df_clean

# Finally cleaning 
clean_df = cleaning_nasa_data(df)

# Calculate 5-year moving average for annual data
clean_df['5yr_Moving_Avg'] = clean_df['J-D'].rolling(window=5, center=True).mean()

