# utils/graphs.py

import plotly.express as px
import seaborn as sns
import pandas as pd

def plot_default_distribution(df):
    """Bar chart of default vs non-default counts"""
    return px.histogram(
        df,
        x="default_label",
        color="default_label",
        title="Distribution of Defaults",
        labels={"default_label": "Default Status"},
        color_discrete_map={"Default": "#E74C3C", "No Default": "#2ECC71"},
    )

def plot_age_vs_default(df):
    """Boxplot of age grouped by default"""
    return px.box(
        df,
        x="default_label",
        y="age",
        color="default_label",
        title="Age Distribution by Default Status",
        labels={"default_label": "Default", "age": "Age"},
        color_discrete_map={"Default": "#E74C3C", "No Default": "#2ECC71"},
    )

def plot_purpose_vs_default(df):
    """Grouped bar chart showing purpose of loan vs default"""
    return px.histogram(
        df,
        x="purpose",
        color="default_label",
        barmode="group",
        title="Loan Purpose vs Default",
        labels={"default_label": "Default", "purpose": "Loan Purpose"},
        color_discrete_map={"Default": "#E74C3C", "No Default": "#2ECC71"},
    )

def plot_credit_amount_by_default(df, selected_purpose=None):
    """
    Simulate ghosting effect: highlight selected purpose, gray out others.
    Keeps all bars visible and clickable via Plotly legend.
    """
    import plotly.graph_objects as go

    df = df.copy()
    purposes = df["purpose"].unique()
    fig = go.Figure()

    for purpose in purposes:
        purpose_df = df[df["purpose"] == purpose]
        color = "#1F77B4" if purpose == selected_purpose else "#C7E9F1"
        opacity = 1.0 if purpose == selected_purpose else 0.4

        fig.add_trace(go.Histogram(
            x=purpose_df["credit_amount"],
            name=purpose,
            marker_color=color,
            opacity=opacity
        ))

    fig.update_layout(
        barmode="overlay",
        title="Credit Amount Distribution by Purpose",
        xaxis_title="Credit Amount",
        yaxis_title="Count",
        legend_title="Purpose",
        bargap=0.1
    )

    return fig


# def plot_credit_amount_by_default(df, selected_purpose=None):
#     """
#     Histogram of credit amount by default, with optional highlighting for selected purpose
#     """
#     df = df.copy()
#     if selected_purpose:
#         # Add a highlight flag
#         df["highlight"] = df["purpose"].apply(
#             lambda x: x if x == selected_purpose else "Other"
#         )
#     else:
#         df["highlight"] = df["purpose"]
#
#     color_map = {
#         selected_purpose: "#E74C3C",
#         "Other": "#D3D3D3"
#     } if selected_purpose else None
#
#     return px.histogram(
#         df,
#         x="credit_amount",
#         color="highlight",
#         nbins=50,
#         title="Credit Amount Distribution (Highlighted Purpose)",
#         labels={"credit_amount": "Credit Amount", "highlight": "Purpose"},
#         color_discrete_map=color_map
#     )

# def plot_credit_history_by_default(df,selected_purpose):
#     """Stacked bar chart of credit history vs default"""
#     return px.histogram(
#         df,
#         x="credit_history",
#         color="default_label",
#         barmode="relative",
#         title="Credit History vs Default",
#         labels={"credit_history": "Credit History", "default_label": "Default"},
#         color_discrete_map={"Default": "#E74C3C", "No Default": "#2ECC71"},
#     )
def plot_credit_history_by_default(df, selected_purpose=None):
    """
    Stacked bar chart of credit history vs default, with optional highlighting for selected purpose
    """
    df = df.copy()
    if selected_purpose:
        df["highlight"] = df["purpose"].apply(
            lambda x: x if x == selected_purpose else "Other"
        )
    else:
        df["highlight"] = df["purpose"]

    color_map = {
        selected_purpose: "#3498DB",  # Blue
        "Other": "#D3D3D3"
    } if selected_purpose else None

    return px.histogram(
        df,
        x="credit_history",
        color="highlight",
        barmode="group",
        title="Credit History vs Default (Highlighted Purpose)",
        labels={"credit_history": "Credit History", "highlight": "Purpose"},
        color_discrete_map=color_map
    )


def plot_correlation_heatmap(df):
    """Generate a heatmap of correlations between numerical columns"""
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).drop(columns=["default"]).copy()
    corr_matrix = numeric_cols.corr()

    fig = px.imshow(
        corr_matrix,
        text_auto=".2f",
        title="Correlation Heatmap (Numerical Features)",
        color_continuous_scale="RdBu",
        labels={"color": "Correlation"},
    )
    return fig
