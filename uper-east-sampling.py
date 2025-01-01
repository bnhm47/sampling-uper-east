import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew

file_path = '/Users/adelphia.ds/Desktop/Data Cafe Upper East 23 sept-1 nov 2024.xlsx'
df = pd.read_excel(file_path)

tanggal_col = 'Tanggal '  
pengunjung_col = 'Banyak Pengunjung '  

df[tanggal_col] = pd.to_datetime(df[tanggal_col])

print("Statistik Deskriptif:")
deskripsi = df[pengunjung_col].describe()
print(deskripsi)
mean = df[pengunjung_col].mean()
median = df[pengunjung_col].median()
mode = df[pengunjung_col].mode().iloc[0]
std_dev = df[pengunjung_col].std()
varian = df[pengunjung_col].var()
rentang = df[pengunjung_col].max() - df[pengunjung_col].min()
skewness = skew(df[pengunjung_col], bias=False)
kurtosis_val = kurtosis(df[pengunjung_col], bias=False)

print(f"\nMean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standar Deviasi: {std_dev}")
print(f"Variansi: {varian}")
print(f"Rentang (Range): {rentang}")
print(f"Skewness (Kemencengan): {skewness}")
print(f"Kurtosis (Keruncingan): {kurtosis_val}")

plt.figure(figsize=(8, 5))
sns.histplot(df[pengunjung_col], kde=True, bins=20, color='blue')
plt.title('Histogram Banyak Pengunjung')
plt.xlabel('Jumlah Pengunjung')
plt.ylabel('Frekuensi')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df[pengunjung_col], color='green')
plt.title('Boxplot Banyak Pengunjung')
plt.xlabel('Jumlah Pengunjung')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df[tanggal_col], y=df[pengunjung_col], color='purple')
plt.title('Scatter Plot Pengunjung per Tanggal')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Pengunjung')
plt.show()

print("\nDistribusi Data:")
if mean > median:
    print("Distribusi data cenderung menceng ke kanan (positif skewed).")
elif mean < median:
    print("Distribusi data cenderung menceng ke kiri (negatif skewed).")
else:
    print("Distribusi data simetris.")

df.set_index(tanggal_col, inplace=True)
df_weekly = df[pengunjung_col].resample('W').mean()

plt.figure(figsize=(12, 6))
plt.plot(df_weekly, marker='o', linestyle='-', color='red')
plt.title('Rata-rata Pengunjung Mingguan')
plt.xlabel('Minggu')
plt.ylabel('Rata-rata Pengunjung')
plt.grid(True)
plt.show()