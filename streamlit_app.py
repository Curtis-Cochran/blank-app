import streamlit as st
import pandas as pd

# App Title
st.title("Simple CSV Aggregator")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Display the first few rows
    st.subheader("📌 Raw Data Preview")
    st.write(df.head())

    # Select column for aggregation
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    if not categorical_cols.empty and not numeric_cols.empty:
        group_col = st.selectbox("Select a column to group by", categorical_cols)
        agg_col = st.selectbox("Select a numeric column to sum", numeric_cols)

        # Perform Aggregation
        aggregated_df = df.groupby(group_col)[agg_col].sum().reset_index()

        # Display Aggregated Data
        st.subheader("📈 Aggregated Data")
        st.write(aggregated_df)
    else:
        st.warning("CSV must have at least one categorical and one numeric column."
)
