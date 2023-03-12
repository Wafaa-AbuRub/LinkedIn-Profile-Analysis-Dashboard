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
import plotly.express as px
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

    def messages_summary(_owner_name: str, _data: pd.DataFrame):
        """
        Generates a pie chart that represents the total number of sent & received messages.
        """

        msg_sent_num = len(_data.query("sender_name == @_owner_name"))
        msg_received_num = len(_data.query("sender_name != @_owner_name"))

        fig = px.pie(names=["Sent", "Received"], values=[msg_sent_num, msg_received_num],
                     template="ggplot2", title="Messages Sent & Received")

        fig.update_traces(marker_colors=['orange', 'royalblue'])

        return fig

    def messages_by_month(_owner_name: str, _data: pd.DataFrame):
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

        m_df = data.query("@start_dt <= date <= @end_dt").reset_index(drop=True)

        messages_cards_figs = [messages_summary(owner_name, m_df), messages_by_month(owner_name, m_df)]

        return messages_cards_figs

    messages_cards_layout = [
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=MessageCardsIDs.msr, figure={})])], style=graph_cards_style)], width=6),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=MessageCardsIDs.msr_by_month, figure={})])], style=graph_cards_style)], width=6)]

    return messages_cards_layout


