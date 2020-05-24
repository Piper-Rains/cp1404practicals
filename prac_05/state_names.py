"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_NAMES)

for i, j in STATE_NAMES.items():
    print("{0:<3} is {1}".format(i, j))

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_NAMES:
        print(state_code, "is", STATE_NAMES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

