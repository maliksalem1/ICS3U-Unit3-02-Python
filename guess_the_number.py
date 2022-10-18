#!/usr/bin/env python3

# Created by: Kyanh Pham
# Created on: Oct 2022
# This program sees if you guess the right number

import constants


def main():
    # This function sees if you guessed right or wrong

    # Input
    guessed_number = int(input("Enter the number between 0-9: "))
    print("")

    # Process and Output
    if guessed_number == constants.CORRECT_NUMBER:
        print("You guessed right.")
    if guessed_number != constants.CORRECT_NUMBER:
        print("You guessed wrong.")

    print("\nDone.")


if __name__ == "__main__":
    main()
