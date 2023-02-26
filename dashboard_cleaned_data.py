"""
{
    "title": "Dashboard Data Cleaning & Preparation",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "Cleans LinkedIn data and prepares it for the dashboard."
}
"""


import pandas as pd


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


# Personal Into
owner_name = r"{} {}".format(profile_df["first_name"].iloc[0], profile_df["last_name"].iloc[0])
owner_linkedin_profile = messages_df[messages_df["from"] == owner_name]["sender_profile_url"].unique()[0]
profile_owner_data = {"owner_name": owner_name, "owner_linkedin_profile": owner_linkedin_profile}


# Convert date columns to datatime objects
messages_df["date"] = pd.to_datetime(messages_df["date"])
reactions_df["date"] = pd.to_datetime(reactions_df["date"])
invitations_df["sent_at"] = pd.to_datetime(invitations_df["sent_at"])
connections_df["connected_on"] = pd.to_datetime(connections_df["connected_on"])


# Extract months
connections_df = connections_df.assign(month=connections_df["connected_on"].dt.strftime("%b"))


