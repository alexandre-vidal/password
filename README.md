#                                                             ENGLISH                                                              #

This is a password generator I've coded from scratch, using the hashlib module's SHA-256 encryption method.
It also gives feedback on the user's password using different simple check methods, and prompts them to try improving it until it meets the following requirements:

- at least one uppercase character
- at least one lowercase character
- at least one digit
- at least one special character
- the password's length must be equal or greater than 8 characters

If all requirements are met, then a password will be generated for the user to copy and paste anywhere they please. It will also be saved to an external txt file named "saved_passwords.txt".
Otherwise, they will be prompted to try again.

This repository contains:
- main.py (the main password generator file, in English, written in Python 3)
- main_fr.py (the same password generator file, in French)
- secrets_strings.py (an alternative, albeit unfinished password generator, also written in Python 3, that makes use of the secrets and string modules to randomly generate a password based on a number given by the user to define its length)

#                                                             FRANÇAIS                                                             #

Ceci est un générateur de mot de passe que j'ai codé en partant de zéro, utilisant la méthode d'encryption SHA-256 du module hashlib.
Il fait également des retours sur le mot de passe de l'utilisateur en utilisant des méthodes de vérification simples, et les invite à l'améliorer jusqu'à ce qu'il corresponde aux critères suivants :

- au moins un caractère en majuscule
- au moins un caractère en minuscule
- au moins un chiffre
- au moins un caractère spécial
- la longueur du mot de passe doit être égale ou supérieure à 8 caractères

Si tous les critères sont remplis, un mot de passe sera généré pour que l'utilisateur puisse le copier partout où il le souhaite. Il sera également sauvegardé dans un fichier nommé "saved_passwords.txt".
Autrement, le programme demandera à l'utilisateur de réessayer.

Ce dépôt contient :
- main_fr.py (le fichier du générateur de mots de passe principal, en français, codé en Python 3)
- main.py (le même fichier, en anglais)
- secrets_strings.py (un générateur de mots de passe alternatif, également codé en Python 3, qui utilise les modules strings et secrets pour générer de manière aléatoire des mots de passe en se basant sur un chiffre donné par l'utilisateur pour définir a longueur, il est cependant incomplet)