import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('ev-charging-station.csv')

# Remove any rows with missing coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create density heatmap
fig = px.density_mapbox(df, 
                        lat='Latitude', 
                        lon='Longitude',
                        radius=10,
                        zoom=3,
                        mapbox_style="open-street-map",
                        title="EV Charger Locations Heatmap")

fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig.show()

# Optional: Save as HTML
fig.write_html('ev_chargers_plotly.html')
