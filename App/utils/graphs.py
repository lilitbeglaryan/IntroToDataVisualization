# utils/graphs.py

import plotly.express as px
import seaborn as sns
import pandas as pd

def plot_default_distribution(df):
    return px.histogram(
        df,
        x="default_label",
        color="default_label",
        title="Distribution of Defaults",
        labels={"default_label": "Default Status", "count": "Number of Records"},
        color_discrete_map={"Default": "#8e44ad", "No Default": "#d2b4de"},
    ).update_layout(
        yaxis_title="Number of Records",
        font=dict(family="Poppins", size=14),
    )


def plot_age_vs_default(df):
    return px.box(
        df,
        x="default_label",
        y="age",
        color="default_label",
        title="Age Distribution by Default Status",
        labels={"default_label": "Default", "age": "Age"},
        color_discrete_map={"Default": "#8e44ad", "No Default": "#d2b4de"},
    ).update_layout(
        yaxis_title="Age",
        font=dict(family="Poppins", size=14),
    )


def plot_purpose_vs_default(df):
    return px.histogram(
        df,
        x="purpose",
        color="default_label",
        barmode="group",
        title="Loan Purpose vs Default",
        labels={"default_label": "Default", "purpose": "Loan Purpose"},
        color_discrete_map={"Default": "#8e44ad", "No Default": "#d2b4de"},
    ).update_layout(
        yaxis_title="Number of Records",
        font=dict(family="Poppins", size=14),
    )
def plot_credit_amount_by_default(df, selected_purpose=None):
    import plotly.graph_objects as go

    df = df.copy()
    purposes = df["purpose"].unique()
    fig = go.Figure()

    # Define purple shades
    color_palette = ["#9B59B6", "#8E44AD", "#7D3C98", "#6C3483", "#5B2C6F", "#4A235A"]
    purpose_colors = {purpose: color_palette[i % len(color_palette)] for i, purpose in enumerate(purposes)}

    for purpose in purposes:
        purpose_df = df[df["purpose"] == purpose]
        color = purpose_colors[purpose]
        opacity = 1.0 if purpose == selected_purpose else 0.5

        fig.add_trace(go.Histogram(
            x=purpose_df["credit_amount"],
            name=purpose[:12],  # Shorten name
            marker_color=color,
            opacity=opacity
        ))

    fig.update_layout(
        barmode="overlay",
        title="Credit Amount by Purpose",
        xaxis_title="Credit Amount",
        yaxis_title="Number of Records",
        legend_title="Purpose",
        bargap=0.1,
        xaxis_tickangle=0  # Horizontal
    )

    return fig



def plot_credit_history_by_default(df, selected_purpose=None):
    import plotly.express as px

    df = df.copy()
    if selected_purpose:
        df["highlight"] = df["purpose"].apply(
            lambda x: x if x == selected_purpose else "Other"
        )
    else:
        df["highlight"] = df["purpose"]

    # Purple palette for selected vs other
    color_map = {
        selected_purpose: "#8E44AD",
        "Other": "#D7BDE2"
    } if selected_purpose else None

    # Create a dynamic title
    title = (
        f"Credit History Distribution (Highlighted: {selected_purpose})"
        if selected_purpose
        else "Credit History Distribution by Loan Purpose"
    )

    return px.histogram(
        df,
        x="credit_history",
        color="highlight",
        barmode="group",
        title=title,
        labels={
            "credit_history": "Credit History",
            "highlight": "Loan Purpose",
        },
        color_discrete_map=color_map
    ).update_layout(
        xaxis_tickangle=0,
        yaxis_title="Number of Records"
    )



def plot_correlation_heatmap(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).drop(columns=["default"]).copy()
    corr_matrix = numeric_cols.corr()

    fig = px.imshow(
        corr_matrix,
        text_auto=".2f",
        title="Correlation Heatmap (Numerical Features)",
        color_continuous_scale=["#d2b4de", "#8e44ad"],
        labels={"color": "Correlation"},
    )

    fig.update_layout(
        font=dict(family="Poppins", size=14),
    )

    return fig
