from sys import argv
import os
from pathlib import Path

user_home = str(Path.home())


def doesCategoryExists(category):
    for cat in os.listdir(user_home + "/.TTIS/"):
        if (cat == category):
            return True
    return False


def listCat():
    for cat in os.listdir(user_home + "/.TTIS/"):
        print(cat.rstrip(".data"))


def initRequired():
    print("You should init your directory first for more info -h")


try:
    a = open(user_home + "/.TTIS/dir.conf", "r")
    setup_dir = a.readlines()[0]
    a.close()
except:
    initRequired()


def usage():
    print(
        "Hello There, welcome to the Things That I Should(TTIS) created by : ze0tron  \ninit -----  * init * for first usage \nadd ---- * category_name add task * adds a task to the category example : do add homework \nlist ---- * category_name list *  lists the content of the category example : learn list  \ndone -----* category_name done  task *  set an task as done and deletes it from category example : watch done Batman_The_Dark_Knight\nlistcat ----- *listcat* lists all categories\ndelcat ----- *delcat category_name* deletes the category with the given name example : delcat watch"
    )


def parseInput():
    if (len(argv) == 1):
        usage()
    #Init
    if (len(argv) == 2):
        if (argv[1] == "init"):
            try:
                os.mkdir(user_home + "/.TTIS")
            except:
                nothing = 0
            c = open(user_home + "/.TTIS/dir.conf", 'w')
            print("v1.0", file=c)
            c.close()
        elif (argv[1] == "listcat"):
            listCat()
    #List
    elif (len(argv) == 3):
        if (argv[2] == "list"):
            if (not doesCategoryExists(argv[1] + ".data")):
                print("This category doesn't exists")
            else:
                c = open(user_home + "/.TTIS/" + argv[1] + ".data", 'r')
                for line in c.readlines():
                    print(line.rstrip())
                c.close()
        elif (argv[1] == "delcat"):
            os.remove(user_home + "/.TTIS/" + argv[2] + ".data")
        #Add
    elif (len(argv) == 4):
        if (argv[2] == "add"):
            if (not doesCategoryExists(argv[1] + ".data")):
                c = open(user_home + "/.TTIS/" + argv[1] + ".data", 'w')
                c.close()

            c = open(user_home + "/.TTIS/" + argv[1] + ".data", 'r')
            duplicate_flag = False
            for line in c.readlines():
                if (line.rstrip() == argv[3]):
                    print("It is already in the list")
                    duplicate_flag = True
                    break
            c.close()
            if (not duplicate_flag):
                c = open(user_home + "/.TTIS/" + argv[1] + ".data", "a+")
                print(argv[3], file=c)
            c.close()
        #Done
        elif (argv[2] == "done"):
            if (not doesCategoryExists(argv[1] + ".data")):
                print("This category doesn't exists")
            else:
                c = open(user_home + "/.TTIS/" + argv[1] + ".data", 'r')
                not_found = False
                lines = []
                for line in c.readlines():
                    if (line.rstrip() != argv[3]):
                        lines.append(line.rstrip())
                    else:
                        not_found = True
                c.close()
                if (not not_found):
                    print("This task is not in this category")
                else:
                    c = open(user_home + "/.TTIS/" + argv[1] + ".data", 'w')
                    for line in lines:
                        print(line, file=c)
                    c.close()
    if (len(argv) == 2 and argv[1] == "-h"):
        usage()


parseInput()
