"""
{
    "title": "Dashboard Animations Reference",
    "owner": ("Wafa'a Aburub", "wafaa.github@gmail.com"),
    "description": "A collection of Lottie's animations fills the card's headers in the LinkedIn profile dashboard."
}
"""


from dash_extensions import Lottie

# Private URL collections from Lottie-files website (https://lottiefiles.com/).
__connections_url = "https://assets9.lottiefiles.com/packages/lf20_vx7eeu3w.json"
__companies_url = "https://assets7.lottiefiles.com/private_files/lf30_ykaw8ptl.json"

__invites_received_url = "https://assets4.lottiefiles.com/packages/lf20_5ooerq0v.json"
__invites_sent_url = "https://assets9.lottiefiles.com/packages/lf20_YHcKv38T82.json"

__reactions_url = "https://assets6.lottiefiles.com/packages/lf20_o7mksxe9.json"

__messages_num_url = "https://assets3.lottiefiles.com/packages/lf20_KCC53wQ6ky.json"


# Setup Lottie's options.
options = dict(loop=True, autoplay=True, renderSettings=dict(preserveAspectRatio="xMidYMid slice"))


# Reference Lottie's components settings.
connections_lottie = Lottie(options=options, width="80%", height="80%", url=__connections_url)
companies_lottie = Lottie(options=options, width="99%", height="99%", url=__companies_url)

invites_received_lottie = Lottie(options=options, width="80%", height="80%", url=__invites_received_url)
invites_sent_lottie = Lottie(options=options, width="80%", height="80%", url=__invites_sent_url)

reactions_lottie = Lottie(options=options, width="80%", height="80%", url=__reactions_url)

messages_num_lottie = Lottie(options=options, width="109%", height="109%", url=__messages_num_url)


