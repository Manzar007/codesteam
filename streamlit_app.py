import streamlit as st
import pandas as pd
import numpy as np

# Function to load datasets from CSV files
@st.cache_data
def load_csv_data(file_path):
    return pd.read_csv(file_path)

# Load the datasets
data1 = load_csv_data("Data1.csv")
data2 = load_csv_data("Data2.csv")
data3a = load_csv_data("Data3a.csv")

# Sidebar for date range selection
st.sidebar.header("Date Range Selector")

# Get minimum and maximum dates from data
data3a["Date"] = pd.to_datetime(data3a["Date"], format="%d-%m-%Y")
start_date = data3a["Date"].min()
end_date = data3a["Date"].max()

# Date range input for filtering
selected_dates = st.sidebar.date_input(
    "Select Date Range",
    [start_date, end_date],
    min_value=start_date,
    max_value=end_date,
)

# Filter data based on selected date range
filtered_data1 = data1[
    (pd.to_datetime(data1["date"]) >= selected_dates[0])
    & (pd.to_datetime(data1["date"]) <= selected_dates[1])
]
filtered_data2 = data2[
    (pd.to_datetime(data2["timepoint"]) >= selected_dates[0])
    & (pd.to_datetime(data2["timepoint"]) <= selected_dates[1])
]
filtered_data3a = data3a[
    (data3a["Date"] >= selected_dates[0]) & (data3a["Date"] <= selected_dates[1])
]

# Display dataframes
st.header("Filtered Data")
st.write("Data1 (Arrivals and Departures)")
st.dataframe(filtered_data1)

st.write("Data2 (Weather Conditions)")
st.dataframe(filtered_data2)

st.write("Data3a (Flight Delays and Cancellations)")
st.dataframe(filtered_data3a)

# Line chart for arrivals and departures
st.header("Arrivals and Departures Over Time")
st.line_chart(filtered_data1[["date", "arrivals", "departures"]].set_index("date"))

# Display additional insights and explanations
st.header("Conclusions and Insights")
st.write("Based on the filtered data, here are some insights and conclusions:")
st.write("1. The number of arrivals and departures varies over time. Use the date range to explore different periods.")
st.write("2. Weather conditions might influence flight delays and cancellations. Compare Data2 and Data3a to find connections.")
st.write("3. Certain airlines might have more delays or cancellations for specific reasons.")

# Add answers to the provided questions
st.header("Additional Information")
st.write("Q1: What are the strengths of the data modeling format?")
st.write("The strengths include flexibility, simplicity, and modularity, allowing easy expansion and integration with other data sources.")

st.write("Q2: What are the weaknesses of the data modeling format?")
st.write("Weaknesses may involve limited advanced querying and sorting capabilities, requiring additional code or workarounds to accomplish complex operations.")

st.write("Q3: How do you store your data on disk?")
st.write("The data is stored in CSV files. This format is simple and accessible but might not be as efficient for large-scale data or complex querying.")

st.write("Q4: How would you extend the model with new data sources?")
st.write("To extend the model, you'd create new data structures or tables and establish relationships with existing data. This extension might require updating the user interface to accommodate new elements.")

st.write("Q5: How would you add new attributes to the data?")
st.write("To add new attributes, you'd typically use additional data sources, APIs, or computations. The new data can be integrated into the existing structure by adding columns or creating new tables.")
