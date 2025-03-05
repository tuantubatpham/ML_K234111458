import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset with proper header detection
df = pd.read_excel("Fashion_Store_Data_Normalized.xlsx", header=0)

# Clean column names
df.columns = df.columns.str.strip()

# Display descriptive statistics
print("Descriptive Statistics:\n", df.describe())

# Set style for seaborn
sns.set_style("whitegrid")

# Check if necessary columns exist
required_columns = {'Age', 'Quantity', 'Amount'}
if not required_columns.issubset(df.columns):
    print("Error: Missing required columns in dataset:", required_columns - set(df.columns))
else:
    # Plot Histogram & KDE for Age, Quantity, Amount
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for ax, col in zip(axes, ['Age', 'Quantity', 'Amount']):
        sns.histplot(df[col].dropna(), kde=True, bins=30, ax=ax)
        ax.set_title(f'Distribution of {col}')

    plt.tight_layout()
    plt.show()

    # Bivariate Analysis - Box Plot & Scatter Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Box Plot for Amount by Quantity
    sns.boxplot(x=df['Quantity'], y=df['Amount'], ax=axes[0])
    axes[0].set_title("Box Plot: Amount by Quantity")

    # Scatter Plot for Amount vs Quantity
    sns.scatterplot(x=df['Quantity'], y=df['Amount'], alpha=0.5, ax=axes[1])
    axes[1].set_title("Scatter Plot: Amount vs Quantity")

    plt.tight_layout()
    plt.show()