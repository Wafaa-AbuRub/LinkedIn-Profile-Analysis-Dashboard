"""
{
    "title": "Sidebar Layout",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Collection of dash components; create the dashboard sidebar."
}
"""


from dash import html
from datetime import date
from components.styles import sidebar_style, linkedin_logo_style, text_style, job_title_img_style, \
    profile_headline_style, signup_img_style, registration_date_style


def render(owner_name: str, profile_link: str, geo_loc: str, profile_headline: str, registration_date: date) -> html.Div:
    """
    Adds a layout to the dashboard interface sidebar.
    """

    sidebar = html.Div(
        [
            html.Img(src="../assets/linkedin_logo.png", width="200", height="50", style=linkedin_logo_style),
            html.Hr(),

            html.A(children=owner_name, href=profile_link, target="_blank", className="lead", style=text_style),
            html.P(geo_loc, style=text_style),

            html.Div([html.Img(src="../assets/job_title_img.png", width="32", height="32", style=job_title_img_style),
                      html.P(profile_headline, style=profile_headline_style)]),

            html.Div([html.Img(src="../assets/signup_img.png", width="40", height="40", style=signup_img_style),
                      html.P("Registration Date\n {}".format(registration_date, profile_link), style=registration_date_style)])],

        style=sidebar_style)

    return sidebar


