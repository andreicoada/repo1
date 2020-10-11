# Problema 1
print("Problema 1")
problema = input("\n\tApasa <Enter> pentru a continua")
brands = ('Asus', 'Hp', 'Lenovo', 'Apple', 'Samsung')
for a in brands:
    print("\n",a,'are un numar de',len(a),'caractere')

# Problema 2
print("\nProblema 2")
problema = input("\n\tApasa <Enter> pentru a continua")
print("\n\tAcum vom valida o adresa de mail.")
mail ="andrei1301"
user = input(str("\nIntrodu te rugam o adresa de mail: "))
if user == "andrei1301":
    print("\nFelicitari, adresa de mail este valida. Ea este: ",mail,"@gmail.com")
else:
    print("\nNe pare rau dar adresa",user,"@gmail.com nu este corecta")

#Problema 3
print("\n\tProblema 3. Apasa <Enter> pentru a continua")
problema = input()
numarTel = "0744602279"  #presupunem ca este un nr de tel dintr-o baza de date
numarTel=input("Adauga te rog nr de tel: ")
if numarTel == "0744602279":
    print("Felicitari, ai validat cu succes numarul de telefon: ",numarTel)
else:
    print("Ne pare rau, numarul de teleton ",numarTel, "nu se afla in baza noastra de date!")

