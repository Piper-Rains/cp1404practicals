"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():

    score = float(input("Enter score: "))

    print(determine_score_status(score))


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


score = random.randint(0, 100)
print(score)
print(determine_score_status(score))

main()
