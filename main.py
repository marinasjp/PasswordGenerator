import random
import string
import enchant


def ask_lengths():
    """Takes input from user to determine the number of letters, numbers and characters to include in the password.
    It takes these values and puts them in a list."""

    questions = ["letters", "numbers", "characters"]
    lengths = []

    for i in range(3):
        done = 0
        while done == 0:
            try:
                letter_no = int(input("Input the number of " + questions[i] + ": "))
                done = 1
                lengths.append(letter_no)

            except ValueError:
                print("Please input a number.")

    return lengths


def create_password(lengths):
    """Adds the required number of elements, according to the list given as argument. Returns the password."""

    exists = True
    while exists:
        password = ""
        for i in range(lengths[0]):
            letter = random.choice(letters)
            password += letter

        # check if word exists in the english language
        exists = dict.check(password.lower())

    for i in range(lengths[1]):
        num = str(random.randint(0, 10))
        password += num

    for i in range(lengths[2]):
        char = random.choice(characters)
        password += char

    return password


def main():
    print("*" * 50)
    print("Welcome to RANDOM PASSWORD GENERATOR.\n You will be able to generate passwords in the format: "
          "letters + numbers + special characters")
    print("*" * 50)

    generate = "yes"
    while generate.lower() == "yes":

        done = 0
        # Loop until user gives a valid answer
        while done == 0:
            try:
                no_passwords = int(input("\nInput the number of passwords to generate: "))
                done = 1
            except ValueError:
                print("Please input a number.")

        lengths = ask_lengths()

        for i in range(no_passwords):
            password = create_password(lengths)
            print("The password generated is: " + password)

        generate = input("Do you want to generate more passwords? Enter \"yes\" to do so.\n")

    print("Thank you for using random password generator!")


if __name__ == '__main__':
    dict = enchant.Dict("en_US")
    letters = string.ascii_letters
    characters = ["/", "(", ")", "=", "!", "?", "@"]
    main()
