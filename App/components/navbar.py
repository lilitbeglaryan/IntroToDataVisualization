# components/navbar.py

import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Overview", href="/")),
        dbc.NavItem(dbc.NavLink("Analysis", href="/analysis")),
    ],
    brand="Credit Scoring Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
)
