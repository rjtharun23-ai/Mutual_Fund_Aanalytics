import requests
import pandas as pd
import os

os.makedirs("data/raw/live_nav", exist_ok=True)

schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])
    df["scheme_code"] = code
    df["scheme_name"] = name

    file_path = f"data/raw/live_nav/{name}_{code}.csv"
    df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")