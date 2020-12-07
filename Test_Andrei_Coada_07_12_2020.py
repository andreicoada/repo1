import collections

lista_nume = ["Maria", "Irina", "Claudiu", "Ionut", "Irina", "Matei", "Irina", "Maria", "Claudiu"]

print(sorted(lista_nume)) # Sortare nume in ordine alfabetica

print(len(lista_nume)) # afiseaza numarul total de Nume din lista



print(collections.Counter(lista_nume)) # afiseaza numarul de aparitii al fiecarui nume


print(max(set(lista_nume),key = lista_nume.count)) # afiseaza numele care apare de cele mai multe ori in lista initiala

print(min(set(lista_nume), key= lista_nume.count)) #afiseaza numele care apare de cele mai multe ori in lista initiala








