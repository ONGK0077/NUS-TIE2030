import re

def check_character(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(string) == None):
        res = False
    else:
        res = True
    return res


trials = 0

print("The rules for creating a password here are:")
print(" The minimum length should be of 10 characters including")
print(" at least one numberical value, one uppercase English alphabet,")
print(" one lowercase English alphabet, and one symbol")
print(" and no 3 consecutive characters")

while trials < 5:
    #counter variables
    consecutive = False
    len_password = True
    num_value = True
    upper_case = True
    lower_case = True
    symbol = True
    digit_count = 0
    symbol_count = 0
    texture_count = 0

    print()

    if (trials > 0):
        while True:
            try:
                set_password = int(input("Want to set your password? Type 1 for yes and 0 for no:"))
                break
            except ValueError:
                print("You have entered something other than 0 or 1. Please retype your password.")
        if (set_password == 0):
            print("You have chosen not to set your password. Goodbye!")
            break
    
    password = str(input("Enter a password: "))
    pass_len = len(password)
    print("Breakdown of the password: ")
    print("Length of you password is:",pass_len)

    if (pass_len >= 10):
        len_password = False
    
    for i in range(pass_len):
        pass_char = password[i]

        #check if password have 3 consecutive numbers
        if (i < pass_len-2):
            if (pass_char == password[i+1] and pass_char == password[i+2] and password[i+1] == password[i+2]):
                consecutive = True
        
        # check if password index is character
        if (pass_char.isalpha()):
            if (pass_char.isupper()):
                upper_case = False
                texture_count += 1
            elif (pass_char.islower()):
                lower_case = False
                texture_count += 1
                
        # check if password is numerical
        if (pass_char.isnumeric()):
            num_value = False
            digit_count += 1

        # check if theres symbol
        if (check_character(pass_char)):
            symbol = False
            symbol_count += 1

            
    if (consecutive):
        print("Please don't put 3 consecutive character")
        print("Minimum password length of 10!")
        print("Invalid password. Try again please.")
    elif (len_password or num_value or upper_case or lower_case or symbol):
        print("Invalid password. Try again please.")
    else:
        print("Valid Password.")
        print("There are", digit_count , "digits in your password.")
        print("There are", texture_count , "texture characters in your password.")
        print("There are", symbol_count , "symbols in your password.")
        print("Valid! Great!")
        break;

    #increment of trials
    trials += 1

if (trials == 5):
    print("You have exceeded the max number of chances! Bye.")
        
