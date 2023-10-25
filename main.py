# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def decoder(password):
    list = []
    for i in range(0, len(password)):
        hold = int(password[i])
        hold -= 3
        if hold < 0:
            hold = abs(hold)
        list.append(str(hold))
    string = ''.join(list)
    return string






def encoder(decode):
    list = []

    for i in range(0, len(decode)):
        temp = int(decode[i])
        temp += 3
        if temp >= 10:
            temp %= 10
        list.append(str(temp))
    string = ''.join(list)
    return string




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option:")
        if choice == "1":
            user_pass = input("Please enter your password to encode:")
            new_pass = encoder(user_pass)
            print("Your password has been encoded and stored!")


        if choice == "2":
            new_pass1 = decoder(new_pass)
            print(f"The encoded password is {new_pass}, and the original password is {new_pass1}.")

        if choice == "3":
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
