import random
import time

play = 0
wrong = 0

print("~ HANGMAN ~")

time.sleep(1)

print("RULES:")
print("- A random word will be chosen at random in the chosen category")
print("- If you fail 10 guesses, you lose!")
print("- If you guess the word under 10 mistakes, you win!")

time.sleep(3)
print("\nLet's play!")
time.sleep(1)

while True:
    print("\nPICK A CATEGORY:")
    print("Enter 1 for Food")
    print("Enter 2 for Sports")
    print("Enter 3 for Clothing")
    print("Enter 4 for School Subjects")
    print("Enter 5 for Technology & Computer Studies")
    category = input(">> ")

    while True:
        if category == "1":
            words = ["doughnut", "mozzarella", "zucchini", "hamburger", "poutine", "macaroni", "spaghetti"]
            chosen_word = random.choice(words).lower()
            char = len(chosen_word)
            time.sleep(1)
            break

        elif category == "2":
            words = ["hockey", "lacrosse", "badminton", "volleyball", "cricket", "ringette", "softball", "baseball", "basketball", "snorkeling", "running"]
            chosen_word = random.choice(words).lower()
            char = len(chosen_word)
            time.sleep(1)
            break

        elif category == "3":
            words = ["sweatshirt", "sweatpants", "sweater", "jacket", "cardigan", "docks", "shirt", "earmuffs", "flannel", "skirt"]
            chosen_word = random.choice(words).lower()
            char = len(chosen_word)
            time.sleep(1)
            break

        elif category == "4":
            words = ["biology", "physics", "chemistry", "business", "philosophy", "calculus", "accounting", "english"]
            chosen_word = random.choice(words).lower()
            char = len(chosen_word)
            time.sleep(1)
            break

        elif category == "5":
            words = ["iphone", "laptop", "airpods", "desktop", "television", "headphones", "monitor", "computer", "motherboard", "mouse", "keyboard"]
            chosen_word = random.choice(words).lower()
            char = len(chosen_word)
            time.sleep(1)
            break

        else:
            print("invalid input\n")
            category = input("Please try again\n>> ")

    print("\nStart guessing...")
    guesses = ''
    turns = 10

    while turns > 0:
        time.sleep(0.5)
        failed = 0

        for char in chosen_word:
            if char in guesses:
                print(char, end=" ")

            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\n\n--YOU WON--")
            break
        guess = input("\n>> ")
        guesses += guess

        if guess not in chosen_word:
            turns -= 1
            wrong += 1

            if turns == 9:
                print("-----\n|   |\n|   0\n|\n|\n|\n|\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 8:
                print("-----\n|   |\n|   0\n|  -+-\n|\n|\n|\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 7:
                print("-----\n|   |\n|   0\n| /-+-\n|\n|\n|\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 6:
                print("-----\n|   |\n|   0\n| /-+-\ \n|\n|\n|\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 5:
                print("-----\n|   |\n|   0\n| /-+-\ \n|   | \n|\n|\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 4:
                print("-----\n|   |\n|   0\n| /-+-\ \n|   | \n|   |\n|\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 3:
                print("-----\n|   |\n|   0\n| /-+-\ \n|   |  \n|   |\n|  |\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 2:
                print("-----\n|   |\n|   0\n| /-+-\ \n|   |  \n|   |\n|  | |\n|\n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 1:
                print("-----\n|   |\n|   0\n| /-+-\ \n|   | \n|   |\n|  | |\n|  | \n|\n--------")
                print("You have", + turns, 'more guesses')

            elif turns == 0:
                print("-----\n|   |\n|   0\n| /-+-\ \n|   | \n|   |\n|  | |\n|  | |\n|\n--------")
                print("\nYOU LOOSE\n" + chosen_word, "was the word")
                break

    play += 1

    time.sleep(1)
    print("\nPlay Again?\nEnter y for yes\nEnter n for no")
    again = input(">> ")

    while True:
        if again == "y":
            time.sleep(1)
            break

        elif again == "n":
            time.sleep(0.5)
            print("\n--STATS--")
            print("Times played:", play)
            print("Failed attempts:", wrong)
            time.sleep(2)
            print("\nTHANK YOU FOR PLAYING!!")
            exit()

        else:
            print("\ninvalid input")
            again = input("Please try again\n>> ")