"""
{
    "title": "LinkedIn Profile Dashboard Layout",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Creates a personal dashboard layout for the owner's LinkedIn profile."
}
"""


from dash import Dash
import dash_bootstrap_components as dbc
from components.styles import layout_container_style
from components import sidebar, header_cards, summary_cards, connections_cards, messages_cards


def wireframe_layout(app: Dash, data: dict) -> dbc.Container:
    """Creates the main interface components."""

    layout = dbc.Container(children=[

        dbc.Container(children=[
            dbc.Row(summary_cards.render(app, data), className="mb-1 mt-3"),
            dbc.Row(connections_cards.render(app, data["connections"]), className="mb-1 mt-1", ),
            dbc.Row(messages_cards.render(app, data['owner_name'], data["messages"]), className="mb-1 mt-1")], style=layout_container_style),

        header_cards.render(data["owner_name"], data["owner_linkedin_profile"], data["start_init_dt"], data["end_init_dt"]),

        sidebar.render(data["owner_name"], data["owner_linkedin_profile"], data["owner_geo_location"], data["owner_profile_headline"])])

    return layout


