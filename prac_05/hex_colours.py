
COLOUR_CODES = {"royalblue": "#4169e1", "skyblue": "#87ceeb", "slateblue": "#6a5acd", "slategray1": "#c6e2ff",
                "springgreen1": "#00ff7f", "thistle": "#d8bfd8", "tomato1": "#ff6347", "turquoise3": "#00c5cd",
                "violet": "#ee82ee", "black": "#000000"}
print(COLOUR_CODES)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(colour_name, "has code:", COLOUR_CODES[colour_name])
    else:
        print("Invalid colour name entered")
    colour_name = input("Enter colour name: ").lower()
