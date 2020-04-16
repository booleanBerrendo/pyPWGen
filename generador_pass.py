import string
from random import *
from random import randint
caracteres = string.ascii_letters + string.punctuation + string.digits
contraseña = "".join(choice(caracteres) for x in range(randint(8,16)))
print(contraseña)

num = randint(1, 99)
f = open("pass"+str(num)+".txt", "w")
f.write(contraseña)
print("Guardado en pass"+str(num)+".txt")
f.close()
