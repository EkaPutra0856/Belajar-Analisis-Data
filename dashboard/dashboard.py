import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Konfigurasi dasar
sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load dataset utama (day.csv)
day_data = pd.read_csv('./data/day.csv')

# Mengubah kolom datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Sidebar untuk rentang tanggal
min_date = day_data['dteday'].min()
max_date = day_data['dteday'].max()

with st.sidebar:
    st.title("Bike Sharing Dashboard")

    # Filter rentang tanggal
    start_date, end_date = st.date_input(
        label="Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# Filter data sesuai dengan rentang tanggal
filtered_data = day_data[(day_data['dteday'] >= pd.to_datetime(start_date)) &
                         (day_data['dteday'] <= pd.to_datetime(end_date))]

# Bagian utama dashboard
st.header("Bike Sharing Dashboard 🚴‍♂️")

# 1. Penyewaan Harian
st.subheader("Daily Bike Rentals")

total_rentals = filtered_data['cnt'].sum()
st.markdown(f"Total Rentals: **{total_rentals}**")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_data['dteday'], filtered_data['cnt'], marker='o', color='#90CAF9')
ax.set_xlabel("Date")
ax.set_ylabel("Bike Rentals")
ax.set_title("Daily Bike Rentals Over Time")
st.pyplot(fig)

# 2. Cuaca dan Penyewaan
st.subheader("Impact of Weather on Bike Rentals")

# Plot hubungan antara cuaca dan jumlah penyewaan
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=filtered_data, palette='coolwarm', ax=ax)
ax.set_xlabel("Weather Situation (1 = Clear, 2 = Mist, 3 = Light Snow/Rain)")
ax.set_ylabel("Bike Rentals")
ax.set_title("Bike Rentals Based on Weather Conditions")
st.pyplot(fig)

# 3. Penyewaan Berdasarkan Musim
st.subheader("Rentals by Season")

# Mengubah season ke kategori dengan nama yang lebih deskriptif
filtered_data['season'] = filtered_data['season'].map({
    1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'
})

season_rentals = filtered_data.groupby('season')['cnt'].sum()

fig, ax = plt.subplots(figsize=(10, 6))
season_rentals.plot(kind='bar', color='#90CAF9', ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Total Bike Rentals")
ax.set_title("Total Bike Rentals by Season")
st.pyplot(fig)

# 4. Suhu dan Penyewaan
st.subheader("Effect of Temperature on Rentals")

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=filtered_data, ax=ax, color='#90CAF9')
ax.set_xlabel("Temperature (Normalized)")
ax.set_ylabel("Bike Rentals")
ax.set_title("Bike Rentals vs Temperature")
st.pyplot(fig)

# Footer
st.caption('Copyright (C) EKA PUTRA MERAVIGLIOSI 2024')
