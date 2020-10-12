# # while conditionare:
# #     atribuire1 / instructiune1
#       atribuire2 / instructiune2
#       atribuire3 / instructiune3
#       ....
#       atribuiren / instructiunen

# while True:
#     print('ruleaza')
#     break

# cel_mai_mare_numar = 999999
# number = int(input('Introdu un numar: '))
# while number != -1:
#     if number > cel_mai_mare_numar or number < cel_mai_mare_numar and number > -1:
#         number -=1
#     elif number < -1:
#         number += 1
#     else:
#         print(cel_mai_mare_numar)
#     print(number)


#Numere pare is numere impare

a = int(input('Introdu un numar: '))
nrPare = 0
nrImpare = 0
while a != 0:
    if a % 2 == 0:
        nrPare += 1
    else:
        nrImpare += 1
    a = int(input("Introdu un numar: "))
print("Am gasit {} nr pare si {} nr impare !".format(nrPare,nrImpare))




