import random
import math


password = []
gen_password = ""
alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

print("Random password generator!")
alpha_len = int(input("How many letters? "))
num_len = int(input("How many numbers? "))
special_len = int(input("How many special characters? "))


def generator(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)


generator(alpha_len, alpha, True)
generator(num_len, num)
generator(special_len, special)

random.shuffle(password)


for p in password:
    gen_password = gen_password + str(p)
print("Password: ", gen_password)
