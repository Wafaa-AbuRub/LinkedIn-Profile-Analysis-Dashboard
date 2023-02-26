"""
{
    "title": "LinkedIn Profile Dashboard Interface",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Creates a dashboard interface for the owner's LinkedIn profile with Dash."
}
"""


# Import the necessary libraries
from dash import Dash, html
import dash_bootstrap_components as dbc
from dashboard_layout import wireframe_layout
from dashboard_cleaned_data import profile_owner_data


def linkedin_dashboard_app() -> None:
    """It creates an interactive web application to present LinkedIn profile data."""

    # Initialize the app
    app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
    app.title = "My LinkedIn Profile Dashboard"

    app.layout = wireframe_layout(app, profile_owner_data)

    app.run()


if __name__ == "__main__":
    linkedin_dashboard_app()


