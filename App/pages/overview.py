# pages/overview.py

import dash
from dash import html, dcc
from data.load_data import load_data
from utils.graphs import (
    plot_default_distribution,
    plot_age_vs_default,
    plot_purpose_vs_default
)

dash.register_page(__name__, path="/")

df = load_data()

layout = html.Div([
    html.Div([
        html.H2("Overview of Credit Defaults", className="section-title"),
        html.P("A general look at default distribution, age, and loan purpose.", className="section-description"),

        dcc.Graph(figure=plot_default_distribution(df)),
        dcc.Graph(figure=plot_age_vs_default(df)),
        dcc.Graph(figure=plot_purpose_vs_default(df)),
    ], className="graph-section")

])
