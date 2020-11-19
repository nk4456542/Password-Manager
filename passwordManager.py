from pyperclip import copy, paste
from base64 import b64encode, b64decode

websitePasswords = {
    'gmail': 'WmFoZWVyIEFiYmFz',
    'github': 'eW91RG9udEtub3dNeVBhc3N3b3Jk',
    'gitlab': 'WmFoZWVyIEFiYmFz'
}


def addPassword():
    print("Enter Website Name:")
    print("Example:\"gmail\" or \"github\"")
    websiteName = input()
    if websiteName in websitePasswords.keys():
        print(
            f"You already have an account and password for {websiteName}, retrieve by selecting \"1\"")
        checkInput()
    else:
        print(f"Enter the Password of {websiteName}")
        password = input()
        encodedPassword = encodePassword(password)
        websitePasswords[websiteName] = encodedPassword
        print(websitePasswords)
        return websitePasswords


def retrievePassword():
    print("Enter the Website Name that you want the password for:")
    print("Example:\"gmail\" or \"github\"")
    websiteName = input()
    encodedPassword = websitePasswords.get(websiteName)
    if encodedPassword is None:
        print(f"{websiteName} account does not exist, add by selecting \"2\"")
        checkInput()
    else:
        print(encodedPassword)
        decodedPassword = b64decode(encodedPassword.encode())
        print(decodedPassword.decode())
        copy(decodedPassword.decode())
        return decodedPassword


def checkPasswordValidation(enteredPassowordEncode, originalPasswordEncode):
    return enteredPassowordEncode == originalPasswordEncode


def encodePassword(enteredPassword):
    enteredPassword = enteredPassword.encode()
    enteredPasswordEncode = b64encode(enteredPassword)
    return enteredPasswordEncode.decode()


def getOriginalPassword():
    with open("originalPasswordEncode.txt", "r") as file:
        originalPasswordEncode = file.read()
    return originalPasswordEncode


def encodeOriginalPassword():
    with open("originalPassword.txt", "r") as file:
        data = file.read()
        encodeOriginalPassword = b64encode(data.encode())
        with open("originalPasswordEncode.txt", "wb") as writeFile:
            writeFile.write(encodeOriginalPassword)


def checkInput():
    print("Enter 1 or 2 or \"break\"")
    userNav = input()
    if userNav == '1':
        retrievePassword()
    elif userNav == '2':
        addPassword()
    elif userNav == "break":
        quit()
    else:
        print("Please enter a valid number")
        checkInput()


def enterPasswordAgain():
    print("Your password did not match")
    print("please enter again")
    print("OR enter \"break\" to exit from the App.")


def greetUser():
    print("Welcome to the Password Manager")
    print("Our Application provides the following features")
    print("1.Retrieve your password by typing the website name")
    print("2.Add new website name and the corresponding password")
    while True:
        checkInput()


def Login():
    print("Enter Password to Login")
    originalPassword = encodeOriginalPassword()
    enteredPasswordEncode = input()
    if enteredPasswordEncode != "break":
        # enteredPasswordEncode = encodePassword(enteredPassword)
        originalPasswordEncode = getOriginalPassword()
        isLoggedIn = checkPasswordValidation(
            enteredPasswordEncode, originalPasswordEncode)
        return isLoggedIn
    else:
        quit()


def main():
    isLoggedIn = Login()
    while True:
        if isLoggedIn:
            greetUser()
            break
        else:
            enterPasswordAgain()
            isLoggedIn = Login()


main()
