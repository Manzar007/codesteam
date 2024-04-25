import streamlit as st
import pandas as pd
import numpy as np

# Function to load and preprocess datasets from CSV files
@st.cache_data
def load_csv_data(file_path, date_column):
    df = pd.read_csv(file_path)
    # Convert specified column to datetime
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")
    return df

# Load the datasets
data1 = load_csv_data("Data1.csv", "date")
data2 = load_csv_data("Data2.csv", "timepoint")
data3a = load_csv_data("Data3a.csv", "Date")

# Sidebar for date range selection
st.sidebar.header("Date Range Selector")

# Get minimum and maximum dates from Data3a
start_date = data3a["Date"].min()
end_date = data3a["Date"].max()

# Date range input for filtering
selected_dates = st.sidebar.date_input(
    "Select Date Range",
    [start_date, end_date],
    min_value=start_date,
    max_value=end_date,
)

# Validate the selected_dates input
if len(selected_dates) == 2:
    # Convert selected dates to datetime
    start_date = pd.Timestamp(selected_dates[0])
    end_date = pd.Timestamp(selected_dates[1])

    # Filter data based on selected date range
    filtered_data1 = data1[
        (data1["date"] >= start_date) & (data1["date"] <= end_date)
    ]
    filtered_data2 = data2[
        (data2["timepoint"] >= start_date) & (data2["timepoint"] <= end_date)
    ]
    filtered_data3a = data3a[
        (data3a["Date"] >= start_date) & (data3a["Date"] <= end_date)
    ]
else:
    st.warning("Please select a valid date range.")

# Line chart for arrivals and departures
st.header("Arrivals and Departures Over Time")
if not filtered_data1.empty:
    st.line_chart(
        filtered_data1[["date", "arrivals", "departures"]].set_index("date")
    )
else:
    st.warning("No data available for the selected date range.")

# Bar chart for weather conditions
st.header("Weather Conditions Over Time")
if not filtered_data2.empty:
    st.bar_chart(filtered_data2[["timepoint", "temp2m"]].set_index("timepoint"))
else:
    st.warning("No weather data available for the selected date range.")

# New Graph: Histogram for Numerical Variable
st.header("Histogram for Numerical Variable in Data3a")
if 'SomeNumericColumn' in filtered_data3a.columns:
    st.histogram(
        filtered_data3a['SomeNumericColumn'],
        bins=10,
        title='Histogram for SomeNumericColumn'
    )
else:
    st.warning("No numerical data for histogram.")

# New Graph: Pie Chart for Categorical Data
st.header("Pie Chart for Categorical Data in Data3a")
if 'SomeCategoryColumn' in filtered_data3a.columns:
    category_counts = filtered_data3a['SomeCategoryColumn'].value_counts()
    st.pie_chart(category_counts, title='Distribution of SomeCategoryColumn')
else:
    st.warning("No data for pie chart.")

# New Graph: Area Chart for Time-Series Data
st.header("Area Chart for Time-Series Data in Data3a")
if 'CumulativeDataColumn' in filtered_data3a.columns:
    cumulative_data = filtered_data3a[["Date", "CumulativeDataColumn"]].set_index("Date")
    st.area_chart(cumulative_data, title='Area Chart for Cumulative Data')
else:
    st.warning("No data for area chart.")

# Additional insights and conclusions
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
