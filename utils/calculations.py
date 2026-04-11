import pandas as pd
import os

def load_all_funds(base_path="mutualfund"):
    all_data = []
    for fund in os.listdir(base_path):
        file_path = os.path.join(base_path, fund, "fund.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path, parse_dates=["Date"], dayfirst=True)
            df["FundName"] = fund
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

def overall_summary(df):
    total_invested = df["Amount"].sum()
    current_value = (df["Units"] * df["NAV"]).sum()
    return {
        "Total Invested": total_invested,
        "Current Value": current_value,
        "Profit/Loss": current_value - total_invested
    }

def fund_summary(df, fund_name):
    fund_df = df[df["FundName"] == fund_name]
    invested = fund_df["Amount"].sum()
    current_value = (fund_df["Units"] * fund_df["NAV"]).sum()
    return {
        "Invested": invested,
        "Current Value": current_value,
        "Profit/Loss": current_value - invested
    }
