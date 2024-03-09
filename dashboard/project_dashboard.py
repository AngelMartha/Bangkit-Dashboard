import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
import streamlit as st

#create_PM10_tabel
def create_PM10_tabel(df):
    PM10_per_bulan = df[df['month'] == bulan]
    PM10_tabel = PM10_per_bulan[['PM10','day']].groupby(['day']).mean()
    return PM10_tabel

#create_TEMP_tabel
def create_TEMP_tabel(df):
    TEMP_per_bulan = df[df['month'] == bulan]
    TEMP_tabel = TEMP_per_bulan.groupby(by=['day']).agg({
        "TEMP":'mean'
    })
    return TEMP_tabel


#Membaca dataset
data = pd.read_csv('https://raw.githubusercontent.com/AngelMartha/Bangkit-Dashboard/main/dashboard/data_cleaning.csv')

#Membuat bagian pertama dashboard
st.title("Pemantauan Kualitas Udara⛅🌦️")
st.header("📍Lokasi : Stasiun Changping")
st.text('Halo, Selamat Datang di Pemantauan Kualitas Udara kami!🙌')
bulan = st.selectbox(
    label = 'Pilih Bulan',
    options = (1,2,3,4,5,6,7,8,9,10,11,12)
    )
st.write('Bulan yang anda pilih: ', bulan)

#membuat tabel informasi PM10 per hari
st.subheader('Jumlah Partikulat PM10')
st.text("Informasi tentang Rata-Rata Jumlah Partikulat PM10 per Hari dalam bulan tertentu")
col1, col2= st.columns(2)

with col1:
    st.table(create_PM10_tabel(data))

with col2:
    st.table(create_PM10_tabel(data).sort_values(by="PM10"))

#membuat chart informasi PM10 per hari
fig, ax = plt.subplots(figsize=(12, 6))
plt.style.use('ggplot')
ax.plot(
    create_PM10_tabel(data),
    marker='o', 
    linewidth=4,
    color="#40679E"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_title(("Rata-Rata Jumlah Partikulat PM10 per Hari pada Bulan " + str(bulan)))
ax.set_xlabel("Tanggal")
ax.set_ylabel("Partikulat PM10 (ug/m^3)")
ax.set_xlim(0,32)
ax.set_ylim(0,300)

st.pyplot(fig)
st.text("")

# Menambahkan kolom bulan dari kolom tanggal
data['bulan_tahun'] = pd.to_datetime(data['year'].astype(str) + '-' + data['month'].astype(str))
data['bulan'] = data['bulan_tahun'].dt.month

# Agregasi data per bulan
PM25_per_bulan = data.groupby('bulan')['PM10'].mean()

# Menampilkan diagram batang per bulan untuk PM10
st.subheader('Diagram Batang per Bulan untuk PM10')
plt.figure(figsize=(10, 6))
PM25_per_bulan.plot(kind='bar')
plt.xlabel('Bulan')
plt.xticks(rotation=45)
plt.ylabel('Rata-Rata PM10')
plt.title('Rata-Rata PM10 per Bulan')
st.pyplot(plt)


#membuat bagian informasi tabel Suhu per hari
st.subheader('Suhu')
st.text("Informasi tentang Rata-Rata Suhu per Hari pada Bulan")
col1, col2= st.columns(2)

with col1:
    st.table(create_TEMP_tabel(data))

with col2:
    st.table(create_TEMP_tabel(data).sort_values(by="TEMP"))

#membuat chart informasi temperature per month
fig, ax = plt.subplots(figsize=(12, 6))
plt.style.use('ggplot')
ax.plot(
    create_TEMP_tabel(data),
    marker='o', 
    linewidth=4,
    color="#5E1675"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_title(("Suhu per Hari di Bulan " + str(bulan)))
ax.set_xlabel("Tanggal")
ax.set_ylabel("Suhu (C)")
ax.set_ylim(-50,50)
st.pyplot(fig)

# Menambahkan kolom bulan dari kolom tanggal
data['bulan_tahun'] = pd.to_datetime(data['year'].astype(str) + '-' + data['month'].astype(str))
data['bulan'] = data['bulan_tahun'].dt.month

# Agregasi data per bulan
TEMP_per_bulan = data.groupby('bulan')['TEMP'].mean()

# Menampilkan diagram batang per bulan untuk suhu (C)
st.subheader('Diagram Batang per Bulan untuk Suhu (C)')
plt.figure(figsize=(10, 6))
TEMP_per_bulan.plot(kind='bar', color='orange')  # Ubah warna menjadi oranye
plt.xlabel('Bulan')
plt.ylabel('Rata-Rata Suhu (C)')
plt.title('Rata-Rata Suhu (C) per Bulan')

# Memutar label sumbu x sebesar 90 derajat
plt.xticks(rotation=45)

st.pyplot(plt)
