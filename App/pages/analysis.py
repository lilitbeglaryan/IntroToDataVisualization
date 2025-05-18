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
    html.H2("In-Depth Credit Risk Analysis", style={
        "color": "#8e44ad",
        "fontFamily": "Poppins, sans-serif",
        "fontSize": "32px",
        "marginTop": "30px",
        "marginBottom": "10px",
        "textShadow": "1px 1px 2px rgba(0,0,0,0.2)",
    }),
    html.P("Explore deeper relationships between variables and default status.", style={
        "color": "#f5f5f5",
        "fontFamily": "Poppins, sans-serif",
        "fontSize": "18px",
        "marginBottom": "30px"
    }),

    # Filters container - center horizontally
html.Div([
    html.Label("Filter by Purpose:", style={
        "color": "#8e44ad",
        "fontFamily": "Poppins, sans-serif",
        "fontWeight": "600",
        "marginRight": "15px",
        "fontSize": "16px"
    }),
    dcc.Dropdown(
        id="purpose-dropdown",
        options=[{"label": p, "value": p} for p in sorted(df["purpose"].unique())],
        value=None,
        placeholder="Select a loan purpose (optional)",
        style={
            "width": "250px",
            "color": "#4b0082",           # Dark purple text
            "backgroundColor": "#f8f0ff", # Light purple background
            "border": "1px solid #8e44ad", # Purple border
        },
        className="custom-dropdown"
    ),


    html.Label("Filter by Age:", style={
        "color": "#8e44ad",
        "fontFamily": "Poppins, sans-serif",
        "fontWeight": "600",
        "marginLeft": "40px",
        "marginRight": "15px",
        "fontSize": "16px"
    }),
    html.Div(
        dcc.Slider(
            id="age-slider",
            min=df["age"].min(),
            max=df["age"].max(),
            value=df["age"].max(),
            step=1,
            marks={i: str(i) for i in range(20, 80, 10)},
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        style={"width": "300px", "display": "inline-block", "verticalAlign": "middle"}
    ),
], style={
    "display": "flex",
    "justifyContent": "center",
    "alignItems": "center",
    "marginBottom": "40px",
    "flexWrap": "wrap",
    "gap": "20px",
}),


    # Graphs side by side container
    html.Div([
        dcc.Graph(id="credit-amount-graph", style={"flex": "1", "minWidth": "300px", "height": "400px"}),
        dcc.Graph(id="credit-history-graph", style={"flex": "1", "minWidth": "300px", "height": "400px"}),
    ], style={
        "display": "flex",
        "justifyContent": "space-around",
        "gap": "20px",
        "flexWrap": "wrap",  # responsive wrap for small screens
        "marginBottom": "40px"
    }),

    dcc.Graph(figure=plot_correlation_heatmap(df)),
], style={
    "padding": "20px",
    "backgroundColor": "#1a1a2e",
    "borderRadius": "10px",
    "boxShadow": "0 4px 10px rgba(0, 0, 0, 0.3)",
})


@dash.callback(
    Output("credit-amount-graph", "figure"),
    Output("credit-history-graph", "figure"),
    Input("purpose-dropdown", "value"),
    Input("age-slider", "value")
)
def update_graphs(selected_purpose, selected_age):
    filtered_df = df[df["age"] <= selected_age]

    # Ensure the selected purpose actually exists in the filtered dataset
    valid_purposes = df["purpose"].unique()

    if selected_purpose in valid_purposes:
        filtered_df = filtered_df[filtered_df["purpose"] == selected_purpose]
    else:
        selected_purpose = None  # Fallback to show all

    return (
        plot_credit_amount_by_default(filtered_df, selected_purpose),
        plot_credit_history_by_default(filtered_df, selected_purpose)
    )
