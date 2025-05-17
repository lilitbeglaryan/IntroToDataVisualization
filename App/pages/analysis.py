# pages/analysis.py

import dash
from dash import html, dcc, Input, Output
from data.load_data import load_data
from utils.graphs import (
    plot_credit_amount_by_default,
    plot_credit_history_by_default,
    plot_correlation_heatmap
)

dash.register_page(__name__, path="/analysis")

df = load_data()


layout = html.Div([
    html.H2("In-Depth Credit Risk Analysis"),
    html.P("Explore deeper relationships between variables and default status."),

    dcc.Graph(id="credit-amount-graph"),
    dcc.Graph(id="credit-history-graph"),

    html.Label("Filter by Purpose:"),
    dcc.Dropdown(
        id="purpose-dropdown",
        options=[{"label": p, "value": p} for p in sorted(df["purpose"].unique())],
        value=None,
        placeholder="Select a loan purpose (optional)",
        style={"width": "50%"}
    ),
    html.Label("Filter by Age:"),
    dcc.Slider(
        id="age-slider",
        min=df["age"].min(),
        max=df["age"].max(),
        value=df["age"].max(),  # default max age
        step=1,
        marks={i: str(i) for i in range(20, 80, 10)},
        tooltip={"placement": "bottom", "always_visible": True},
    ),
    html.Br(),
    dcc.Graph(figure=plot_correlation_heatmap(df)),
])
# @dash.callback(
#     Output("credit-amount-graph", "figure"),
#     Output("credit-history-graph", "figure"),
#     Input("purpose-dropdown", "value"),
#     Input("age-slider", "value")
# )
@dash.callback(
    Output("credit-amount-graph", "figure"),
    Output("credit-history-graph", "figure"),
    Input("purpose-dropdown", "value"),
    Input("age-slider", "value")
)
def update_graphs(selected_purpose, selected_age):
    filtered_df = df[df["age"] <= selected_age]
    if selected_purpose:
        filtered_df = filtered_df[filtered_df["purpose"] == selected_purpose]

    return (
        plot_credit_amount_by_default(filtered_df),
        plot_credit_history_by_default(filtered_df)
    )


# def update_graphs(selected_purpose, selected_age):
#     filtered_df = df[df["age"] <= selected_age]
#
#     return (
#         plot_credit_amount_by_default(filtered_df, selected_purpose),
#         plot_credit_history_by_default(filtered_df, selected_purpose)
#     )

