"""
{
    "title": "LinkedIn Profile Dashboard Layout",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Creates a personal dashboard layout for the owner's LinkedIn profile."
}
"""

from dash import Dash
import dash_bootstrap_components as dbc


def wireframe_layout(app: Dash, data: dict) -> dbc.Container:
    """Creates the main interface components."""

    layout = dbc.Container(children=[
        # ....First Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardImg(src="assets/linkedin_logo.png")], className='mb-2'),
                     dbc.Card([dbc.CardBody([dbc.CardLink(data["owner_name"], target="_blank", href=data["owner_linkedin_profile"])])])],
                    width=2),

            # ....Second Column.... #
            dbc.Col([dbc.Card(dbc.CardBody([]))], width=10)],

            className="mb-2 mt-2"),

        # ....Second Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),

            # ....Third Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),

            # ....Forth Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),

            # ....Fifth Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),

            # ....Sixth Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=2)],

            className="mb-2"
        ),

        # ....Third Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=6),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=6)],

            className="mb-2"),

        # ....Forth Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=4),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=4),

            # ....Third Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([])])], width=4)],

            className="mb-2")
    ], fluid=True)

    return layout


