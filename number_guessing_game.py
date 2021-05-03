#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program checks if guessed number is correct or incorrect


def main():
    # this function checks if guessed number is correct or incorrect

    # input
    print("Can you guess the number I choose from 0 to 9?")
    guessed_number = int(input("Enter the guessed number: "))
    print("")

    # process & output
    if guessed_number == 5:
        print("Correct!")
    else:
        print("Incorrect, the number was 5.")


if __name__ == "__main__":
    main()
