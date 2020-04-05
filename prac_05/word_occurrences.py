
COLOUR_CODES = {"RoyalBlue": "#4169e1", "SkyBlue": "#87ceeb", "SlateBlue": "#6a5acd", "SlateGray1": "#c6e2ff",
                "SpringGreen1": "#00ff7f", "thistle": "#d8bfd8", "tomato1": "#ff6347", "turquoise3": "#00c5cd",
                "violet": "#ee82ee", "black": "#000000"}
print(COLOUR_CODES)

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(colour_name, "has code:", COLOUR_CODES[colour_name])
    else:
        print("Invalid colour name entered")
    colour_name = input("Enter colour name: ")
