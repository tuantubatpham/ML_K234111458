import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import mutual_info_classif, chi2, SelectKBest, RFE
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Đọc dữ liệu từ file Excel
file_path = "Fashion Store Data Analysis.xlsx"  # Đổi tên file nếu cần
df = pd.read_excel(file_path, sheet_name="Fashion Store Data")

# Chọn các cột số và biến mục tiêu (giả sử 'Target' là biến phân loại)
columns_to_analyze = ["Age", "Qty", "Amount"]
target_variable = "Target"

# Mã hóa biến mục tiêu nếu là categorical
vif df[target_variable].dtype == 'object':
    le = LabelEncoder()
    df[target_variable] = le.fit_transform(df[target_variable])

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[columns_to_analyze] = scaler.fit_transform(df[columns_to_analyze])

# 1. Vẽ heatmap thể hiện mức độ tương quan
plt.figure(figsize=(8, 6))
sns.heatmap(df_scaled.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.show()

# 2. Mutual Information
mutual_info = mutual_info_classif(df_scaled[columns_to_analyze], df_scaled[target_variable])
mutual_info_series = pd.Series(mutual_info, index=columns_to_analyze)
print("Mutual Information Scores:")
print(mutual_info_series.sort_values(ascending=False))

# 3. Chi-square test (chỉ áp dụng cho dữ liệu dạng categorical)
chi2_selector = SelectKBest(chi2, k='all')
chi2_selector.fit(df_scaled[columns_to_analyze], df_scaled[target_variable])
chi2_scores = pd.Series(chi2_selector.scores_, index=columns_to_analyze)
print("Chi-Square Scores:")
print(chi2_scores.sort_values(ascending=False))

# 4. Recursive Feature Elimination (RFE)
x_train, x_test, y_train, y_test = train_test_split(df_scaled[columns_to_analyze], df_scaled[target_variable], test_size=0.2, random_state=42)
model = RandomForestClassifier()
rfe = RFE(model, n_features_to_select=2)
rfe.fit(x_train, y_train)
rfe_selected_features = [feature for feature, selected in zip(columns_to_analyze, rfe.support_) if selected]
print("Selected Features by RFE:", rfe_selected_features)
