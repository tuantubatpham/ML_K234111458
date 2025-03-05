import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file Excel
file_path = "Fashion Store Data Analysis.xlsx"  # Đổi tên file nếu cần
df = pd.read_excel(file_path, sheet_name="Fashion Store Data")

# Chọn các cột số để phân tích tương quan
columns_to_analyze = ["Age", "Qty", "Amount"]

# 1. Vẽ heatmap thể hiện ma trận tương quan
plt.figure(figsize=(8, 6))
sns.heatmap(df[columns_to_analyze].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# 2. Loại bỏ các biến có tương quan cao để tránh multicollinearity
correlation_matrix = df[columns_to_analyze].corr()
high_corr_vars = set()
thresh = 0.8  # Ngưỡng tương quan cao

for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > thresh:
            colname = correlation_matrix.columns[i]
            high_corr_vars.add(colname)

df_reduced = df.drop(columns=high_corr_vars)


print(f"Các biến bị loại bỏ do tương quan cao: {high_corr_vars}")
