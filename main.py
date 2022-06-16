import random


def create_password(lengths):
    password = ""

    for i in range(lengths[0]):
        letter = random.choice(letters)
        password += letter

    for i in range(lengths[1]):
        num = str(random.randint(0, 10))
        password += num

    for i in range(lengths[2]):
        char = random.choice(characters)
        password += char

    return password


def ask_lenghts():
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


def main():
    generate = "yes"
    while generate.lower() == "yes":
        
        done = 0
        while done == 0:
            try:
                no_passwords = int(input("Input the number of passwords to generate: "))
                done = 1
            except ValueError:
                print("Please input a number.")

        lengths = ask_lenghts()

        for i in range(no_passwords):
            password = create_password(lengths)
            print("The password generated is: " + password)

        generate = input("Do you want to generate more passwords? Enter \"yes\" to do so.\n")


if __name__ == '__main__':
    letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x"]
    characters = ["/", "(", ")", "=", "!", "?", "@"]
    main()
