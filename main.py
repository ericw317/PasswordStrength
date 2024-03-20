import secrets
import string
import math

# function that returns number of pairs of upper and lower case characters
def mixedCasePairs(passwd):
    upperAmount, lowerAmount, pairAmount = 0, 0, 0

    # for loop to cycle through each password character
    for x in passwd:
        if x.isalpha():  # only check if character is alphabetic
            if x.isupper():  # if character is uppercase, add to upperAmount
                upperAmount += 1
            elif x.islower():  # if char is lowercase, add to lowerAmount
                lowerAmount += 1

    if upperAmount > 0 and lowerAmount > 0:
        if upperAmount > lowerAmount:
            pairAmount = lowerAmount
        elif upperAmount < lowerAmount:
            pairAmount = upperAmount
        else:
            pairAmount = upperAmount

    # return amount of pairs
    return int(pairAmount)

# function to check how many numbers in password
def numberAmount(passwd):
    counter = 0

    #  for loop to go through each char in password
    for x in passwd:
        if x.isnumeric():  # if char is numeric, add 1 to counter
            counter += 1

    return int(counter)

# function to check if password contains any special characters
def specialAmount(passwd):
    specCounter = 0

    # loop through password to check for special characters
    for x in passwd:
        if not x.isalnum():  # if char is not alphanumeric, then set specPresent to True and return Ture
            specCounter += 1

    return specCounter

# function to print suggestion message at end of the program
def passwordSuggestion(length, case, numbers, special):
    if length < 3:
        print("- Increase password length")
    if case < 3:
        print("- Use more uppercase and lowercase letters")
    if numbers < 3:
        print("- Use more numbers")
    if special < 3:
        print("- Use more special characters and symbols")

    return ""

# function to generate a random password
def generatePassword(passwordLength):
    charBank = string.ascii_letters + string.digits + string.punctuation  # bank of characters to select from
    generatedPassword = ""  # initialize empty password string

    # choose a passwordLength amount of characters and put them together
    for x in range(passwordLength):
        generatedPassword += secrets.choice(charBank)

    return generatedPassword


programLoop = True

while programLoop:

    selection = input("Select what you'd like to do: \n"
                      "1) Check password strength\n"
                      "2) Generate a random password\n"
                      "0) Quit\n")

    # input validation
    while not selection.isnumeric() or int(selection) < 0 or int(selection) > 2:
        selection = input("Must selection a number between 0-2: ")

    if int(selection) == 1:
        password = input("Enter a password to check it's strength: ")  # stores user input in password variable

        length = len(password)  # store length of password
        lengthAmount = math.floor(length/6)  # store point amount for length
        casePairs = mixedCasePairs(password) # store number of case pairs
        numbersAmount = numberAmount(password)  # store amount of numbers
        specAmount = specialAmount(password)  # store amount of special characters

        strengthScore = 0  # initialize strength score valuable
        passStrength = ""  # initialize variable to convert from strength score

        # series of if statements to increment strengthScore if certain aspects are present
        if lengthAmount <= 3:
            strengthScore += lengthAmount
        else:
            strengthScore += 3

        if casePairs <= 3:
            strengthScore += casePairs
        else:
            strengthScore += 3

        if numbersAmount <= 3:
            strengthScore += numbersAmount
        else:
            strengthScore += 3

        if specAmount <= 3:
            strengthScore += specAmount
        else:
            strengthScore += 3

        # present analysis of strength based on score
        if strengthScore <= 3:
            passStrength = "Poor"

            print("Password Score: " + passStrength)
            print("Consider doing the following to make your password stronger: ")
            print(passwordSuggestion(lengthAmount, casePairs, numbersAmount, specAmount))
        elif 3 < strengthScore <= 6:
            passStrength = "Weak"

            print("Password Score: " + passStrength)
            print("Consider doing the following to make your password stronger: ")
            print(passwordSuggestion(lengthAmount, casePairs, numbersAmount, specAmount))
        elif 6 < strengthScore <= 9:
            passStrength = "Decent"

            print("Password Score: " + passStrength)
            print("Consider doing the following to make your password stronger: ")
            print(passwordSuggestion(lengthAmount, casePairs, numbersAmount, specAmount))
        elif strengthScore > 9:
            passStrength = "Great"

            print("Password Score: " + passStrength)
            print("Congratulations! Your password is strong.")

        input("Press enter to continue.")
    elif int(selection) == 2:
        passLength = input("How long would you like your password to be?\n")

        # input validation
        while not passLength.isnumeric() or int(passLength) < 1 or int(passLength) > 100:
            passLength = input("Input must be a number between 1-100: ")

        print(generatePassword(int(passLength)))
        input("\nPress enter to continue.")
    elif int(selection) == 0:
        programLoop = False
