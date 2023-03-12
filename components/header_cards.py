"""
{
    "title": "Header Cards Components & Layouts",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Collection of layouts and components at the top of the dashboard interface."
}
"""


from dash import dcc
from datetime import date
import dash_bootstrap_components as dbc
from components.ids import DatePickerIDs
from components.styles import date_picker_card_body_style


def render(owner_name: str, linkedin_profile: str, start_dt: date, end_dt: date) -> list:
    """
    Adds a layout to the dashboard interface header.
    """

    header_cards_layout = [
        # ....First Column.... #
        dbc.Col([dbc.Card([dbc.CardImg(src="../assets/linkedin_logo.png")], className='mb-2'),
                 dbc.Card([dbc.CardBody(
                     [dbc.CardLink(owner_name, target="_blank", href=linkedin_profile)])])],
                width=2),

        # ....Second Column.... #
        dbc.Col([dbc.Card(dbc.CardBody([
            dcc.DatePickerSingle(id=DatePickerIDs.start,
                                 min_date_allowed=start_dt,
                                 date=start_dt,
                                 className="date-picker-start"),

            dcc.DatePickerSingle(id=DatePickerIDs.end,
                                 max_date_allowed=end_dt,
                                 date=end_dt,
                                 className="date-picker-end")

        ]), color="info", style=date_picker_card_body_style)], width=10)]

    return header_cards_layout


