import streamlit as st
from utils.calculations import load_all_funds, overall_summary
from utils.nav_fetch import update_navs

st.title("📊 Overall Investment Summary")

df = load_all_funds()
df = update_navs(df)

summary = overall_summary(df)

st.metric("Total Invested", f"₹{summary['Total Invested']:.2f}")
st.metric("Current Value", f"₹{summary['Current Value']:.2f}")
st.metric("Profit/Loss", f"₹{summary['Profit/Loss']:.2f}")

st.write("### All Transactions")
st.dataframe(df)
