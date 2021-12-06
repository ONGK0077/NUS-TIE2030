import re

def check_character(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,]')
    if(regex.search(string) == None):
        res = False
    else:
        res = True
    return res

def vowel_checker(statement, vowel):
    count = 0
    for i in range(len(statement)):
        item = statement[i]
        if (item.isalpha() and item.lower() == vowel):
            count += 1
    return count

def total_char_count(statement):
    count = 0
    for i in range(len(statement)):
        count+=1
    return count

def word_count(statement):
    word_list = statement.split()
    return len(word_list)

def others_count(statement):
    count = 0
    for i in range(len(statement)):
        item = statement[i]
        if (item.isnumeric() or check_character(item)):
            count+=1
    return count
    

#statement_one = "PythOn was conceived in the late 1980s by GuIdo van Rossum at CEntrum WIskunde & InformaticA"
#statement_two = "Python uses the words and, or, not for its boOlean opErators rather than the Symbolic &&, ||, ! used in Java and C"


#list_one = [statement_one, statement_two]

#print("Total number of statements:", len(list_one))

#loop = int(input("Do you want to continue? Press 1 for yes and 0 for no."))

'''for item in list_one:
    print("Your Statement:")
    print(item)
    print("Total number of characters in the given statement:", total_char_count(item))
    print("Total number of words in a statement:", word_count(item))
    print("The frequency of vowel a is", vowel_checker(item,'a'))
    print("The frequency of vowel e is", vowel_checker(item,'e'))
    print("The frequency of vowel i is", vowel_checker(item,'i'))
    print("The frequency of vowel o is", vowel_checker(item,'o'))
    print("The frequency of vowel u is", vowel_checker(item,'u'))
    print("Total number of characters other than alphabets:", others_count(item))
    print()'''

loop = 0

while True:
    try:
        loop = int(input("Enter the number of total statements required:"))
        break
    except ValueError:
        print("You have entered other than an integer. Please key the value again.")

for i in range(loop):
    item = input("Enter your statement: ")
    print("Your Statement:")
    print(item)
    print("Total number of characters in the given statement:", total_char_count(item))
    print("Total number of words in a statement:", word_count(item))
    print("The frequency of vowel a is", vowel_checker(item,'a'))
    print("The frequency of vowel e is", vowel_checker(item,'e'))
    print("The frequency of vowel i is", vowel_checker(item,'i'))
    print("The frequency of vowel o is", vowel_checker(item,'o'))
    print("The frequency of vowel u is", vowel_checker(item,'u'))
    print("Total number of characters other than alphabets:", others_count(item))
    print()
