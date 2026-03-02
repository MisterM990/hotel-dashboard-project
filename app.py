import pandas as pd
import streamlit as st

df = pd.read_excel("hotel_data.xlsx")
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
# Create a display version (clean dates, no time)
df_display = df.copy()
df_display["date"] = df_display["date"].dt.date

st.set_page_config(layout="wide")

st.title("🏨 Hotel Performance Dashboard")
st.markdown("Monitor revenue, bookings, and occupancy performance")

st.sidebar.header("Filters")

filter_type = st.sidebar.radio("Filter Type", ["Single Day", "Date Range"])

if filter_type == "Single Day":
    selected_date = st.date_input("Select a date")
    selected_date = pd.to_datetime(selected_date)
    df = df[df["date"] == selected_date]

else:
    selected_range = st.date_input("Select date range", [])
    
    if len(selected_range) == 2:
        start_date = pd.to_datetime(selected_range[0])
        end_date = pd.to_datetime(selected_range[1])

        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
# KPIs
total_revenue = df["total_revenue_ht"].sum()
total_bookings = df["sold_rooms"].sum()
avg_price = df["avg_price"].mean()
occupancy = df["occupancy_rate"].mean()

# Display KPIs
st.markdown("## 📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"£{total_revenue:,.0f}")
col2.metric("🛏️ Bookings", int(total_bookings))
col3.metric("📈 Avg Price", f"£{avg_price:.2f}")
col4.metric("🏨 Occupancy Rate", f"{occupancy:.2f}%")

st.markdown("## 📈 Performance Over Time")

col1, col2 = st.columns(2)

# Revenue chart
revenue_by_date = df.groupby("date")["total_revenue_ht"].sum().sort_index()
col1.line_chart(revenue_by_date)

# Bookings chart
bookings_by_date = df.groupby("date")["sold_rooms"].sum().sort_index()
col2.line_chart(bookings_by_date)

st.subheader("Raw Data Preview")
st.write(df_display.head())

st.markdown("## 🧠 Insights")

st.write("• Revenue increases during high occupancy periods.")
st.write("• Weekends tend to generate more bookings.")
st.write("• Suggest optimizing pricing during peak demand.")