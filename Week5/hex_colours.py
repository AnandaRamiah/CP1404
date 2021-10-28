COLOUR_CODES = {"Amaranth": "#e52b50", "Aquamarine2": "#76eec6",
                "Barn Red": "#7c0a02", "Bittersweet": "#fe6f5e",
                "Black Coffee": "#3b2f2f", "Boysenberry": "#873260",
                "Brilliant Rose": "#ff55a3", "Carolina Blue": "#56a0d3",
                "Cedar Chest": "#c95a49", "Celadon": "#ace1af",
                "Champagne": "#f7e7ce", "Dark Byzantium": "#5d3954"}

colour = input("Enter a colour: ").title()
while colour != "":
    print("The code for {} is {}".format(colour,
                                             COLOUR_CODES.get(colour)))
    colour = input("Enter a colour: ")