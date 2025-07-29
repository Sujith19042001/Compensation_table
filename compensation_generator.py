import streamlit as st
import pandas as pd

# Taxonomy mapping
taxonomy_map = {
    "Fees Earned or Paid in Cash": "Salary",
    "Salary":"Salary",
    "Bonus": "Bonus",
   "Non-Equity Incentive Plan Compensation" :"Non-Equity Incentive Plan Compensation",
   "Change in pension value and nonqualified deferred compensation earnings" :"Change in pension value and nonqualified deferred compensation earnings", 
    "Stock Awards": "Stock Awards",
    "Option Awards" :"Option Awards",
    "Other Compensation": "Other Compensation",
    "All Other Compensation":"Other Compensation",
    "Total": "Total Compensation",
    "Total Compensation" : "Total Compensation"

}

st.title("Compensation Table Generator")

# Sidebar or main controls
with st.form("comp_form"):
    col1, col2 = st.columns(2)
    with col1:
        selected_params = st.multiselect(
            "Parameters", list(taxonomy_map.keys())
        )
    with col2:
        selected_years = st.multiselect(
            "Years", ["2024","2023","2022","2021"]
        )
    
    repeat = st.number_input("Repeat", min_value=1, value=1, step=1)
    submitted = st.form_submit_button("Generate")

# Table generation
if submitted:
    records = []
    selected_years.sort()
    for r in range(repeat):
        for year in selected_years:
            for param in selected_params:
                taxonomy = taxonomy_map.get(param, "Unknown")
                records.append({
                    "Parameter": param,
                    "Year": year,
                    "Taxonomy": taxonomy
                })
    
    df = pd.DataFrame(records)
    st.write("### Generated Table")
    st.table(df)