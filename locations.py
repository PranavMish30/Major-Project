import pandas as pd

# Read Excel file
df = pd.read_excel("locations.xlsx")  # make sure Name and Code columns exist

# Create vertices list (list of tuples)
vertices = list(zip(df["Landmark"], df["BSSID"]))

# name → index
landmark_to_index = {name: i for i, (name, code) in enumerate(vertices)}

# code → index
bssid_to_index = {code: i for i, (name, code) in enumerate(vertices)}


