#!/usr/bin/env python3
# Created By: Tony Tran
# Date: November. 14, 2023
# This is program calculate the power of 2 of of 1 to your number.


import random


def continuous(correct_num):
    user_num = input("Choose a number from 1-10:\n")
    try:
        user_num = int(user_num)
    except ValueError:
        print(f"{user_num} isn't a whole number.")
    else:
        if (user_num >= 1) and (user_num <= 10):
            if correct_num == user_num:
                return "correct"
            else:
                print(f"{user_num} is incorrect!")
                return user_num


def main():
    correct_num = random.randint(1, 10)
    user_num = input("Choose a number from 1-10:\n")
    try:
        user_num = int(user_num)
    except ValueError:
        print(f"{user_num} isn't a whole number.")
    else:
        if (user_num >= 1) and (user_num <= 10):
            if correct_num == user_num:
                print("Your guess was correct!")
            else:
                while True:
                    if continuous(correct_num) == "correct":
                        print("Correct!")
                        break
                    else:
                        print(f"{continuous(correct_num)} is incorrect!")
        else:
            print("Cannot be a number lower than 1 and higher than 10")
    finally:
        print("Thank you for using my code.")


if __name__ == "__main__":
    main()
