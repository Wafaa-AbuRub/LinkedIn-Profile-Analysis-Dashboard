"""
{
    "title": "Header Cards Components & Layouts",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Collection of layouts and components at the top of the dashboard interface."
}
"""

from dash import dcc, html
from datetime import date
from components.ids import DatePickerIDs
from components.styles import header_card_style, date_picker_card_style


def render(owner_name: str, linkedin_profile: str, start_dt: date, end_dt: date) -> html.Header:
    """
    Adds a layout to the dashboard interface header.
    """

    header_cards_layout = html.Header(
        dcc.DatePickerRange(id=DatePickerIDs.range,
                            min_date_allowed=start_dt,
                            max_date_allowed=end_dt,
                            start_date=start_dt,
                            end_date=end_dt,
                            # className="date-picker-range",
                            style=date_picker_card_style),
        style=header_card_style)

    return header_cards_layout


