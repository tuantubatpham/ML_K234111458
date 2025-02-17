import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

"""Dữ liệu có 21 cột, trong đó các cột số phù hợp để chuẩn hóa là:

Age (Tuổi)
Qty (Số lượng)
Amount (Số tiền)
ship-postal-code (Mã bưu chính)"""


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

# Lưu kết quả vào file Excel mới
output_file = "Fashion_Store_Data_Normalized.xlsx"
df_scaled.to_excel(output_file, index=False)

print(f"Dữ liệu đã được chuẩn hóa và lưu vào: {output_file}")
