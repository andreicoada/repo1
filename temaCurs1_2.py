# Problema 1
print("Problema 1, hit Enter to continue")
brands = ('Asus', 'Hp', 'Lenovo', 'Apple', 'Samsung')
for a in brands:
    print(a,'are un numar de',len(a),'caractere')

# Problema 2

print("\n\tAcum vom valida o adresa de mail.")
mail ="andrei1301"
user = input(str("Introdu te rugam o adresa de mail: "))
if user == "andrei1301":
    print("Felicitari, adresa de mail este valida. Ea este: ",mail,"@gmail.com")
else:
    print("Ne pare rau dar adresa",user,"@gmail.com nu este corecta")

#Problema 3

print("Problema 3. Apasa <Enter> pentru a continua")
enter = input()
numarTel = "0744602279"  #presupunem ca este un nr de tel dintr-o baza de date
numarTel=input("Adauga te rog nr de tel: ")
if numarTel == "0744602279":
    print("Felicitari, ai validat numarul de tel ",numarTel)
else:
    print("Ne pare rau, numarul de teleton ",numarTel, "nu se afla in baza noastra de date")

