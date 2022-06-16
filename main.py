import random


def create_password(letter_no, num_no, char_no):
    password = ""

    for i in range(letter_no):
        letter = random.choice(letters)
        password += letter

    for i in range(num_no):
        num = str(random.randint(0, 10))
        password += num

    for i in range(char_no):
        char = random.choice(characters)
        password += char

    return password


def main():
    letter_no = int(input("Input the number of letters: "))
    int_no = int(input("Input the number of numbers: "))
    char_no = int(input("Input the number of characters: "))

    password = create_password(letter_no, int_no, char_no)
    print(password)


if __name__ == '__main__':
    letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x"]
    characters = ["/", "(", ")", "=", "!", "?", "@"]
    main()
