from mftool import Mftool

mf = Mftool()

mutual_funds = {
    "Bandhan Small Cap Fund": "147946",
    "Axis Small Cap Fund": "125354",
    "SBI Small Cap Fund": "125497",
    "quant Small Cap Fund": "120828",
    "Motilal Oswal Midcap Fund": "127042",
    "HSBC Midcap Fund": "151034",
    "Kotak Midcap Fund": "119775",
    "quant Mid Cap Fund": "120841",
    "Edelweiss Nifty Midcap150 Momentum 50 Index Fund": "150902",
    "Parag Parikh Flexi Cap Fund": "122639",
    "Kotak Flexicap Fund": "112090",
    "Nippon India Large Cap Fund": "118632",
    "ICICI Pru BHARAT 22 FOF": "143903",
    "Mirae Asset FANG+": "148928",
    "SBI Magnum Children's Benefit Fund": "148490"
}

def update_navs(df):
    for fund, code in mutual_funds.items():
        nav_data = mf.get_scheme_quote(code)
        if nav_data:
            latest_nav = float(nav_data["nav"])
            df.loc[df["FundName"] == fund, "NAV"] = latest_nav
    return df
