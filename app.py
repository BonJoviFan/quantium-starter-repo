import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Read the processed sales data
df = pd.read_csv("data/daily_sales_data.csv")

# Sort by date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by=["date"], ascending=True)

# Create the line chart
fig = px.line(df, x="date", y="sales", color="region"
              ,title="",
              labels={"date": "Date","sales": "Sales ($)", "region": "Region"})

# Create the dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    # Header
    html.H1("Pink Morsel Sales: Before and After Price Increase"),
    # Line Chart
    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
