import pandas as pd

def load_data(file_path="data/investments.csv"):
    df = pd.read_csv(file_path, parse_dates=["Date"], dayfirst=True)
    return df

def overall_summary(df):
    total_invested = df["Amount"].sum()
    current_value = (df["Units"] * df["NAV"]).sum()
    profit_loss = current_value - total_invested
    return {
        "Total Invested": total_invested,
        "Current Value": current_value,
        "Profit/Loss": profit_loss
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
