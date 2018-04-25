#Uses list comprehension to return whether a password meets a minimum threshold:
#It contains a mixture of upper and lowercase letters, and at least one number


def meets_threshold(password):
    UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LC_LETTERS = "abcdefghijklmnopqrstuvwzyz"
    NUMBERS = "01234556789"

    #Converted is the list that contains what kind of letters and numbers are used in the password
    #0 = Lowercase letter
    #1 = Uppercase letter
    #2 = Number
    
    converted = [1 for x in password if x in UC_LETTERS]
    converted += [0 for x in password if x in LC_LETTERS] 
    converted += [2 for x in password if x in NUMBERS]

    strength = 0

    #Iterating through converted to see if password meets criteria:
    for x in converted:
        if x == 1:
            strength += 1

        elif x == 0:
            strength += 1

        elif x == 2:
            strength += 1

    if strength > 3:
        return True

    else:
        return False 
    

#Uses list comprehension to return a password's strength rating. This function should return a low integer for a weak password and a higher integer for a stronger password(Suggested scale: 1-10)
#Criteria:
#Mixture of upper and lowercase
#Inclusion of numerals
#Inclusion of these non-alphanumeric char: . ? ! & # , ; : - _ *



def check_strength(password):
    UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LC_LETTERS = "abcdefghijklmnopqrstuvwzyz"
    NUMBERS = "01234556789"
    SPECIAL_CHAR = ".?!&#,;:-_*"


    converted = [1 for x in password if x in UC_LETTERS]
    converted += [1 for x in password if x in LC_LETTERS] 
    converted += [1 for x in password if x in NUMBERS]
    converted += [2 for x in password if x in NUMBERS]

    upperCount = 0
    lowerCount = 0
    charCount = 0
    numCount = 0

    strength = 0

    #Iterating through converted to see if password meets criteria:
    for x in converted:
        strength += x

    if strength > 10:
        strength = 10

    return strength 
    


password = "NinjaUnicorn123"
password2 = "pew"
password3 = "bad"
password4 = "Green!67"
password5="GrV1@"

print check_strength(password4)
print check_strength(password2)
print check_strength(password2)
print check_strength(password)
print check_strength(password5) 
