"""
{
    "title": "Header Cards Components & Layouts",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Collection of layouts and components at the top of the dashboard interface."
}
"""


from datetime import date
from dash import dcc, html
from components.ids import DatePickerIDs
from components.styles import header_style, date_picker_card_style, date_picker_div_style, avatar_img_style, avatar_text_style, avatar_div_style


def render(owner_first_name: str, start_dt: date, end_dt: date) -> html.Header:
    """
    Adds a layout to the dashboard interface header.
    """

    header_cards_layout = html.Header([
        html.Div([html.Img(src="../assets/avatar_img.png", height=50, width=50, style=avatar_img_style),
                  html.P("Hi, {}!".format(owner_first_name), style=avatar_text_style)], style=avatar_div_style),

        html.Div(dcc.DatePickerRange(id=DatePickerIDs.range,
                                     min_date_allowed=start_dt,
                                     max_date_allowed=end_dt,
                                     start_date=start_dt,
                                     end_date=end_dt,
                                     # className="date-picker-range",
                                     style=date_picker_card_style), style=date_picker_div_style)
    ], style=header_style)

    return header_cards_layout


