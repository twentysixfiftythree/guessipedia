from .data_fetch import fetch_wikipedia_page_details
from .database_interaction import add_wikipedia_pages

'''
[
        'https://en.wikipedia.org/wiki/Boston_Bruins',
        'https://en.wikipedia.org/wiki/Chicago_Blackhawks',
        'https://en.wikipedia.org/wiki/Detroit_Red_Wings',
        'https://en.wikipedia.org/wiki/Montreal_Canadiens',
        'https://en.wikipedia.org/wiki/New_York_Rangers',
        'https://en.wikipedia.org/wiki/Toronto_Maple_Leafs',
        'https://en.wikipedia.org/wiki/Vancouver_Canucks',
        'https://en.wikipedia.org/wiki/Edmonton_Oilers',
        'https://en.wikipedia.org/wiki/Calgary_Flames',
        'https://en.wikipedia.org/wiki/Quebec_Nordiques',
        'https://en.wikipedia.org/wiki/Winnipeg_Jets_(1972–1996)',
        'https://en.wikipedia.org/wiki/Ottawa_Senators',
        'https://en.wikipedia.org/wiki/Florida_Panthers',
        'https://en.wikipedia.org/wiki/Tampa_Bay_Lightning',
        'https://en.wikipedia.org/wiki/Carolina_Hurricanes',
        'https://en.wikipedia.org/wiki/Washington_Capitals',
        'https://en.wikipedia.org/wiki/Philadelphia_Flyers',
        'https://en.wikipedia.org/wiki/Pittsburgh_Penguins',
        'https://en.wikipedia.org/wiki/New_Jersey_Devils',
        'https://en.wikipedia.org/wiki/New_York_Islanders',
        'https://en.wikipedia.org/wiki/Buffalo_Sabres',
        'https://en.wikipedia.org/wiki/Minnesota_Wild',
        'https://en.wikipedia.org/wiki/Colorado_Avalanche',
        'https://en.wikipedia.org/wiki/Dallas_Stars',
        'https://en.wikipedia.org/wiki/St._Louis_Blues',
        'https://en.wikipedia.org/wiki/Nashville_Predators',
        'https://en.wikipedia.org/wiki/Arizona_Coyotes',
        'https://en.wikipedia.org/wiki/Anaheim_Ducks',
        'https://en.wikipedia.org/wiki/Los_Angeles_Kings',
        'https://en.wikipedia.org/wiki/San_Jose_Sharks',
        'https://en.wikipedia.org/wiki/Vegas_Golden_Knights',
    ]
        'https://en.wikipedia.org/wiki/Canada',
        'https://en.wikipedia.org/wiki/Ontario',
        'https://en.wikipedia.org/wiki/United_States',
        'https://en.wikipedia.org/wiki/Portugal',
        'https://en.wikipedia.org/wiki/Mexico',
        'https://en.wikipedia.org/wiki/Kazakhstan',
        'https://en.wikipedia.org/wiki/Ukraine',
        'https://en.wikipedia.org/wiki/Australia',
        'https://en.wikipedia.org/wiki/New_Zealand',
        'https://en.wikipedia.org/wiki/Spain',
        'https://en.wikipedia.org/wiki/Italy',
        'https://en.wikipedia.org/wiki/India',
        'https://en.wikipedia.org/wiki/China',
        'https://en.wikipedia.org/wiki/Japan',
        'https://en.wikipedia.org/wiki/South_Korea',
        'https://en.wikipedia.org/wiki/Indonesia',
        'https://en.wikipedia.org/wiki/Singapore',
        'https://en.wikipedia.org/wiki/Ireland',
    ]
    

    [
        'https://en.wikipedia.org/wiki/Up_(2009_film)',
        'https://en.wikipedia.org/wiki/Moana_(2016_film)',
        'https://en.wikipedia.org/wiki/101_Dalmatians_(1996_film)',
        'https://en.wikipedia.org/wiki/Cinderella_(1950_film)',
        'https://en.wikipedia.org/wiki/Snow_White_and_the_Seven_Dwarfs_(1937_film)',
        'https://en.wikipedia.org/wiki/Frozen_(2013_film)',
        'https://en.wikipedia.org/wiki/Frozen_II',
        'https://en.wikipedia.org/wiki/Aladdin_(1992_Disney_film)',
        'https://en.wikipedia.org/wiki/Sleeping_Beauty_(1959_film)',
        'https://en.wikipedia.org/wiki/Beauty_and_the_Beast_(1991_film)',
        'https://en.wikipedia.org/wiki/Lilo_%26_Stitch',
        'https://en.wikipedia.org/wiki/Shrek',
        'https://en.wikipedia.org/wiki/The_Parent_Trap_(1998_film)',
        'https://en.wikipedia.org/wiki/The_Little_Mermaid_(1989_film)',
        'https://en.wikipedia.org/wiki/Cars_(film)',
        'https://en.wikipedia.org/wiki/Monsters,_Inc.',
        'https://en.wikipedia.org/wiki/Alice_in_Wonderland_(1951_film)',
        'https://en.wikipedia.org/wiki/Finding_Nemo',
    ]'''


def run():
    urls = [
        'https://en.wikipedia.org/wiki/Canada',
        'https://en.wikipedia.org/wiki/Ontario',
        'https://en.wikipedia.org/wiki/United_States',
        'https://en.wikipedia.org/wiki/Portugal',
        'https://en.wikipedia.org/wiki/Mexico',
        'https://en.wikipedia.org/wiki/Kazakhstan',
        'https://en.wikipedia.org/wiki/Ukraine',
        'https://en.wikipedia.org/wiki/Australia',
        'https://en.wikipedia.org/wiki/New_Zealand',
        'https://en.wikipedia.org/wiki/Spain',
        'https://en.wikipedia.org/wiki/Italy',
        'https://en.wikipedia.org/wiki/India',
        'https://en.wikipedia.org/wiki/China',
        'https://en.wikipedia.org/wiki/Japan',
        'https://en.wikipedia.org/wiki/South_Korea',
        'https://en.wikipedia.org/wiki/Indonesia',
        'https://en.wikipedia.org/wiki/Singapore',
        'https://en.wikipedia.org/wiki/Ireland',
    ]

    # Example URLs
    for url in urls:
        page_data = fetch_wikipedia_page_details(url)
        add_wikipedia_pages(page_data)
