import string 
import random

char = list(string.ascii_letters + string.digits + "+_)(*&^%$#@!")

def generator_ran_pswd():
    lenght = int(input("Długość hasła: "))

    random.shuffle(char)

    pswd = []
    for i in range(lenght):
        pswd.append(random.choice(char))

    random.shuffle(pswd)

    print("".join(pswd))

generator_ran_pswd()