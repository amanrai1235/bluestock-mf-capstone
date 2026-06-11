
import pandas as pd

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

def recommend_funds(risk_level):

    if risk_level == "Low":
        rec = fund_master[
            fund_master["risk_category"].str.contains(
                "Low", case=False, na=False
            )
        ]

    elif risk_level == "Moderate":
        rec = fund_master[
            fund_master["risk_category"].str.contains(
                "Moderate", case=False, na=False
            )
        ]

    else:
        rec = fund_master[
            fund_master["risk_category"].str.contains(
                "High", case=False, na=False
            )
        ]

    return rec[
        ["amfi_code","scheme_name","category","risk_category"]
    ].head(3)

print(recommend_funds("High"))
