import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv('activities.csv')

temp_time_speed = data.filter(['Activity Date','Activity Type','Elapsed Time','Distance', 'Relative Effort','Average Speed','Average Heart Rate','Calories','Apparent Temperature','Humidity','Wind Gust','Percipitation'],axis=1)
temp_time_speed = temp_time_speed.drop(temp_time_speed[(temp_time_speed['Activity Type'] != 'Run')].index)

""" fig = go.Figure([go.Scatter(x=temp_time_speed['Activity Date'], y=temp_time_speed['Relative Effort'])])
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
fig.show() """

temp_time_speed['Activity Date'] = pd.to_datetime(temp_time_speed['Activity Date'], infer_datetime_format=True)

fig = px.line(temp_time_speed, x='Activity Date', y='Average Speed')

fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
fig.show()
#print(temp_time_speed.dtypes)