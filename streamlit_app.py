pip install matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Streamlit Example App")

# Create some sample data
@st.cache_data
def create_data(size):
    np.random.seed(42)
    x = np.linspace(0, 10, size)
    y = np.sin(x) + np.random.normal(0, 0.1, size)
    return pd.DataFrame({'x': x, 'y': y})

# Create a slider to control the size of the dataset
data_size = st.slider("Select Data Size", min_value=50, max_value=500, value=100, step=50)

# Create the dataset
data = create_data(data_size)

# Display a line chart
st.line_chart(data, x='x', y='y')

# Display a simple text box for user input
user_text = st.text_input("Enter some text:")
if user_text:
    st.write(f"You entered: {user_text}")

# Display a checkbox to toggle additional information
if st.checkbox("Show Summary Statistics"):
    st.write("Summary statistics:")
    st.write(data.describe())

# Add a custom Matplotlib plot
st.subheader("Custom Plot with Matplotlib")
fig, ax = plt.subplots()
ax.scatter(data['x'], data['y'])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Scatter Plot of Data")
st.pyplot(fig)
