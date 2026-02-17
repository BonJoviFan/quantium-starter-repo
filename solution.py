# Import pandas
import pandas as pd

# Read the csv files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine into one table
df = pd.concat([df1, df2, df3])

# Filter only pink morsels
df = df[df["product"] == "pink morsel"]

# Remove $ sign and convert price to a number
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Calculate sales
df["sales"] = df["quantity"] * df["price"]
df = df[["sales", "date", "region"]]

# Save to output file
df.to_csv("data/daily_sales_data.csv", index=False)

print("Done!")