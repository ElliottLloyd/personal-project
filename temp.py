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
        for x in range(len(options)):
            option = options[x]
            print("\033[0m",option,"\033[0m-\033[94m", (x+1))

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
    for o in data['hobbies']:
        print("\033[92m  I spend",data['hobbies'][o]['hours per week'],"hours per week",o)
        print("  I think I am",data['hobbies'][o]['skill level'],"out of 10 in",o)
        print()

def foods():
    print()
    print("\033[0m\033[4m\033[1mMY FAVOURITE FOODS\033[0m")
    print()
    
    for i in data['foods']:
        print("\033[92m  I eat",i,data['foods'][i]['how often per week'],"times per week")
        print("In my opinion,",i+"s a",data['foods'][i]['how much i like it'],"out of 10")
        print()

def friends():
    print()
    print("\033[0m\033[4m\033[1mMY FRIENDS\033[0m")
    print()
    mysep = ", "
    sep = ""
    x = mysep.join(data['friends'])
    print("\033[92mMy friends are",x+".")
    print()
    addRemove=input("\033[94mInfo\033[0m/\033[92mAdd\033[0m/\033[91mRemove\033[0m friend (Leave blank to cancel): ").upper()
    if addRemove == "ADD":
        enter = input("\033[92mInput name to add friend: ")
        enter1 = enter.capitalize()
        #data['friends'].update(enter1:enter2)
        otherFriends = []

        running = True
        while running:
            enter2 = input("Input name of "+enter1+"'s friend: ")
            enter2=enter2.capitalize()
           
            if enter2 == "Cancel":
                running = False
            else:
                otherFriends.append(enter2)
        
        print("\033[92mSuccessfully added",enter1,"and their friends\033[0m")

        data['friends'][enter1]=otherFriends
    
    elif addRemove == "REMOVE":
        enter = input("\033[91mInput name to remove friend: ")
        enter1 = enter.capitalize()
        if enter1 in data['friends']:
            data['friends'].pop(enter1, None)
            print("\033[91m\033[1mSuccessfully removed",enter1, "\033[0m")
        else:
            print("INVALID NAME")
    elif addRemove == "INFO":
        enter = input("\033[94mInput name to get info of friend: ").capitalize()
        if enter in data['friends']:
            e = mysep.join(data['friends'][enter])
            print("\033[92m"+enter,"is best friends with", e)
        else:
            print("\033[91mINVALID NAME")
    elif addRemove == "":
        print("\033[91mCancelled")
    else:
        print()
        print("\033[91m\033[1mList of commands")
        list = ["\033[91m\033[1mAdd - Add a friend", "Remove - Remove a friend", "(Leave blank) - cancel\033[0m"]
        for b in list:
            print(b)
        friends()

def family():
    print()
    print("\033[0m\033[4m\033[1mMY FAMILY\033[0m")
    print()
    for f in data['family']:
        print("\033[92mMy",data['family'][f]['who'],"is",f)
        print(f,"is very",data['family'][f]['personality'])
        print()
    print("For more information:")
    print()
    list=["Cancel","Robin","Helen","Simon"]
    number=getChoice(list)
    if number == 1:
        print("Returning to menu.")
    else:
        if number == 2:
            name = "Robin"
        if number ==3:
            name = "Helen"
        if number == 4:
            name = "Simon"
        print ("What I like about",name,"is that",data['family'][name]['what i like about them'])

###############################
path = "./data"
dir_list = os.listdir(path)
for i in range(len(dir_list)):
    dir_list[i] = dir_list[i].replace(".json","")

e = getChoice(dir_list) - 1

waitingForPassword=True

f = open('./data/' + dir_list[e] + '.json', 'r+')
data = 
while waitingForPassword:
    password = hash(password)
    if password == data['password']:
           waitingForPassword=False
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
        
if e == 1:
    f = open('./data/elliott.json', 'w')
elif e == 2:
    f = open('./data/george.json', 'w')
json.dump(data, f)
f.close()