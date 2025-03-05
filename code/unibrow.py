'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal Data Browser")

uploaded_file = st.file_uploader("Upload a dataset", type=["csv", "xlsx", "json"])

if uploaded_file:
    file_extension = pl.get_file_extension(uploaded_file.name)

    df = pl.load_file(uploaded_file, file_extension)

    selected_columns = st.multiselect("Select columns to display:", df.columns.tolist(), default=df.columns.tolist())

    apply_filter = st.checkbox("Apply Filter")

    if apply_filter:
        object_columns = pl.get_columns_of_type(df, "object")
        
        if object_columns:
            selected_column = st.selectbox("Select a column to filter by:", object_columns)

            unique_values = pl.get_unique_values(df, selected_column)
            selected_value = st.selectbox(f"Select a value from '{selected_column}':", unique_values)

            df = df[df[selected_column] == selected_value]

    st.subheader("Filtered Data")
    st.dataframe(df[selected_columns])

    st.subheader("Dataset Description")
    st.write(df[selected_columns].describe())


# TODO Write code here to complete the unibrow.py

