# components/navbar.py

import dash_bootstrap_components as dbc
from dash import html, callback, Input, Output, State

navbar = dbc.Navbar(
    dbc.Container(
        [
            # Left: Video + Title in a horizontal row
            html.Div([
                html.Video(
                    src="/assets/Finance_img1.mp4",
                    autoPlay=True,
                    loop=True,
                    muted=True,
                    style={
                        "height": "60px",  # Control scaling height here
                        "width": "auto",
                        "marginRight": "10px",
                        "objectFit": "contain",
                    }
                ),
                dbc.NavbarBrand("Credit Scoring Dashboard", href="/", className="navbar-brand"),
            ], style={
                "display": "flex",
                "alignItems": "center",
                "flexShrink": "0"  # Prevent shrinking on smaller screens
            }),

            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),

            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Overview", href="/", className="nav-link me-4")),  # Adds right margin
                        dbc.NavItem(dbc.NavLink("Analysis", href="/analysis", className="nav-link")),
                    ],
                    className="ms-auto d-flex gap-4",  # Push to right and add space between links
                    navbar=True
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            )
        ]
    ),
    color="primary",
    dark=True,
    className="navbar custom-navbar",
)

@callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar(n, is_open):
    if n:
        return not is_open
    return is_open
