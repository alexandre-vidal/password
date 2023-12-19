import hashlib

a_string = input("Rentrez un mot de passe qui contiendra au moins 8 caractères, une majuscule, un minuscule, un chiffre, et un caractère spécial : ")

if any(ch.isupper() for ch in a_string) == True :

    if any(ch.islower() for ch in a_string) == True :

        if any(ch.isdigit() for ch in a_string) == True :

            if len(a_string) >= 8:

                hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
                print(hashed_string)