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
import dash_bootstrap_components as dbc
from wordcloud import WordCloud, STOPWORDS
from dash.dependencies import Input, Output
from components.ids import ConnectionCardsIDs, DatePickerIDs
from components.styles import cards_header_style, tc_by_month_style, tc_by_company_style, tc_by_position_style, colors_palette


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
                     height=500, template='ggplot2',
                     color_discrete_sequence=colors_palette,
                     opacity=.9,
                     labels={"connected_on": "Connection Month", "total_connections": "Connections Number"})

        fig.update_xaxes(dtick="M1", ticklabelmode="period", tickformat="%b")  # or "%b\n%Y"
        fig.update_traces(textposition="outside")
        fig.update_layout(legend_title="Years", margin=dict(l=20, r=20, t=0, b=20))

        return fig

    # Number pf companies to present
    top_n = 7

    def con_by_company_fig(_data: pd.DataFrame):
        """
        Generates a bar chart figure that represents the number of connections per n top companies.
        """

        top_comp = _data[['company']].value_counts().reset_index().head(top_n).rename(columns={0: "total_connections"})

        fig = px.bar(top_comp, x='total_connections', y='company', orientation='h', text_auto=True, template='ggplot2',
                     opacity=.9,
                     labels={"company": "Company Name", "total_connections": "Connections Number"})

        fig.update_layout(margin=dict(l=20, r=20, t=0, b=20))
        fig.update_traces(marker_color='royalblue')

        return fig

    def con_by_position_fig(_data: pd.DataFrame):
        """
        Generates a word-cloud chart figure that represents the number of connections per position.
        """

        positions_text = _data.position.fillna("Unknown").astype(str)

        positions_wordcloud = WordCloud(background_color="white", collocations=False, random_state=1,
                                        colormap="Blues", max_font_size=300,
                                        stopwords=STOPWORDS, width=400, height=400).generate(' '.join(positions_text))

        fig = px.imshow(positions_wordcloud, template='ggplot2')
        fig.update_layout(margin=dict(l=5, r=5, t=0, b=5))
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
            dbc.Col([dbc.Card([dbc.CardHeader("Total Connections Per Month", style=cards_header_style),
                               dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_month, figure={})])],
                              style=tc_by_month_style)], width=12)], className="mb-1 mt-1"),

        # ....Second Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card(
                [dbc.CardHeader("Total Connections For Top {} Companies!".format(top_n), style=cards_header_style),
                 dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_company, figure={})])],
                style=tc_by_company_style)], width=6),

            # ....Second Column.... #
            dbc.Col(
                [dbc.Card([dbc.CardHeader("Total Connections Per Position", style=cards_header_style),
                 dbc.CardBody([dcc.Graph(id=ConnectionCardsIDs.tc_by_position, figure={})])],
                 style=tc_by_position_style)], width=6)], className="mb-1 mt-1")]

    return connections_cards_layout


