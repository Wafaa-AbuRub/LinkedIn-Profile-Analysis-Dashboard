"""
{
    "title": "Dashboard Data Cleaning & Preparation",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Loads, cleans LinkedIn data and prepares it for the dashboard."
}
"""


import pandas as pd


def loader() -> dict:
    """Loads LinkedIn's data & applies the necessary cleaning!"""

    # Import your LinkedIn files
    profile_df = pd.read_csv("data/profile.csv")
    messages_df = pd.read_csv("data/messages.csv")
    reactions_df = pd.read_csv("data/reactions.csv")
    invitations_df = pd.read_csv("data/invitations.csv")
    connections_df = pd.read_csv("data/connections.csv")

    # Convert data-frame columns names to a standard naming format (all small letters with _ between words)
    data_dfs_list = [profile_df, messages_df, reactions_df, invitations_df, connections_df]
    for df in data_dfs_list:
        for col_name in df.columns:
            df.rename(columns={col_name: col_name.lower().replace(" ", "_")}, inplace=True)

    # Personal Intro
    owner_name = r"{} {}".format(profile_df["first_name"].iloc[0], profile_df["last_name"].iloc[0])
    owner_linkedin_profile = messages_df[messages_df["from"] == owner_name]["sender_profile_url"].unique()[0]

    # Convert date columns to datatime objects
    messages_df["date"] = pd.to_datetime(messages_df["date"])
    reactions_df["date"] = pd.to_datetime(reactions_df["date"])
    invitations_df["sent_at"] = pd.to_datetime(invitations_df["sent_at"])
    connections_df["connected_on"] = pd.to_datetime(connections_df["connected_on"])

    # Extract months
    connections_df = connections_df.assign(month=connections_df["connected_on"].dt.strftime("%b"))
    messages_df = messages_df.assign(month=messages_df["date"].dt.strftime("%b"))

    # Date-range picker start and end dates
    start_init_dt = connections_df.connected_on.min().date()  # First connection date
    end_init_dt = connections_df.connected_on.max().date()  # Last connection date

    # Combine dashboard data into one dictionary
    dashboard_data = {
        "start_init_dt": start_init_dt,
        "end_init_dt": end_init_dt,

        "owner_name": owner_name,
        "owner_linkedin_profile": owner_linkedin_profile,

        "profile": profile_df,
        "messages": messages_df,
        "reactions": reactions_df,
        "invitations": invitations_df,
        "connections": connections_df
    }

    return dashboard_data


