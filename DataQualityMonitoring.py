import pandas as pd

# Sample data for monitoring
data = {
    'ID': [1, 2, 3, 4],
    'Portfolio_Value': [100000, 200000, None, 150000],
    'Risk_Level': ['Low', 'Medium', 'High', None]
}

df_data = pd.DataFrame(data)

def check_data_quality(df):
    """
    Check for missing values and report data quality issues.
    """
    print("Checking Data Quality...")

    # Check for missing values
    missing_values = df.isnull().sum()
    
    # Report missing values
    print("Data Quality Report:")
    for col, missing in missing_values.items():
        if missing > 0:
            print(f"Column {col} has {missing} missing value(s)")
        else:
            print(f"Column {col} is complete")

# Run the data quality monitoring
check_data_quality(df_data)
