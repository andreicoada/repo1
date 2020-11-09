import random
lista_cuvinte = ["masina", "vapor", "calculator", "laptop", "avion", "maimuta", "caine"]

def alege_cuvant(lista_cuvinte):
    cuvant = random.choice(lista_cuvinte)
    return cuvant.upper()


def joc(cuvant):
    completare_cuvant = "_" * len(cuvant)
    ghicit = False
    litera_ghicita = []
    cuvinte_ghicite = []
    incercari = 8
    print("Sa jucam Spanzuratoare !")
    print((incercari))
    print(completare_cuvant)
    print("\n")
    while not ghicit and incercari > 0:
        ghicire = input("Adauga o litera: ").upper()
        if len(ghicire) == 1 and ghicire.isalpha():
            if ghicire in litera_ghicita:
                print("Ai mai incercat aceasta litera", ghicire, "!")
            elif ghicire not in cuvant:
                print(ghicire, "Nu se afla in cuvant")
                incercari -= 1
                litera_ghicita.append(ghicire)
            else:
                print("Ai ghicit litera,", ghicire,"este parte din cuvant!")
                litera_ghicita.append(ghicire)
                cuvant_ca_lista = list(completare_cuvant)
                indices = [i for i, letter in enumerate(cuvant) if letter == ghicire]
                for index in indices:
                    cuvant_ca_lista[index] = ghicire
                completare_cuvant = "".join(cuvant_ca_lista)
                if "_" not in completare_cuvant:
                    ghicit = True
        elif len(ghicire) == len(cuvant) and ghicire.isalpha():
            if ghicire in cuvinte_ghicite:
                print("Deja ai incercat", ghicire, "!")
            elif ghicire != cuvant:
                print(ghicire, " Nu este cuvantul")
                incercari -= 1
                cuvinte_ghicite.append(ghicire)
            else:
                ghicit = True
                completare_cuvant = cuvant
        else:
            print("Ai introdus un caracter invalid !")
        print((incercari))
        print(completare_cuvant)
        print("\n")
    if ghicit:
        print("Bravo, ai ghicit cuvantul!")
    else:
        print("Ai atins numarul maxim de incercari. Cuvantul era " + cuvant)


def main():
    cuvant = alege_cuvant(lista_cuvinte)
    joc(cuvant)
    while input("Jucam din nou? (Y/N) ").upper() == "Y":
        cuvant = alege_cuvant(lista_cuvinte)
        joc(cuvant)

if __name__ == "__main__":
    main()