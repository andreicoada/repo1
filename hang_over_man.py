import random

words_list = ['pasare', 'laptop', 'masina', 'telefon', 'pisica']

chosen_word = random.choice(words_list)
selected_word = list(['_'] * len(chosen_word))
wrong_choose = []
number_of_attempts = 7
print('Your word until this moment is: {}'.format(' '.join(selected_word)))

while selected_word != chosen_word and number_of_attempts:
    next_letter = input('Next letter: ').lower()

    if len(next_letter) != 1:
        print('Trebuie introdusa o singura litera. Incercati din nou !')
        continue
    elif not next_letter.isalpha():
        print('Caracterul introdus trebuie sa fie o litera. Incercati din nou.')
        continue
    elif next_letter in wrong_choose or next_letter in selected_word:
        print('Litera a fost deja aleasa. Incercati din nou.')
        continue
    elif next_letter in chosen_word:
        for idx, litera in enumerate(chosen_word):
            if litera == next_letter:
                selected_word[idx] = next_letter

        print('Your word is : {}'.format(' '.join(selected_word)))
    else:
        wrong_choose.append(next_letter)
        number_of_attempts -= 1
        print('Remaining attempts : {} | wrong letters: {}'.format(number_of_attempts, wrong_choose))

if number_of_attempts:
    print('Succes! Cuvantul corect era: {}'.format(''.join(chosen_word)))
else:
    print('Gresit! Cuvantul corect era: {}'.format(''.join(chosen_word)))

