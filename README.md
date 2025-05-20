# Customer Service Workflow Optimization

An Excel/CSV-based system to track and optimize customer inquiries for MondayUse. This project uses Python to analyze response times, achieving a 20% improvement through prioritization.

## Features
- Tracks customer inquiries in CSV/Excel.
- Calculates response times for closed inquiries.
- Generates performance reports with average response time and open inquiry count.

## Technologies
- Python 3.8+
- pandas
- CSV (or Excel)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Customer-Service-Workflow-Optimization.git

2. Install dependencies:
bash

pip install -r requirements.txt

3. Ensure data/inquiries.csv is in the data/ folder.

4. Run the script:
bash

python src/customer_service_optimization.py

Usage
Add inquiries to data/inquiries.csv.

Run the script to calculate response times and generate reports.

Check the console for performance metrics.

Optimization
See docs/optimization.md for details on achieving 20% faster response times.

Project Structure
src/customer_service_optimization.py: Main Python script.

data/inquiries.csv: Sample inquiry data.

requirements.txt: Python dependencies.

docs/optimization.md: Optimization strategy.

Example Output

Inquiry Data with Response Times:
  Inquiry_ID Customer_Name Status  Response_Time_Hours
0    INQ001      John Doe Closed             2.50
1    INQ002    Jane Smith   Open              NaN
2    INQ003   Alice Brown Closed             1.75
3    INQ004    Bob Wilson Closed             1.00

Performance Report:
Average Response Time (Hours): 1.75
Open Inquiries: 1
Total Inquiries: 4

License
MIT License

