# Hotel Performance Dashboard

## Problem
Hotels need insights into occupancy, revenue, and bookings to optimize operations.  
This dashboard provides KPIs and visual trends.

## Tools
- Python
- pandas
- Streamlit
- Excel

## Features
- Key metrics: Revenue, Bookings, Avg Price, Occupancy Rate
- Charts: Revenue & Bookings over time
- Filters: Single day or date range selection
- Insights and recommendations

## Dataset
- Fake dataset inspired by real hotel KPIs (RevPAR, ADR, Occupancy Rate)
- Columns: date, available_rooms, sold_rooms, occupancy_rate, total_revenue_ht, avg_price

## Screenshots
![Dashboard Overview](screenshots/dashboard_overview.png)

## How to Run
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

N.B: the data contains a range of date from 01/02/2025 to 31/03/2025 so if you go beyond that it will show nothing.
