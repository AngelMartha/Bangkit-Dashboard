import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

"""## Data Wrangling

### Gathering Data
"""

data = pd.read_csv("https://raw.githubusercontent.com/AngelMartha/Bangkit-Dashboard/main/Changping_Clean.csv")
data

"""### Assessing Data

### *Memeriksa* tipe data dari tiap kolom
"""

data.info()

"""Semua tipe data sudah sesuai

Checking duplicate data
"""

print("Jumlah duplikasi: ", data.duplicated().sum())

### Cleaning Data

"""Handling missing value"""

data.isna().count()

"""Fill missing value """
# Fill missing values with the constant values 
data_filled= data.fillna(0)

data_filled.isna().sum()

# Fill missing values with the mode of each column
data_filled['wd'].fillna(data_filled['wd'].mode()[0], inplace=True)


data.to_csv("data_cleaning.csv", index = False)