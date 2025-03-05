import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Đọc dữ liệu từ file Excel
file_path = "Fashion Store Data Analysis.xlsx"  # Đổi tên file nếu cần
df = pd.read_excel(file_path, sheet_name="Fashion Store Data")

# Chọn các cột số để chuẩn hóa
columns_to_scale = ["Age", "Qty", "Amount"]


def normalize_data(df, columns):
    df_scaled = df.copy()

    # Min-Max Scaling
    minmax_scaler = MinMaxScaler()
    df_scaled[[col + "_minmax" for col in columns]] = minmax_scaler.fit_transform(df[columns])

    # StandardScaler (Z-score normalization)
    standard_scaler = StandardScaler()
    df_scaled[[col + "_zscore" for col in columns]] = standard_scaler.fit_transform(df[columns])

    return df_scaled


# Áp dụng chuẩn hóa
df_scaled = normalize_data(df, columns_to_scale)

# Vẽ biểu đồ phân bố cho các phương pháp chuẩn hóa
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

for i, col in enumerate(columns_to_scale):
    sns.histplot(df_scaled[col + "_minmax"], bins=30, kde=True, ax=axes[0, i], color="blue")
    axes[0, i].set_title(f"Min-Max Scaling: {col}")

    sns.histplot(df_scaled[col + "_zscore"], bins=30, kde=True, ax=axes[1, i], color="red")
    axes[1, i].set_title(f"StandardScaler: {col}")

plt.tight_layout()
plt.show()

# Lưu kết quả vào file Excel mới
output_file = "Fashion_Store_Data_Normalized.xlsx"
df_scaled.to_excel(output_file, index=False)

print(f"Dữ liệu đã được chuẩn hóa và lưu vào: {output_file}")
