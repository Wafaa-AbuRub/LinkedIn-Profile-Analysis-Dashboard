"""
{
    "title": "LinkedIn Profile Dashboard Layout",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Creates a personal dashboard layout for the owner's LinkedIn profile."
}
"""


from dash import Dash
import dash_bootstrap_components as dbc
from components import header_cards, summary_cards, connections_cards, messages_cards


def wireframe_layout(app: Dash, data: dict) -> dbc.Container:
    """Creates the main interface components."""

    layout = dbc.Container(children=[
        # ....First Row.... #
        dbc.Row(header_cards.render(data["owner_name"], data["owner_linkedin_profile"], data["start_init_dt"], data["end_init_dt"]), className="mb-2 mt-2"),

        # ....Second Row.... #
        dbc.Row(summary_cards.render(app, data), className="mb-2"),

        # ....Third Row.... #
        dbc.Row(connections_cards.render(app, data["connections"]), className="mb-2 mt-3"),

        # ....Forth Row.... #
        dbc.Row(messages_cards.render(app, data['owner_name'], data["messages"]), className="mb-2 mt-3")],

        fluid=True)

    return layout


