import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('ev-charging-station.csv')

# Remove any rows with missing coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create scatter mapbox
fig = px.scatter_mapbox(df, 
                        lat='Latitude', 
                        lon='Longitude',
                        zoom=3,
                        mapbox_style="open-street-map",
                        opacity=0.6,
                        title="EV Charger Locations")

fig.update_traces(marker=dict(size=4))
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig.write_html('ev_chargers_plotly.html')