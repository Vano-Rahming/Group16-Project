import random
from time import time
from hashlib import sha256


class blockChain(object):
    # Input verification was successful this some points for security.
    # diff_level = input("Please set difficulty Level the Range is 00 - 00000:\n")
    # try:
    #     diff_level = int(diff_level)
    # except:
    #     print("Your input was not an integer please rerun the program and try again.")
    #     exit()
    #
    # if diff_level != 00 or diff_level != 000 or diff_level != 0000 or diff_level != 00000:
    #     print("difficulty level invalid please rerun the program to start again")
    #     exit()

    counter = 0

    while True:  # This is the parent while loop. This runs the program

        while True:  # This is the first child while loop. This while loop contains the Login security
            print("Welcome to Inventory Inc! Please Login")
            login_name = input("Username: ")
            login_Password = input("Password: ")
            if login_Password == "admin" and login_name == "admin":
                print("Welcome admin!")
                break
            else:
                print("Account not found")
                counter += 1

            if counter == 3:
                print("Login timeout, please rerun and try again.")
                exit()

        bChain = []
        inventory = []
        unit = 0
        index = 0
        hash = ""
        while True:  # This is the second child while loop. This while loop contains the functionality of the program
            userInput = input("Hello what would you like to do?\nAdd(1), Remove(2), Display(3):\n")
            userInput = int(userInput)
            if userInput == 1:
                print("Your option was code 1 (add)")
            elif userInput == 2:
                print("Your option was code 2 (Remove)")
            elif userInput == 3:
                print("Your option was code 3 (display)")

            if userInput == 1:
                while True:
                    nonce = random.randint(0, 99)
                    placer = []
                    block_recorder = []
                    print("You can now add an item!")
                    item = input("Please enter item: ")
                    amount = input("Please enter the amount: ")
                    sender = input("Who is storing the item: ")  # Digital signature
                    unit += 1
                    placer.append("Unit:" + str(unit))
                    placer.append("Item:" + item)
                    placer.append("amount:" + amount)
                    placer.append("sender:" + sender)
                    inventory.append(placer)

                    index += 1
                    hashString = item + amount + sender + str(unit)
                    hash = sha256(hashString.encode('utf-8')).hexdigest()
                    block_recorder.append("Previous Hash:" + hash)
                    block_recorder.append("index:" + str(index))
                    block_recorder.append("Nonce" + str(nonce))
                    block_recorder.append("Timestamp:" + str(time()))
                    block_recorder.append("unit:" + str(unit))
                    bChain.append(block_recorder)
                    print(inventory)
                    print("Blockchain was updated")

                    userInput_add = input("Would you like to go back to the main page? y or n\n")
                    if userInput_add == 'y':
                        break
                    elif userInput_add == 'n':
                        continue
                    else:
                        print("Invalid input")
                        continue

            elif userInput == 2:
                while True:
                    i = 0
                    Remove_counter = 1
                    block_recorder = []
                    nonce = random.randint(0, 99)
                    print("You can now remove a unit!")
                    print("Your inventory is currently ", len(inventory), " unit\nTo remove an unit use the digits")
                    while i < len(inventory):
                        print(i, " For unit ", Remove_counter)
                        i += 1
                        Remove_counter += 1

                    userInput_remove = input("Which unit do you want to remove?\n")
                    userInput_remove = int(userInput_remove)
                    inventory.pop(userInput_remove)
                    print("The inventory now looks like this:\n", inventory)

                    index += 1
                    hash = sha256(hash.encode('utf-8')).hexdigest()
                    block_recorder.append("Previous Hash:" + hash)
                    block_recorder.append("index:" + str(index))
                    block_recorder.append("Nonce" + str(nonce))
                    block_recorder.append("Timestamp:" + str(time()))
                    block_recorder.append("Action:Remove")
                    bChain.append(block_recorder)
                    print("Blockchain was updated")
                    userInput_remove = input("Would you like to go back to the main page? y or n\n")
                    if userInput_remove == 'y':
                        break
                    elif userInput_remove == 'n':
                        continue
                    else:
                        print("Invalid input")
                        continue

            elif userInput == 3:
                while True:
                    print("Do you want to display the inventory or the blockchain Records?:\nInventory(1), Blockchain "
                          "Records(2)")
                    userInput_edit = input()
                    userInput_edit = int(userInput_edit)
                    if userInput_edit == 1:
                        print("Here is the inventory:")
                        print(inventory)
                    elif userInput_edit == 2:
                        i = 0
                        edit_counter = 1
                        print("which Block do you want to see: ")
                        while i < len(bChain):
                            print(i, " For unit ", edit_counter)
                            i += 1
                            edit_counter += 1
                        print("Or type the word 'all' to list the full block")
                        userInput_edit = input()
                        try:
                            userInput_edit = int(userInput_edit)
                        except:
                            if userInput_edit == "all":
                                print("Here is the full BlockChain")
                                print(bChain)

                        try:
                            print(bChain[userInput_edit])
                        except:
                            if userInput_edit == "all":
                                continue
                            else:
                                print("Invalid option")

                        userInput_add = input("Would you like to go back to the main page? y or n\n")
                        if userInput_add == 'y':
                            break
                        elif userInput_add == 'n':
                            continue
                        else:
                            print("Invalid input")
                            continue

            else:
                while True:
                    userInput = input("Sorry that input was invalid! Would you like to continue? y or n:\n")
                    print("Your option code was ", userInput)
                    if userInput == 'y':
                        break
                    elif userInput == 'n':
                        exit()
                    else:
                        print("Please type the letter y for yes or the letter n for no")
                        continue


if __name__ == '__main__':
    blockChain()
