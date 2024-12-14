import streamlit as st
import plotly.express as px
import pandas as pd

# Set up CSS for white background and left-aligned content
st.markdown("""
   <style>
       /* Set the body background to white and text color */
       body {
           font-family: 'Roboto', sans-serif;
           background-color: #ffffff;  /* Set the background color to white */
           color: #1e1e1e;  /* Dark text for readability */
           margin: 0;
           padding: 0;
           display: flex;
           flex-direction: column;
           align-items: flex-start;  /* Align content to the left */
       }

       /* Remove any centering from main content container */
       .main {
           padding: 20px;
           width: 100%;
       }

       /* Adjust Button and Input fields to be left-aligned */
       .stButton>button {
           background-color: #0078d4;
           color: white;
           text-align: left;
       }

       .stTextInput>div>input {
           background-color: #ffffff;
           border: 1px solid #dcdcdc;
           text-align: left;
       }

       .stSelectbox>div>div {
           background-color: #ffffff;
           text-align: left;
       }

       /* Left-align the headers and titles */
       .stHeader, .stTitle {
           font-weight: 500;
           color: #0078d4;
           text-align: left;
       }

       /* Ensure all markdown text aligns to the left */
       .stMarkdown {
           text-align: left;
       }

       /* Left-align the Metrics cards */
       .stMetric {
           text-align: left;
       }

       /* Left-align radio buttons, select boxes, etc. */
       .stRadio, .stCheckbox, .stSelectbox {
           text-align: left;
       }

       /* Footer aligned left */
       footer {
           text-align: left;
           padding-left: 20px;
           padding-top: 20px;
       }
   </style>
""", unsafe_allow_html=True)

# Sample Data for Visualization
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 15, 7, 22]
})

# App Header and Logo
st.title("Power BI-Inspired Dashboard")
# st.image("path/to/your/logo.png", width=200)

# Main Layout (Using Columns)
col1, col2 = st.columns([3, 1])

# Column 1: Overview
with col1:
    st.header("Overview")
    st.write("This dashboard provides key metrics and performance indicators. "
             "Use the filters to interact with the data.")

    # Interactive Visualization (Bar chart using Plotly)
    st.header("Category Value Comparison")
    fig = px.bar(df, x='Category', y='Value', title="Category Value Comparison")
    st.plotly_chart(fig)

# Column 2: Filters and Controls
with col2:
    st.header("Filters")
    # Dropdown for category selection
    selected_category = st.selectbox("Select Category", df['Category'])

    # Display filtered data based on selection
    st.write(f"Displaying data for category: {selected_category}")
    filtered_data = df[df['Category'] == selected_category]
    st.write(filtered_data)

# Additional Section: KPI Cards (Example for Key Metrics)
st.header("Key Performance Indicators")
col3, col4 = st.columns([2, 2])

with col3:
    st.subheader("Total Value")
    total_value = df['Value'].sum()
    st.metric(label="Total", value=f"${total_value}")

with col4:
    st.subheader("Average Value")
    avg_value = df['Value'].mean()
    st.metric(label="Average", value=f"${avg_value:.2f}")

# Expandable Section for More Details
with st.expander("Show More Details"):
    st.write("""
        You can place additional metrics, trends, or detailed analysis here. 
        This section can include things like time series charts, 
        regional breakdowns, or predictive analytics.
    """)

# Additional Chart Example: Line Chart (with interactive range)
st.header("Trends Over Time")
# Sample time series data
date_range = pd.date_range(start="2021-01-01", periods=12, freq='M')
data = pd.DataFrame({
    'Date': date_range,
    'Sales': [100, 200, 150, 300, 400, 350, 500, 600, 550, 700, 750, 800]
})
fig2 = px.line(data, x='Date', y='Sales', title="Monthly Sales Trend")
st.plotly_chart(fig2)

# Custom Footer Section (Optional)
st.markdown("""
   <footer>
       <p>© 2024 Power BI-Inspired Streamlit Dashboard</p>
   </footer>
""", unsafe_allow_html=True)
