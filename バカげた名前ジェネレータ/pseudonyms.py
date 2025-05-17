import random
import sys


def main():
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")

    print("A name just like Sean would pick for Gus:\n\n")

    first: tuple[str, ...] = (
        "Bill",
        "Chad",
        "Cleet",
        "Elphonso",
        "Ignatious",
        "Johnny",
        "Schlomo",
    )

    middle: tuple[str, ...] = (
        "Baby Oil",
        "Bad News",
        "Big Burps",
        "Bob 'Stinkbug'",
        "Bowel Noises",
        "Boxelder",
        "Bud 'Lite'",
        "Butterbean",
        "Buttermilk",
        "Buttocks",
        "Chesterfield",
        "Chewy",
        "Chigger",
        "Cinnabuns",
        "Cornbread",
        "Crab Meat",
        "Crapps",
        "Dark Skies",
        "Dennis Clawhammer",
        "Dicman",
        "Fancypants",
        "Figgs",
        "Foncy",
        "Gootsy",
        "Greasy Jim",
        "Huckleberry",
        "Huggy",
        "Jimbo",
        "Joe 'Pottin Soil'",
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

    last: tuple[str, ...] = (
        "Appleyard",
        "Bigmeat",
        "Bloominshine",
        "Boogerbottom",
        "Breedslovetrout",
        "Butterbaugh",
        "Clovenhoof",
        "Clutterbuck",
        "Cocktoasten",
        "Endicott",
        "Fewhairs",
        "Gooberdapple",
        "Goodensmith",
        "Goodpasture",
        "Guster",
        "Henderson",
        "Hooperbag",
        "Hoosenater",
        "Hootkins",
        "Jefferson",
        "Jenkins",
        "Jingley-Schmidt",
        "Johnson",
        "Kingfish",
        "Listenbee",
        "M'Bembo",
        "McFadden",
        "Moonshine",
        "Nettles",
        "Noseworthy",
        "Olivetti",
        "Outerbridge",
        "Overpeck",
        "Overturf",
        "Oxhandler",
        "Pealike",
        "Pennywhistle",
        "Peterson",
        "Pieplow",
        "Pinkerton",
        "Porkins",
        "Putney",
        "Quakenbush",
        "Rainwater",
        "Rosenthal",
        "Rubbins",
        "Sackrider",
        "Snuggleshine",
        "Splern",
        "Stevens",
        "Stroganoff",
        "Sugar-Gold",
        "Swackhamer",
        "Tippins",
        "Turnipseed",
        "Vinaigrette",
        "Walkingstick",
        "Wallbanger",
        "Weewax",
        "Weiners",
        "Whipkey",
        "Wigglesworth",
        "Wimplesnatch",
        "Winterkorn",
        "Woolysocks",
    )

    while True:
        firstName = random.choice(first)
        lastName = random.choice(last)
        if random.randint(0, 1) == 1:
            firstName = f"{firstName} '{random.choice(middle)}'"

        print("\n\n")
        print(firstName, lastName, file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
