import json
import hashlib
import os

def hash(input):
    m = hashlib.sha256()
    input = input.encode('ascii')
    m.update(input)
    return m.hexdigest()

def getChoice(options):
    while True:
        
        for i in range(len(options)):
            option = options[i]
            print("\033[0m",option,"\033[0m-\033[94m\033[1m", (i+1))

        choice = input("\033[0mEnter a number: \033[1m\033[94m")
        
        try: 
            choice = int(choice)
            
            if choice in range(1, len(options) +1):
                return choice
            else:
                print("\033[91mINVALID INPUT")
        except:
             print("\033[91mINVALID INPUT")

def hobbies():
    print()
    print("\033[0m\033[4m\033[1mMY HOBBIES\033[0m")
    print()
    
    for hobby in data['hobbies']:
        print("\033[92m  I spend", data['hobbies'][hobby]['hours per week'], "hours per week", hobby)
        print("  I think I am", data['hobbies'][hobby]['skill level'], "out of 10 in", hobby)
        print()

def foods():
    print()
    print("\033[0m\033[4m\033[1mMY FAVOURITE FOODS\033[0m")
    print()
    
    for food in data['foods']:
        print("\033[92m  I eat", food, data['foods'][food]['how often per week'], "times per week")
        print("In my opinion,", food + "s a", data['foods'][food]['how much i like it'], "out of 10")
        print()

def friends():
    print()
    print("\033[0m\033[4m\033[1mMY FRIENDS\033[0m")
    print()
    f = ", ".join(data['friends'])
    print("\033[92mMy friends are", f + ".")
    print()
    addRemove=input("\033[94mInfo\033[0m/\033[92mAdd\033[0m/\033[91mRemove\033[0m friend (Leave blank to cancel): ").upper()
    
    if addRemove == "ADD":
        enter = input("\033[92mInput name to add friend: ").capitalize()
        otherFriends = []
        running = True

        while running:
            enter2 = input("Input name of " + enter + "'s friend: ").capitalize()
           
            if enter2 == "Cancel":
                running = False
            else:
                otherFriends.append(enter2)
        
        print("\033[92mSuccessfully added",enter,"and their friends\033[0m")

        data['friends'][enter] = otherFriends
    
    elif addRemove == "REMOVE":
        enter = input("\033[91mInput name to remove friend: ").capitalize()

        if enter in data['friends']:
            data['friends'].pop(enter, None)
            print("\033[91m\033[1mSuccessfully removed", enter, "\033[0m")
        else:
            print("INVALID NAME")

    elif addRemove == "INFO":
        enter = input("\033[94mInput name to get info of friend: ").capitalize()
 
        if enter in data['friends']:
            e = ", ".join(data['friends'][enter])
            print("\033[92m" + enter, "is best friends with", e)
        else:
            print("\033[91mINVALID NAME")
    
    elif addRemove == "":
        print("\033[91mCancelled")
    else:
        print()
        print("\033[91m\033[1mList of commands")
        commands = ["\033[91m\033[1mAdd - Add a friend", "Remove - Remove a friend", "(Leave blank) - cancel\033[0m"]
        
        for command in commands:
            print(command)
        friends()

def family():
    print()
    print("\033[0m\033[4m\033[1mMY FAMILY\033[0m")
    print()
    familyList=["Cancel"]
    for member in data['family']:
        print("\033[92mMy", data['family'][member]['who'],"is",member)
        print(member,"is very", data['family'][member]['personality'])
        print()
        familyList.append(member)
    print("For more information:")
    print()
    
    number=getChoice(familyList)
    if number == 1:
        print("Returning to menu.")
    else:
        name = familyList[number-1]
        
        print ("What I like about",name,"is that",data['family'][name]['what i like about them'])

#############################
path = "./data"
dir_list = os.listdir(path)

for i in range(len(dir_list)):
    dir_list[i] = dir_list[i].replace(".json","")

name = getChoice(dir_list) - 1

waitingForPassword=True

file = open('./data/' + dir_list[name] + '.json', 'r+')
data = json.load(file)

while waitingForPassword:
    password= input("Enter your password: ")
    password = hash(password)
    
    if password == data['password']:
           waitingForPassword = False
    else: 
        print("\033[91mINCORRECT PASSWORD PLEASE TRY AGAIN")


is_running = True

while is_running:
    print()
    print("\033[0m\033[4m\033[1mABOUT ME")
    print()
    page = getChoice([
        "Close Code",
        "Family",
        "Friends",
        "Hobbies",
        "Favourite Foods"
    ])
    
    if page == 1:
        is_running=False
    elif page == 2:
        family()
    elif page == 3:
        friends()
    elif page == 4:
        hobbies()
    elif page == 5:
        foods()
        
if name == 1:
    file = open('./data/elliott.json', 'w')
elif name == 2:
    file = open('./data/george.json', 'w')

json.dump(data, file)
file.close()