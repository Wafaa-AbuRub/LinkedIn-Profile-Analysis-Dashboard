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
from components.ids import MessageCardsIDs, DatePickerIDs
from components.styles import cards_header_style, msr_style, msr_by_month_style, graph_cards_box_shadow


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

        fig = px.pie(names=["Sent", "Received"], values=[msg_sent_num, msg_received_num], template="ggplot2")

        fig.update_traces(marker_colors=['orange', 'royalblue'])

        return fig

    def messages_by_month(_owner_name: str, _data: pd.DataFrame):
        """
        Generates a bar chart figure that represents the number of messages sent & received per month.
        """

        _data = _data.assign(msg_source=_data.sender_name.apply(lambda x: "Sent" if x == _owner_name else "Received"))

        _data = _data.groupby([pd.Grouper(key='date', freq='M'), "msg_source"]).size().reset_index(level=[0, 1]).rename(
            columns={0: "total_messages"})

        _data["years"] = _data.date.dt.year

        fig = px.bar(_data, x='date', y='total_messages', color='msg_source', text_auto=True, barmode="group",
                     template='ggplot2', color_discrete_map={"Sent": "orange", "Received": "royalblue"},
                     labels={"total_messages": "Messages Number", "date": "Connection Month"})

        fig.update_traces(textposition="outside")
        fig.update_layout(legend_title="MSG Source", margin=dict(l=20, r=20, t=30, b=20))

        return fig

    @app.callback(
        Output(MessageCardsIDs.msr, "figure"),
        Output(MessageCardsIDs.msr_by_month, "figure"),
        Input(DatePickerIDs.range, "start_date"),
        Input(DatePickerIDs.range, "end_date")
    )
    def update_message_cards(start_dt: date, end_dt: date):
        """Updates the graphs within the message cards."""

        m_df = data.query("@start_dt <= date <= @end_dt").reset_index(drop=True)

        messages_cards_figs = [messages_summary(owner_name, m_df), messages_by_month(owner_name, m_df)]

        return messages_cards_figs

    messages_cards_layout = [
        # ....First Column.... #
        dbc.Col([dbc.Card([
            dbc.CardHeader("Messages Sent & Received", style=cards_header_style),
            dbc.CardBody([dcc.Graph(id=MessageCardsIDs.msr, figure={})])],
            style=msr_style)], width=5),

        # ....Second Column.... #
        dbc.Col([dbc.Card([
            dbc.CardHeader("Messages Sent & Received Per Month", style=cards_header_style),
            dbc.CardBody([dcc.Graph(id=MessageCardsIDs.msr_by_month, figure={})])],
            style=msr_by_month_style)], width=7)]

    return messages_cards_layout


