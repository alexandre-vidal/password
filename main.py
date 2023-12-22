#--------------------------------------------------------------------------------------------------#
#                                       WORKING CODE BELOW                                         #
#--------------------------------------------------------------------------------------------------#
#                                             Modules                                              #
#--------------------------------------------------------------------------------------------------#

import hashlib
import sys

#--------------------------------------------------------------------------------------------------#
#                                           Functions                                              #
#--------------------------------------------------------------------------------------------------#
#                                  Function no. 1: Password input                                  #
#--------------------------------------------------------------------------------------------------#

def password_input():
    password = input()
    return password

#--------------------------------------------------------------------------------------------------#
#                                  Function no. 2: Password check                                  #
#--------------------------------------------------------------------------------------------------#

def password_check(): 
        
        print("")
        print("Welcome in this encrypted password generator!")
        print("You will need a password that meets the following requirements:")
        print("")
        print("- at least one uppercase character")
        print("- at least one lowercase character")
        print("- at least one number")
        print("- at least one special character")
        print("- the password must be at least 8 characters in length")
        print("")
        print("Please enter a password:")
        
        password = password_input()
        # Calls the previous function and defining a variable that'll be used repeatedly throughout the entire function.
        
        Upper = False
        Lower = False
        Digit = False
        Special = False
        # Defining the variables that will check for the types of characters used in the password. Making them "False" by default.
        
        Length = False
        # Defining the variable that will check if the password is long enough.
        
        #------------------------------------------------------------------#
        #                       CHARACTER TYPE CHECKS                      #
        #------------------------------------------------------------------#
        
        for check in password:
            if check.isupper():
                Upper = True
                # Checks if there are any uppercase characters in the string.
                
            elif check.islower():
                Lower = True
                # Checks if there are any lowercase characters in the string.
                
            elif check.isdigit():
                Digit = True
                # Checks if there are any numbers in the string.
                
            else:
                Special = True
                # Checks if there are any special characters in the string.
        
        print("")
        print("Uppercase:", Upper)
        print("Lowercase:", Lower)
        print("Numbers:", Digit)
        print("Special characters:", Special)
        # Print the results of each check to give the user feedback.
        
        if len(password) >= 8:
        # If the password's length is equal or greater than 8...
            Length = True
            print("Length:", len(password), "(long enough)")
            # Let the user know their password is long enough.
        else:
            print("Length:", len(password), "(not long enough)")
            # Otherwise, tell them it's not.
            
        #------------------------------------------------------------------------------------------#
        #                              PASSWORD GENERATION PROCESS                                 #
        #------------------------------------------------------------------------------------------#
            
        if Upper == True and Lower == True and Digit == True and Special == True and Length == True:
        # If all requirements are successfully met...
            print("")
            print("Password successfully generated!")
            # Print this message.
            hashed_string = hashlib.sha256(password.encode('UTF-8')).hexdigest()
            # Then generate a password using hashlib's SHA-256 encryption method.
            print("")
            print(hashed_string)
            # And print it for the user to copy and paste anywhere they want.
            
            with open('saved_passwords.txt', 'a') as o:
                o.write(password + "\n")
                o.write(hashed_string + "\n" + "\n")
            # Saves the passwords in a text file.

            print("")
            print('Press enter to close the program, or type "again" to run it once more:')
            close = input()

            if close == str("again"):
                password_check()
            
            else:
                sys.exit()
            # Useful to prevent Python's window from closing without the user's consent.
            
        else:
            print("")
            print("Try again:")
            password_check()
            # If at least one condition isn't met, prompt the user to try again and roll back to the start of the function until they succeed.
        
password_check()
# Calling the function.

#--------------------#
# CODE SAMPLES BELOW #
#--------------------#

# This code enables us to generate SHA256-encrypted passwords:

    # import hashlib
    # print("Please enter a password:")
    # password = input()
    # hashed_string = hashlib.sha256(password.encode('UTF-8')).hexdigest()
    # print(hashed_string)
    
############################################################################################################
    
# This code enables us to check which characters are used in the input:

    # def password_input():
    #     print("Let's check which types of characters are in your password:")
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
            
    #     print("Uppercase:", Upper)
    #     print("Lowercase:", Lower)
    #     print("Numbers:", Digit)
    #     print("Special characters:", Special)
        
    #     Length = False
    #     if len(password) >= 8:
    #         Length = True
    #         print("Length:", len(password), "(long enough)")
    #     else:
    #         print("Length:", len(password), "(not long enough)")
            
    #     if Upper == True and Lower == True and Digit == True and Special == True and Length == True:
    #         print("Success!")
    #     else:
    #         print("Try again:")
    #         string_check()
        
    # string_check()