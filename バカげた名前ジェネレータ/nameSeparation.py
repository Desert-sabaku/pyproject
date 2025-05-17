import re

text = """
        "Baby Oil",
        "Bad News",
        "Big Burps",
        "Bill",
        "Bob 'Stinkbug'",
        "Bowel Noises",
        "Boxelder",
        "Bud 'Lite'",
        "Butterbean",
        "Buttermilk",
        "Buttocks",
        "Chad",
        "Chesterfield",
        "Chewy",
        "Chigger",
        "Cinnabuns",
        "Cleet",
        "Cornbread",
        "Crab Meat",
        "Crapps",
        "Dark Skies",
        "Dennis Clawhammer",
        "Dicman",
        "Elphonso",
        "Fancypants",
        "Figgs",
        "Foncy",
        "Gootsy",
        "Greasy Jim",
        "Huckleberry",
        "Huggy",
        "Ignatious",
        "Jimbo",
        "Joe 'Pottin Soil'",
        "Johnny",
        "Lemongrass",
        "Lil Debil",
        "Longbranch",
        '"Lunch Money"',
        "Mergatroid",
        '"Mr Peabody"',
        "Oil-Can",
        "Oinks",
        "Old Scratch",
        "Ovaltine",
        "Pennywhistle",
        "Pitchfork Ben",
        "Potato Bug",
        "Pushmeet",
        "Rock Candy",
        "Schlomo",
        "Scratchensniff",
        "Scut",
        "Sid 'The Squirts'",
        "Skidmark",
        "Slaps",
        "Snakes",
        "Snoobs",
        "Snorki",
        "Soupcan Sam",
        "Spitzitout",
        "Squids",
        "Stinky",
        "Storyboard",
        "Sweet Tea",
        "TeeTee",
        "Wheezy Joe",
        "Winston 'Jazz Hands'",
        "Worms",
    )
"""


def split_names_into_arrays(text: str) -> tuple[list[str], list[str]]:
    names = re.findall(r'"([^"]*)"', text)
    first_names: list[str] = []
    nicknames: list[str] = []
    for name in names:
        if " " in name:
            parts = name.split(" ")
            first_name = parts[0]
            nickname = " ".join(parts[1:]).strip("'")
            first_names.append(first_name)
            nicknames.append(nickname)
        else:
            first_names.append(name)
    return first_names, nicknames


first_names, nicknames = split_names_into_arrays(text)

print("First Names:", first_names)
print("Nicknames/Other Parts:", nicknames)
