# This is a sample Python script.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    encoded = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        menu_selection = int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)

        elif menu_selection == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded} and the original password is {decoded}.")
        elif menu_selection == 3:
            break
def encode(password):
    finalpassword = ""
    for i in password:
        i = int(i)
        t = i + 3
        u = str(t)
        finalpassword += u
    return finalpassword


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
