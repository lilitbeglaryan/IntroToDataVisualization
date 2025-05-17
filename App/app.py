# app.py

import dash
from dash import html, page_container
import dash_bootstrap_components as dbc
from components.navbar import navbar

# Enable multi-page support with Dash Pages
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Credit Scoring Dashboard"

# App layout
app.layout = dbc.Container(
    [
        navbar,
        html.Hr(), # horizontal rule (line seperator at the top)
        page_container
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
