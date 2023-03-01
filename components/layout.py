"""
{
    "title": "LinkedIn Profile Dashboard Layout",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Creates a personal dashboard layout for the owner's LinkedIn profile."
}
"""

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from components.ids import *
from components.styles import *
from components.animations import *


def wireframe_layout(app: Dash, data: dict) -> dbc.Container:
    """Creates the main interface components."""

    layout = dbc.Container(children=[
        # ....First Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardImg(src="../assets/linkedin_logo.png")], className='mb-2'),
                     dbc.Card([dbc.CardBody(
                         [dbc.CardLink(data["owner_name"], target="_blank", href=data["owner_linkedin_profile"])])])],
                    width=2),

            # ....Second Column.... #
            dbc.Col([dbc.Card(dbc.CardBody([
                dcc.DatePickerSingle(id=DatePickerIDs.start,
                                     min_date_allowed=data["start_init_dt"],
                                     date=data["start_init_dt"],
                                     className="date-picker-start"),

                dcc.DatePickerSingle(id=DatePickerIDs.end,
                                     max_date_allowed=data["end_init_dt"],
                                     date=data["end_init_dt"],
                                     className="date-picker-end")

            ]), color="info", style=date_picker_card_body_style)], width=10)],

            className="mb-2 mt-2"),

        # ....Second Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=connections_lottie),
                dbc.CardBody([html.H6(children="Connections"),
                              html.H2(id=SummaryCardsIDs.connections, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Second Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=companies_lottie),
                dbc.CardBody([html.H6(children="Companies"),
                              html.H2(id=SummaryCardsIDs.companies, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Third Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=invites_received_lottie),
                dbc.CardBody([html.H6(children="Invites received"),
                              html.H2(id=SummaryCardsIDs.invites_received, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Forth Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=invites_sent_lottie),
                dbc.CardBody([html.H6(children="Invites sent"),
                              html.H2(id=SummaryCardsIDs.invites_sent, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Fifth Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=reactions_lottie),
                dbc.CardBody([html.H6(children="Reactions"),
                              html.H2(id=SummaryCardsIDs.reactions, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Sixth Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=messages_num_lottie),
                dbc.CardBody([html.H6(children="Messages #"),
                              html.H2(id=SummaryCardsIDs.messages_num, children="000")])
            ], style=lottie_cards_style)], width=2)],

            className="mb-2"
        ),

        # ....Third Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=GraphCardsIDs.tc_by_month, figure={})])], style=graph_cards_style)], width=6),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=GraphCardsIDs.tc_by_company, figure={})])], style=graph_cards_style)], width=6)],

            className="mb-2 mt-3"),

        # ....Forth Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=GraphCardsIDs.tc_by_position, figure={})])], style=graph_cards_style)], width=4),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=GraphCardsIDs.msr, figure={})])], style=graph_cards_style)], width=4),

            # ....Third Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=GraphCardsIDs.msr_by_month, figure={})])], style=graph_cards_style)], width=4)],

            className="mb-2 mt-3")
    ], fluid=True)

    return layout


