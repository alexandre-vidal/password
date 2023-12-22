#--------------------------------------------------------------------------------------------------#
#                                  CODE FONCTIONNEL CI-DESSOUS                                     #
#--------------------------------------------------------------------------------------------------#
#                                             Modules                                              #
#--------------------------------------------------------------------------------------------------#

import hashlib
import sys

#--------------------------------------------------------------------------------------------------#
#                                           Fonctions                                              #
#--------------------------------------------------------------------------------------------------#
#                             Fonction no. 1: Insertion du mot de passe                            #
#--------------------------------------------------------------------------------------------------#

def password_input():
    password = input()
    return password

#--------------------------------------------------------------------------------------------------#
#                            Fonction no. 2: Vérification du mot de passe                          #
#--------------------------------------------------------------------------------------------------#

def password_check(): 
        
        print("")
        print("Bienvenue dans ce générateur de mots de passe encryptés !")
        print("Vous aurez besoin d'un mot de passe qui remplit les conditions suivantes :")
        print("")
        print("- au moins un caractère en majuscule")
        print("- au moins un caractère en minuscule")
        print("- au moins un chiffre")
        print("- au moins un caractère spécial")
        print("- le mot de passe doit être d'une longueur d'au moins 8 caractères")
        print("")
        print("Veuillez insérer un mot de passe :")
        
        password = password_input()
        # Appelle la fionction précédente et définit une variable qui sera utilisée à plusieurs reprise tout au long de la fonction.
        
        Upper = False
        Lower = False
        Digit = False
        Special = False
        # Définit les variables qui vérifieront les types de caractères employés dans le mot de passe. Définis comme "Faux" par défaut.
        
        Length = False
        # Définit la variable qui vérifiera si le mot de passe est suffisamment long.
        
        #------------------------------------------------------------------#
        #                VÉRIFICATION DES TYPES DE CARACTÈRES              #
        #------------------------------------------------------------------#
        
        for check in password:
            if check.isupper():
                Upper = True
                # Vérifie s'il y a au moins un caractère haut-de-casse dans la chaîne.
                
            elif check.islower():
                Lower = True
                # Vérifie s'il y a au moins un caractère bas-de-casse dans la chaîne.
                
            elif check.isdigit():
                Digit = True
                # Vérifie s'il y a au moins un chiffre dans la chaîne.
                                
            else:
                Special = True
                # Vérifie s'il y a au moins un caractère spécial dans la chaîne.
        
        print("")
        print("Majuscules :", Upper)
        print("Minuscules :", Lower)
        print("Chiffres :", Digit)
        print("Caractères spéciaux :", Special)
        # Imprime les résultats de chaque vérification pour faire un retour à l'utilisateur.
        
        if len(password) >= 8:
        # Si la longueur du mot de passe est égale ou supérieure à 8...
            Length = True
            print("Longueur:", len(password), "(suffisamment long)")
            # Faire savoir à l'utilisateur que leur mot de passe est suffisamment long.
        else:
            print("Longueur:", len(password), "(pas suffisamment long)")
            # Sinon, indiquez-leur que ce n'est pas le cas.
            
        #------------------------------------------------------------------------------------------#
        #                         PROCÉDÉ DE GÉNÉRATION DE MOT DE PASSE                            #
        #------------------------------------------------------------------------------------------#
            
        if Upper == True and Lower == True and Digit == True and Special == True and Length == True:
        # Si toutes les conditions sont remplies avec succès...
            print("")
            print("Mot de passe généré avec succès !")
            # Imprimer ce message.
            hashed_string = hashlib.sha256(password.encode('UTF-8')).hexdigest()
            # Puis générer un mot de passe avec la méthode d'encryption SHA-256 du module Hashlib.
            print("")
            print(hashed_string)
            # Et l'imprimer pour que l'utilisateur puisse le copier-coller où il le souhaite.

            print("")
            print('Appuyez sur entrée pour quitter le programme, ou tapez "encore" pour relancer le programme :')
            close = input()

            if close == str("encore"):
                password_check()
            
            else:
                sys.exit()
            # Utile pour empêcher la fermeture de la fenêtre de Python sans l'accord de l'utilisateur.
            
        else:
            print("")
            print("Veuillez réessayer :")
            password_check()
            # Si au moins une des conditions n'est pas remplie, inviter l'utilisateur à réessayer et retourner au début de la fonction.
        
password_check()
# Appeler la fonction.

#-----------------------------#
# EXTRAITS DE CODE CI-DESSOUS #
#-----------------------------#

# Ce code nous permet de générer des mot de passe avec la méthode d'encryption SHA-256 :

    # import hashlib
    # print("Please enter a password:")
    # password = input()
    # hashed_string = hashlib.sha256(password.encode('UTF-8')).hexdigest()
    # print(hashed_string)
    
############################################################################################################
    
# Ce code nous permet de vérifier quels types de caractères sont utilisés dans le mot de passe :

    # def password_input():
    #     print("Vérifions quels types de caractères sont utilisés dans votre mot de passe :")
    #     password = input()
    #     return password

    # def string_check(): 
        
    #     password = password_input()
        
    #     Upper = False
    #     Lower = False
    #     Digit = False
    #     Special = False
        
    #     for check in password:
    #         if check.isupper():
    #             Upper = True
    #         elif check.islower():
    #             Lower = True
    #         elif check.isdigit():
    #             Digit = True
    #         else:
    #             Special = True
            
    #     print("Majuscules :", Upper)
    #     print("Minuscules :", Lower)
    #     print("Chiffres :", Digit)
    #     print("Caractères spéciaux :", Special)
        
    #     Length = False
    #     if len(password) >= 8:
    #         Length = True
    #         print("Longueur:", len(password), "(suffisamment long)")
    #     else:
    #         print("Longueur:", len(password), "(pas suffisamment long)")
            
    #     if Upper == True and Lower == True and Digit == True and Special == True and Length == True:
    #         print("Votre mot de passe est suffisamment sécurisé !")
    #     else:
    #         print("Essayez un mot de passe plus complexe :")
    #         string_check()
        
    # string_check()