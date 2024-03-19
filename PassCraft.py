"""
Script pentru generarea de parole aleatorii.

Script: PassCraft
Autor: ThinkRoot
Versiune: 7

Descriere:
Acest script permite utilizatorului să genereze parole aleatorii conform specificațiilor dorite, inclusiv lungimea parolei, includerea sau excluderea caracterelor speciale și specificarea numărului de parole generate.

Utilizare:
    - Asigurați-vă că aveți Python instalat pe computer. Puteți descărca și instala Python de la adresa https://www.python.org/downloads/.
    - Descărcați scriptul pentru generarea de parole aleatorii sau creați un nou fișier text și copiați codul din script în fișierul text.
    - Deschideți terminalul sau linia de comandă și navigați la directorul în care se află scriptul.
    - Rulați scriptul folosind Python. Pentru a face acest lucru, tastați `python PassCraft.py` și apăsați Enter.
    - Urmăriți instrucțiunile afișate de script pentru a specifica lungimea parolei dorite, dacă doriți să includeți caractere speciale, numărul de parole dorite și dacă doriți să generați mai multe parole.
    - Scriptul va genera și va afișa parolele aleatorii conform specificațiilor furnizate.
    - Puteți repeta pașii 5-6 pentru a genera mai multe seturi de parole, dacă doriți.
"""

import random
import string
import secrets

def generate_password(length=16, include_special_chars=True, custom_charset=None):
    """
    Funcția generează o parolă aleatorie conform specificațiilor date.

    Parametri:
    length (int): Lungimea parolei dorite (implicit 16).
    include_special_chars (bool): Indicator pentru includerea caracterelor speciale (implicit True).
    custom_charset (str): Setul personalizat de caractere pentru generarea parolei.

    Returnează:
    str: Parola generată.
    """
    if custom_charset:
        # Verificare set de caractere personalizat
        if len(set(custom_charset)) != len(custom_charset):
            raise ValueError("Setul personalizat de caractere conține caractere duplicate.")
        if any(char not in string.printable for char in custom_charset):
            raise ValueError("Setul personalizat de caractere conține caractere nevalide.")
        characters = custom_charset
    else:
        characters = string.ascii_letters + string.digits
        if include_special_chars:
            characters += string.punctuation

    if not isinstance(length, int) or length <= 0:
        raise ValueError("Lungimea parolei trebuie să fie un număr întreg pozitiv.")

    if length < 8:
        raise ValueError("Lungimea minimă a parolei trebuie să fie cel puțin 8 caractere.")

    password = [secrets.choice(string.ascii_lowercase),
                secrets.choice(string.ascii_uppercase),
                secrets.choice(string.digits)]
    if include_special_chars:
        password.append(secrets.choice(string.punctuation))

    password.extend(secrets.choice(characters) for _ in range(length - len(password)))
    random.shuffle(password)

    return ''.join(password)

def get_password_requirements():
    """
    Funcția solicită utilizatorului lungimea, opțiunea de includere a caracterelor speciale și opțiunea de repetare.

    Returnează:
    int: Lungimea parolei specificată de utilizator.
    bool: Indicator pentru includerea caracterelor speciale.
    bool: Indicator pentru repetarea generării de parole.
    """
    print("Introdu lungimea parolei (minim 8): ")
    while True:
        try:
            password_length = int(input())
            if password_length < 8:
                raise ValueError("Lungimea minimă a parolei trebuie să fie cel puțin 8 caractere.")
            break
        except ValueError:
            print("Te rog introdu un număr întreg pentru lungimea parolei: ")

    print("Dorești să incluzi caractere speciale? (Da/Nu): ")
    while True:
        choice = input().strip().lower()
        if choice in ["da", "nu"]:
            include_special_chars = choice == "da"
            break
        else:
            print("Te rog răspunde cu Da sau Nu: ")

    print("Câte parole dorești să generezi?")
    while True:
        try:
            num_passwords = int(input())
            if num_passwords <= 0:
                raise ValueError("Numărul de parole generate trebuie să fie un număr pozitiv.")
            break
        except ValueError:
            print("Te rog introdu un număr pozitiv pentru numărul de parole generate: ")

    print("Dorești să generezi alte parole? (Da/Nu): ")
    while True:
        choice = input().strip().lower()
        if choice in ["da", "nu"]:
            repeat = choice == "da"
            break
        else:
            print("Te rog răspunde cu Da sau Nu: ")

    return password_length, include_special_chars, num_passwords, repeat

if __name__ == "__main__":
    try:
        print("Acest script generează parole aleatorii.")
        print("Instrucțiuni: Introdu lungimea dorită pentru parolă (minim 8), alege dacă dorești să incluzi caractere speciale, specifică numărul de parole și dacă dorești să generezi alte parole.")

        while True:
            password_length, include_special_chars, num_passwords, repeat = get_password_requirements()

            for _ in range(num_passwords):
                password = generate_password(password_length, include_special_chars)
                print("Parola generată:", password)

            if not repeat:
                break
    except Exception as e:
        print("Eroare:", e)
