"""
{
    "title": "Messages Cards Maths & Layouts",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Calculates the number of LinkedIn messages sent&received total, and per month within a specific date range."
}
"""


import pandas as pd
from datetime import date
from dash import Dash, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from components.styles import graph_cards_style
from components.ids import MessageCardsIDs, DatePickerIDs


def render(app: Dash, owner_name: str, data: pd.DataFrame) -> list:
    """
    Renders the message cards and gathers the filtration selections associated with the
    user's interactions to calculate the messages number sent & received total and per month
    within a specific date range.
    """

    def messages_summary(_data: pd.DataFrame):
        """
        TODO: Type the functionality here...
        """

        return []

    def messages_by_month(_data: pd.DataFrame):
        """
        TODO: Type the functionality here...
        """

        return []

    @app.callback(
        Output(MessageCardsIDs.msr, "figure"),
        Output(MessageCardsIDs.msr_by_month, "figure"),
        Input(DatePickerIDs.start, "date"),
        Input(DatePickerIDs.end, "date")
    )
    def update_message_cards(start_dt: date, end_dt: date):
        """Updates the graphs within the message cards."""

        m_df = data.query("@start_dt <= connected_on <= @end_dt").reset_index(drop=True)

        messages_cards_figs = [messages_summary(m_df), messages_by_month(m_df)]

        return messages_cards_figs

    messages_cards_layout = [
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=MessageCardsIDs.msr, figure={})])], style=graph_cards_style)], width=6),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=MessageCardsIDs.msr_by_month, figure={})])], style=graph_cards_style)], width=6)]

    return messages_cards_layout


