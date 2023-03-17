"""
{
    "title": "Sidebar Layout",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Collection of dash components; create the dashboard sidebar."
}
"""


from dash import html
from components.styles import sidebar_style


def render(owner_name: str, profile_link: str, geo_loc: str, profile_headline: str) -> html.Div:
    """
    Adds a layout to the dashboard interface sidebar.
    """

    sidebar = html.Div(
        [
            html.Img(src="../assets/linkedin_logo.png", width="180", height="50"),
            html.Hr(),
            html.A(children=owner_name, href=profile_link, target="_blank", className="lead"),
            html.P(geo_loc),
            html.P(profile_headline)
        ],
        style=sidebar_style,
    )

    return sidebar


