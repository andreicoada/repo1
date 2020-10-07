print("primul meu mesaj")  #nu necesita paranteze 2.7
#a = input('apasa tasta r') #raw_input pt python 2.7
#print(a)
print("Elevul 'x' nu si-a realizat tema")
print('Elevul "X" nu si-a realizat tema')
# print("Elevul "x" nu si-a realizat tema") #nu functioneaza
print("elevul ''''' nu si-a realizat tema")
print('elevul """""" nu si-a realizat teama')
print("""
\tAna are mere
Maria are BMW
nu plange ana""")
variabila1 = 1
variabila2 = 2
variabila3 = f" Ana are {variabila1} mar si {variabila2} pere."
print(variabila3)
variabila4 = "Ana are {} mar si {} pere".format(variabila1,variabila2)
print(variabila4)
variabila3 = f" Ana are {1} mar si {2} pere.".format(variabila1,variabila2)
print(variabila3)
variabila5 = "Ana are {1} mar si {1} pere.".format(variabila1,variabila2)
print(variabila5)
variabila2 = 3
print("variabila4 =>>", type(variabila4))
print("variabila2 =>>", type(variabila2))
print(type(variabila4))
print(type(variabila2))
variabila6 = "Ana are " + str(variabila2) + " mere."
print(variabila6)
print(variabila1 + variabila2)
print(str(variabila1)+ str(variabila2))

print(variabila2 - variabila1)

variable_number_1 = 3 - 2j
print(variable_number_1.real)
print(variable_number_1.imag)
print(variable_number_1.conjugate())