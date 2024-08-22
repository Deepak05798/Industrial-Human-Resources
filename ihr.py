import streamlit as st
import plotly.express as px
import pandas as pd
import json

# Load the dataset
df = pd.read_csv("data.csv")

# Load the India GeoJSON file
with open("Indian_States", "r") as file:
    india_states = json.load(file)

# Streamlit app title
st.title("Industrial Human Resource Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

# Filter options for states and clusters
selected_state = st.sidebar.selectbox("Select a State", df['States'].unique())
selected_cluster = st.sidebar.selectbox("Select a Cluster", df['text_cluster'].unique())

# Filter dataset based on user selection
filtered_data = df[(df['States'] == selected_state) & (df['text_cluster'] == selected_cluster)]

# Visualize worker distribution across industries for the selected state and cluster
st.subheader(f"Main Workers by Industry for {selected_state} in Cluster {selected_cluster}")

# Create bar plot for main workers by industry
fig_main_workers = px.bar(filtered_data, x='NIC_Name', y='Main Workers', color='NIC_Name',
                          title='Main Workers by Industry',
                          labels={'NIC_Name': 'Industry', 'Main Workers': 'Number of Workers'},
                          height=500)
st.plotly_chart(fig_main_workers)

# Visualize rural vs urban distribution of main workers
st.subheader(f"Rural vs Urban Main Workers Distribution for {selected_state} in Cluster {selected_cluster}")

# Create a stacked bar plot for rural and urban main workers
fig_main_rural_urban = px.bar(filtered_data, x='NIC_Name', y=['Main Workers Rural', 'Main Workers Urban'],
                              title='Rural vs Urban Main Workers Distribution',
                              labels={'value': 'Number of Workers', 'NIC_Name': 'Industry'},
                              height=500)
st.plotly_chart(fig_main_rural_urban)

# Visualize rural vs urban distribution of marginal workers
st.subheader(f"Rural vs Urban Marginal Workers Distribution for {selected_state} in Cluster {selected_cluster}")

# Create a stacked bar plot for rural and urban marginal workers
fig_marginal_rural_urban = px.bar(filtered_data, x='NIC_Name', y=['Marginal Workers Rural', 'Marginal Workers Urban'],
                                  title='Rural vs Urban Marginal Workers Distribution',
                                  labels={'value': 'Number of Workers', 'NIC_Name': 'Industry'},
                                  height=500)
st.plotly_chart(fig_marginal_rural_urban)

# Geo-Visualization
st.subheader("Geographical Distribution of Workers")

# Aggregate data at the state level for visualization
geo_data = df.groupby('States').sum().reset_index()

# Create a choropleth map for India
fig_geo = px.choropleth(geo_data, 
                        geojson=india_states, 
                        locations='States', 
                        featureidkey="properties.ST_NM",
                        color='Main Workers', 
                        hover_name='States', 
                        color_continuous_scale='Viridis',
                        title='Geographical Distribution of Main Workers in India')

# Ensuring the map is visible and fits within the boundaries
fig_geo.update_geos(fitbounds="locations", visible=False)

# Display the map in Streamlit
st.plotly_chart(fig_geo)

# Display some statistical insights for all worker categories
st.subheader("Statistical Overview of Workers")
st.write(filtered_data[['Main Workers', 'Main Workers Rural', 'Main Workers Urban',
                        'Marginal Workers', 'Marginal Workers Rural', 'Marginal Workers Urban']])
