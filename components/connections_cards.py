"""
{
    "title": "Connections Cards Maths & Layouts",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Calculates the number of LinkedIn connections per month, company, and position within a specific date range."
}
"""


import pandas as pd
from datetime import date
from dash import Dash, dcc
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from components.styles import graph_cards_style
from components.ids import ConnectionCardsIDs, DatePickerIDs


def render(app: Dash, data: pd.DataFrame) -> list:
    """
    Renders the connection cards and gathers the filtration selections associated with the
    user's interactions to calculate connections number per month, company, and position
    within a specific date range.
    """

    def con_by_month_fig(_data: pd.DataFrame):
        """
        Generates a bar chart figure that represents the number of connections per month.
        """

        _data = _data.groupby(pd.Grouper(key='connected_on', freq='M')).size().reset_index(level=0).rename(
            columns={0: "total_connections"})

        _data["years"] = _data.connected_on.dt.year.astype(str)

        fig = px.bar(_data, x='connected_on', y='total_connections', color='years', text_auto=True,
                     title="Total Connections Per Month", height=500, template='ggplot2')

        fig.update_xaxes(dtick="M1", ticklabelmode="period", tickformat="%b")  # or "%b\n%Y"
        fig.update_traces(textposition="outside")
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))

        return fig

    def con_by_company_fig(_data: pd.DataFrame):
        """
        Generates a bar chart figure that represents the number of connections per n top companies.
        """

        # Number pf companies to present
        top_n = 7

        top_comp = _data[['company']].value_counts().reset_index().head(top_n).rename(columns={0: "total_connections"})

        fig = px.bar(top_comp, x='total_connections', y='company', orientation='h', text_auto=True,
                     title="Total Connections For Top {} Companies!".format(top_n),
                     template='ggplot2')

        fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))
        fig.update_traces(marker_color='royalblue')

        return fig

    def con_by_position_fig(_data: pd.DataFrame):
        """
        Generates a word-cloud chart figure that represents the number of connections per position.
        """

        positions_text = _data.position.fillna("Unknown").astype(str)

        positions_wordcloud = WordCloud(background_color="white", collocations=False, random_state=1,
                                        stopwords=STOPWORDS, height=275).generate(' '.join(positions_text))

        fig = px.imshow(positions_wordcloud, template='ggplot2', title="Total Connections Per Position")
        fig.update_layout(margin=dict(l=55, r=55, t=55, b=55))
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)

        return fig

    @app.callback(
        Output(ConnectionCardsIDs.tc_by_month, "figure"),
        Output(ConnectionCardsIDs.tc_by_company, "figure"),
        Output(ConnectionCardsIDs.tc_by_position, "figure"),
        Input(DatePickerIDs.range, "start_date"),
        Input(DatePickerIDs.range, "end_date")
    )
    def update_connection_cards(start_dt: date, end_dt: date):
        """Updates the graphs within the connection cards."""

        c_df = data.query("@start_dt <= connected_on <= @end_dt").reset_index(drop=True)

        connection_cards_figs = [con_by_month_fig(c_df), con_by_company_fig(c_df), con_by_position_fig(c_df)]

        return connection_cards_figs

    connections_cards_layout = [
        # ....First Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_month, figure={})])], style=graph_cards_style)], width=12)], className="mb-2 mt-3"),

        # ....Second Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_company, figure={})])], style=graph_cards_style)], width=6),
            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_position, figure={})])], style=graph_cards_style)], width=6)], className="mb-2 mt-3")]

    return connections_cards_layout


