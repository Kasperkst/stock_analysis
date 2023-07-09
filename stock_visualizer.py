import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from flask_caching import Cache
import pandas as pd
import plotly.graph_objs as go
import webbrowser
import plotly.figure_factory as ff
from risk_analysis import RiskAnalysisTool

# Continue with the rest of your code...
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

'''*****************************************************************************************************
Defining the dashboard layout
*****************************************************************************************************'''

# Define your sidebar style
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# Define your content style
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Dashboard", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Historical Prices", href="/tab-1", active="exact"),
                dbc.NavLink("Rolling Risk", href="/tab-2", active="exact"),
                dbc.NavLink("Expected Shortfall", href="/tab-3", active="exact"),
                dbc.NavLink("Value at Risk", href="/tab-4", active="exact"),
                dbc.NavLink("Graph5", href="/tab-5", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

'''*****************************************************************************************************
Retrieving the data
*****************************************************************************************************'''


df = pd.read_excel('historical_prices.xlsx')
def get_data_for_symbol(symbol):
    return df.loc[df['Symbol'] == symbol, ['Date', 'Close']]

#portfolio = Portfolio(asset_prices)
#risk_tool = RiskAnalysisTool(portfolio)

'''*****************************************************************************************************
Defining the graphs
*****************************************************************************************************'''


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/tab-1":
        df_filtered = get_data_for_symbol('NVO')
        return dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Scatter(
                        x=df_filtered['Date'], 
                        y=df_filtered['Close'], 
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
            id='price-graph'
        )
    elif pathname == "/tab-2":
        df_filtered = get_data_for_symbol('NVO')
        df_filtered['Returns'] = df_filtered['Close'].pct_change()  # Calculate returns
        df_filtered['Rolling Risk'] = df_filtered['Returns'].rolling(window=60).std()  # Calculate rolling risk
        return dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Scatter(
                        x=df_filtered['Date'], 
                        y=df_filtered['Rolling Risk'], 
                        mode='lines',
                        name='Rolling Risk'
                    )
                ],
                layout=go.Layout(
                    title='Rolling Risk',
                    showlegend=True,
                    legend=go.layout.Legend(
                        x=0,
                        y=1.0
                    ),
                    margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                )
            ),
            style={'height': 300},
            id='risk-graph'
        )
    elif pathname == "/tab-3":
        return dcc.Graph(
        )
    elif pathname == "/tab-4":
        return dcc.Graph(
            # ... Your code for the Volume graph...
        )
    elif pathname == "/tab-5":
        return dcc.Graph(
            # ... Your code for the Volume graph...
        )
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/')
    app.run_server(debug=True)
