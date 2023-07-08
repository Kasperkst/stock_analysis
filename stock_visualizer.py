import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

# Continue with the rest of your imports...
from flask_caching import Cache
import pandas as pd
import plotly.graph_objs as go
import webbrowser

# Continue with the rest of your code...
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
        html.H2("Stock Analysis", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Historical Prices", href="/tab-1", active="exact"),
                dbc.NavLink("Volume", href="/tab-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/tab-1":
        return dcc.Graph(
            # ... Your code for the Historical Prices graph...
        )
    elif pathname == "/tab-2":
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
