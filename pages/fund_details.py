import streamlit as st
from utils.calculations import load_all_funds, fund_summary
from utils.nav_fetch import update_navs

st.title("📈 Individual Fund Details")

df = load_all_funds()
df = update_navs(df)

funds = df["FundName"].unique()
selected_fund = st.selectbox("Choose a Fund", funds)

summary = fund_summary(df, selected_fund)

st.metric("Invested", f"₹{summary['Invested']:.2f}")
st.metric("Current Value", f"₹{summary['Current Value']:.2f}")
st.metric("Profit/Loss", f"₹{summary['Profit/Loss']:.2f}")

st.write("### Transaction History")
st.dataframe(df[df["FundName"] == selected_fund])
