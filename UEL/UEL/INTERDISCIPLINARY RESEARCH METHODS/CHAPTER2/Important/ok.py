import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file Excel
file_path = "Fashion Store Data Analysis.xlsx"  # Đổi tên file nếu cần
df = pd.read_excel(file_path, sheet_name="Fashion Store Data")
# Kiểm tra dữ liệu
print(df.info())

# Thiết lập kiểu hiển thị cho biểu đồ
sns.set_style("whitegrid")

# Vẽ biểu đồ phân bố cho các biến quan trọng
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Kiểm tra nếu cột tồn tại trước khi vẽ biểu đồ
if "Age" in df.columns:
    sns.histplot(df["Age"], bins=30, kde=True, ax=axes[0], color="blue")
    axes[0].set_title("Distribution of Age")

if "Qty" in df.columns:
    sns.histplot(df["Qty"], bins=20, kde=True, ax=axes[1], color="green")
    axes[1].set_title("Distribution of Qty")

if "Amount" in df.columns:
    sns.histplot(df["Amount"], bins=30, kde=True, ax=axes[2], color="red")
    axes[2].set_title("Distribution of Amount")

plt.tight_layout()
plt.show()