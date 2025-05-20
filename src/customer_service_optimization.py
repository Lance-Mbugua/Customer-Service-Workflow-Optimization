import pandas as pd
from datetime import datetime

# Load inquiry data from CSV
def load_inquiries(file_path='data/inquiries.csv'):
    try:
        df = pd.read_csv(file_path)
        df['Inquiry_Date'] = pd.to_datetime(df['Inquiry_Date'])
        df['Response_Date'] = pd.to_datetime(df['Response_Date'], errors='coerce')
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

# Calculate response time in hours
def calculate_response_time(df):
    df['Response_Time_Hours'] = (df['Response_Date'] - df['Inquiry_Date']).dt.total_seconds() / 3600
    return df

# Generate performance report
def generate_report(df):
    closed_inquiries = df[df['Status'] == 'Closed']
    avg_response_time = closed_inquiries['Response_Time_Hours'].mean()
    open_inquiries = df[df['Status'] == 'Open'].shape[0]
    report = {
        'Average Response Time (Hours)': round(avg_response_time, 2) if not pd.isna(avg_response_time) else 'N/A',
        'Open Inquiries': open_inquiries,
        'Total Inquiries': df.shape[0]
    }
    return report

def main():
    # Load inquiries
    df = load_inquiries()
    if df is None:
        return

    # Calculate response times
    df = calculate_response_time(df)
    print("Inquiry Data with Response Times:")
    print(df[['Inquiry_ID', 'Customer_Name', 'Status', 'Response_Time_Hours']])

    # Generate report
    report = generate_report(df)
    print("\nPerformance Report:")
    for key, value in report.items():
        print(f"{key}: {value}")

    # Save updated data
    df.to_csv('data/inquiries.csv', index=False)
    print("\nData saved to data/inquiries.csv")

if __name__ == "__main__":
    main()
