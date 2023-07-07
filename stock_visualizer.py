import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc, html
import webbrowser

# Load the data
df = pd.read_excel('historical_prices.xlsx')

app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Historical Prices', children=[
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Scatter(
                            x=df['Date'], 
                            y=df['Close'], 
                            mode='lines',
                            name='Historical Prices'
                        )
                    ],
                    layout=go.Layout(
                        title='Historical Prices',
                        showlegend=True,
                        legend=go.layout.Legend(
                            x=0,
                            y=1.0
                        ),
                        margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                    )
                ),
                style={'height': 300},
                id='my-graph'
            )
        ]),
        dcc.Tab(label='Volume', children=[
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=df['Date'], 
                            y=df['Volume'], 
                            name='Volume'
                        )
                    ],
                    layout=go.Layout(
                        title='Volume',
                        showlegend=True,
                        legend=go.layout.Legend(
                            x=0,
                            y=1.0
                        ),
                        margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                    )
                ),
                style={'height': 300},
                id='my-graph2'
            )
        ])
    ])
])

if __name__ == '__main__':
    # Open the web browser before running the app
    webbrowser.open('http://127.0.0.1:8050/')
    app.run_server(debug=True)
