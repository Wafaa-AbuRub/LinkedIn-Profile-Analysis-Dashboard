"""
{
    "title": "Connections Cards Maths & Layouts",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Calculates the number of LinkedIn connections per month, company, and position within a specific date range."
}
"""


from dash import Dash, dcc
import pandas as pd
import dash_bootstrap_components as dbc
from components.styles import graph_cards_style
from components.ids import ConnectionCardsIDs, DatePickerIDs


def render(app: Dash, data: pd.DataFrame) -> list:
    """
    Renders the connection cards and gathers the filtration selections associated with the
    user's interactions to calculate connections number per month, company, and position
    within a specific date range.
    """

    connections_cards_layout = [
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_month, figure={})])], style=graph_cards_style)], width=6),
            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_company, figure={})])], style=graph_cards_style)], width=6),
            # ....Third Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_position, figure={})])],style=graph_cards_style)], width=4)]

    return connections_cards_layout


