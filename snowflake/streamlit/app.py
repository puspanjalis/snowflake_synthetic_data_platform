
import streamlit as st

st.set_page_config(page_title="Synthetic Data Generator", layout="wide")

st.title("Synthetic Data Generator")
st.caption("Enterprise Synthetic Data Generation Platform for Snowflake")

db_name = st.text_input("Database", placeholder="e.g., EDW")
schema_name = st.text_input("Schema", placeholder="e.g., SALES")

mode = st.radio(
    "Generation Mode",
    [
        "Generate via Wrapper (Recommended)",
        "Debug / Direct Fallback (Empirical Generator)"
    ],
    horizontal=True
)

selected_objects = st.multiselect(
    "Select Tables / Views",
    ["CUSTOMERS", "ORDERS", "FACT_SALES", "VW_REVENUE"]
)

rows = st.number_input(
    "Rows to Generate",
    min_value=10,
    max_value=200000,
    value=500
)

if st.button("Generate Synthetic Data"):
    st.success("Synthetic generation workflow started.")

    st.write("Database:", db_name)
    st.write("Schema:", schema_name)
    st.write("Mode:", mode)
    st.write("Objects:", selected_objects)
    st.write("Rows:", rows)

st.divider()

st.subheader("Synthetic Preview")
st.info("Preview will appear here after generation.")
