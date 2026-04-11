from mftool import Mftool

mf = Mftool()

def get_nav(fund_code):
    data = mf.get_scheme_quote(fund_code)
    if data:
        return float(data["nav"])
    return None
