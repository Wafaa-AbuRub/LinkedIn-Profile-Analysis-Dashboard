"""
{
    "title": "LinkedIn Profile Dashboard Interface",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Creates a dashboard interface for the owner's LinkedIn profile with Dash."
}
"""


# Import the necessary libraries
from dash import Dash
import dash_bootstrap_components as dbc
from components.layout import wireframe_layout
from data.data_loader import loader


def linkedin_dashboard_app() -> None:
    """It creates an interactive web application to present LinkedIn profile data."""

    # Initialize the app
    app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
    app.title = "My LinkedIn Profile Dashboard"

    dashboard_data = loader()

    app.layout = wireframe_layout(app, dashboard_data)

    app.run()


if __name__ == "__main__":
    linkedin_dashboard_app()


