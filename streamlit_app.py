
import streamlit as st

st.set_page_config(page_title="Synthetic Data Generator", layout="wide")

st.title("Synthetic Data Generator")
st.caption("Enterprise Synthetic Data Generation Platform for Snowflake")

db = st.text_input("Database", placeholder="e.g., EDW")
schema = st.text_input("Schema", placeholder="e.g., SALES")

mode = st.radio(
    "Generation Mode",
    [
        "Generate via Wrapper (Recommended)",
        "Debug / Direct Fallback (Empirical Generator)"
    ],
    horizontal=True
)

objects = st.multiselect(
    "Select Tables / Views",
    ["CUSTOMERS", "ORDERS", "FACT_SALES", "VW_REVENUE"]
)

rows = st.number_input("Rows to Generate", min_value=10, value=500)

if st.button("Generate Synthetic Data"):
    st.success("Synthetic generation workflow started.")
    st.write("Database:", db)
    st.write("Schema:", schema)
    st.write("Mode:", mode)
    st.write("Objects:", objects)
    st.write("Rows:", rows)

st.divider()

st.subheader("Preview")
st.info("Synthetic table preview will appear here.")
