"""
{
    "title": "LinkedIn's Profile General Key Measures",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Calculates main keys; represent your activities on LinkedIn."
}
"""


from datetime import date
from dash import Dash, html
from components.styles import *
from components.animations import *
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from components.ids import SummaryCardsIDs, DatePickerIDs


def render(app: Dash, data: dict) -> list:
    """
    Renders the summary cards and gathers the filtration selections associated with the
    user's interactions to calculate summary information within a specific date range.
    """

    @app.callback(
        Output(SummaryCardsIDs.connections, "children"),
        Output(SummaryCardsIDs.companies, "children"),
        Output(SummaryCardsIDs.invites_received, "children"),
        Output(SummaryCardsIDs.invites_sent, "children"),
        Output(SummaryCardsIDs.reactions, "children"),
        Output(SummaryCardsIDs.messages_num, "children"),
        Input(DatePickerIDs.start, "date"),
        Input(DatePickerIDs.end, "date"))
    def update_summary_cards(start_dt: date, end_dt: date):
        """Updates the numbers within the summary cards."""

        c_df = data["connections"].query("@start_dt <= connected_on <= @end_dt").reset_index(drop=True)
        i_df = data["invitations"].query("@start_dt <= sent_at <= @end_dt").reset_index(drop=True)
        r_df = data["reactions"].query("@start_dt <= date <= @end_dt").reset_index(drop=True)
        m_df = data["messages"].query("@start_dt <= date <= @end_dt").reset_index(drop=True)

        # Initialization!
        con_num, comp_num, inv_in_num, inv_out_num, react_num, msg_num = 6 * [0]

        if not c_df.empty:  # Connections & Companies Cards
            con_num = len(c_df)
            comp_num = c_df.company.nunique()

        if not i_df.empty:  # Invitation Cards
            inv_in_out_nums = i_df.groupby("direction")["direction"].count()
            inv_in_num = inv_in_out_nums.INCOMING
            inv_out_num = inv_in_out_nums.OUTGOING

        if not r_df.empty:  # Reactions Card
            react_num = len(r_df)

        if not m_df.empty:  # Messages Card
            msg_num = m_df.conversation_id.nunique()

        return con_num, comp_num, inv_in_num, inv_out_num, react_num, msg_num

    summary_cards_layout = [
        # ....First Column.... #
        dbc.Col([dbc.Card([dbc.CardHeader(connections_lottie), dbc.CardBody([html.H6("Connections"), html.H2(id=SummaryCardsIDs.connections, children="000")])], style=lottie_cards_style)], width=2),
        # ....Second Column.... #
        dbc.Col([dbc.Card([dbc.CardHeader(companies_lottie), dbc.CardBody([html.H6("Companies"), html.H2(id=SummaryCardsIDs.companies, children="000")])], style=lottie_cards_style)], width=2),
        # ....Third Column.... #
        dbc.Col([dbc.Card([dbc.CardHeader(invites_received_lottie), dbc.CardBody([html.H6("Invites received"), html.H2(id=SummaryCardsIDs.invites_received, children="000")])], style=lottie_cards_style)], width=2),
        # ....Forth Column.... #
        dbc.Col([dbc.Card([dbc.CardHeader(invites_sent_lottie), dbc.CardBody([html.H6("Invites sent"), html.H2(id=SummaryCardsIDs.invites_sent, children="000")])], style=lottie_cards_style)], width=2),
        # ....Fifth Column.... #
        dbc.Col([dbc.Card([dbc.CardHeader(reactions_lottie), dbc.CardBody([html.H6("Reactions"), html.H2(id=SummaryCardsIDs.reactions, children="000")])], style=lottie_cards_style)], width=2),
        # ....Sixth Column.... #
        dbc.Col([dbc.Card([dbc.CardHeader(messages_num_lottie), dbc.CardBody([html.H6("Messages #"), html.H2(id=SummaryCardsIDs.messages_num, children="000")])], style=lottie_cards_style)], width=2)]

    return summary_cards_layout


