import pandas as pd
import numpy as np
import scipy
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv('activities.csv')

temp_time_speed = data.filter(['Activity Date','Activity Type','Elapsed Time','Distance', 'Relative Effort','Average Speed','Average Heart Rate','Calories','Apparent Temperature','Humidity','Wind Gust','Percipitation'],axis=1)
temp_time_speed = temp_time_speed.drop(temp_time_speed[(temp_time_speed['Activity Type'] != 'Run')].index)
dropdown=temp_time_speed.filter(['Elapsed Time','Average Speed'],axis=1)

""" fig = go.Figure([go.Scatter(x=temp_time_speed['Activity Date'], y=temp_time_speed['Relative Effort'])])
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
fig.show() """

temp_time_speed['Activity Date'] = pd.to_datetime(temp_time_speed['Activity Date'], infer_datetime_format=True)
"""
fig = px.line(temp_time_speed, x='Activity Date', y='Average Speed')

fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
fig.show() """

#fig = go.Figure()

""" for column in dropdown.columns.to_list():
    fig.add_trace(
        go.Scatter(
            x = temp_time_speed['Activity Date'],
            y = dropdown['Elapsed Time'],
            name = column
        )
    ) """
    
""" fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [dict(label = 'Distance',
                  method = 'update',
                  args = [{'visible': [False, False, False, False]},
                          {'title': 'All',
                           'showlegend':True}]),
             dict(label = 'Relative Effort',
                  method = 'update',
                  args = [{'visible': [True, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'MSFT',
                           'showlegend':True}]),
             dict(label = 'Average Heart Rate',
                  method = 'update',
                  args = [{'visible': [False, True, False, False]},
                          {'title': 'AAPL',
                           'showlegend':True}]),
             dict(label = 'Average Speed',
                  method = 'update',
                  args = [{'visible': [False, False, True, False]},
                          {'title': 'AMZN',
                           'showlegend':True}]),
             dict(label = 'Elapsed Time',
                  method = 'update',
                  args = [{'visible': [False, False, False, True]},
                          {'title': 'GOOGL',
                           'showlegend':True}]),
            ])
        )
    ])
 """

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=temp_time_speed['Activity Date'], y=temp_time_speed['Average Speed'], name="Average Speed"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=temp_time_speed['Activity Date'], y=temp_time_speed['Apparent Temperature'], name="Temperature",line=None),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Effect of temperature and running "
)

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Average Speed</b> km/h", secondary_y=False)
fig.update_yaxes(title_text="<b>Temperature</b> deg Celsius", secondary_y=True)

fig.show()




#print(temp_time_speed.dtypes)