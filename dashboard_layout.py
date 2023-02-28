"""
{
    "title": "LinkedIn Profile Dashboard Layout",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Creates a personal dashboard layout for the owner's LinkedIn profile."
}
"""

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from ids import *
from styles import *
from animations import *
from dashboard_cleaned_data import start_dt, end_dt


def wireframe_layout(app: Dash, data: dict) -> dbc.Container:
    """Creates the main interface components."""

    layout = dbc.Container(children=[
        # ....First Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardImg(src="assets/linkedin_logo.png")], className='mb-2'),
                     dbc.Card([dbc.CardBody(
                         [dbc.CardLink(data["owner_name"], target="_blank", href=data["owner_linkedin_profile"])])])],
                    width=2),

            # ....Second Column.... #
            dbc.Col([dbc.Card(dbc.CardBody([
                dcc.DatePickerSingle(id=date_picker_start,
                                     min_date_allowed=start_dt,
                                     date=start_dt,
                                     className="date-picker-start"),

                dcc.DatePickerSingle(id=date_picker_end,
                                     max_date_allowed=end_dt,
                                     date=end_dt,
                                     className="date-picker-end")

            ]), color="info", style=date_picker_card_body_style)], width=10)],

            className="mb-2 mt-2"),

        # ....Second Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=connections_lottie),
                dbc.CardBody([html.H6(children="Connections"),
                              html.H2(id=connections_card_header_id, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Second Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=companies_lottie),
                dbc.CardBody([html.H6(children="Companies"),
                              html.H2(id=companies_card_header_id, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Third Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=invites_received_lottie),
                dbc.CardBody([html.H6(children="Invites received"),
                              html.H2(id=invites_received_card_header_id, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Forth Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=invites_sent_lottie),
                dbc.CardBody([html.H6(children="Invites sent"),
                              html.H2(id=invites_sent_card_header_id, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Fifth Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=reactions_lottie),
                dbc.CardBody([html.H6(children="Reactions"),
                              html.H2(id=reactions_card_header_id, children="000")])
            ], style=lottie_cards_style)], width=2),

            # ....Sixth Column.... #
            dbc.Col([dbc.Card([
                dbc.CardHeader(children=messages_num_lottie),
                dbc.CardBody([html.H6(children="Messages #"),
                              html.H2(id=messages_num_card_header_id, children="000")])
            ], style=lottie_cards_style)], width=2)],

            className="mb-2"
        ),

        # ....Third Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=tc_by_month_id, figure={})])], style=graph_cards_style)], width=6),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=tc_by_company_id, figure={})])], style=graph_cards_style)], width=6)],

            className="mb-2 mt-3"),

        # ....Forth Row.... #
        dbc.Row([
            # ....First Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=tc_by_position_id, figure={})])], style=graph_cards_style)], width=4),

            # ....Second Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=msr_id, figure={})])], style=graph_cards_style)], width=4),

            # ....Third Column.... #
            dbc.Col([dbc.Card([dbc.CardBody([dcc.Graph(id=msr_by_month_id, figure={})])], style=graph_cards_style)], width=4)],

            className="mb-2 mt-3")
    ], fluid=True)

    return layout


