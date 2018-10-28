import os
import sys
import difflib

print "Welcome to Python Shell"


def cd(command):
    if len(command) == 2:
        if os.path.isdir(command[1]):
            if os.access(command[1], os.X_OK):
                os.chdir(command[1])
            else:
                print "Permission Denied"
        else:
            print "Invalid Path"
    else:
        print "Invalid Argument"


def ls(command):
    if len(command) == 1:
        if os.access(os.getcwd(), os.R_OK):
            files = os.listdir(".")
            for fname in files:
                if fname[0] != '.':
                    print fname
        else:
            print "Permission Denied"
    elif len(command) == 2:
        if os.path.isdir(command[1]):
            if os.access(command[1], os.R_OK):
                files = os.listdir(command[1])
                for fname in files:
                    print fname
            else:
                print "Permission Denied"
        else:
            print "Invalid Path"
    else:
        print "Invalid Argument"


def pwd(command):
    if len(command) == 1:
        print os.getcwd()
    else:
        print "Invalid Argument"


def touch(command):
    if len(command) >= 2:
        for i in command:
            if i == "touch":
                continue
            index = i.rfind("/")
            if index == -1:
                if os.access(os.getcwd(), os.W_OK):
                    open(i, "a").close()
                    os.utime(i, None)
                else:
                    print "Permission Denied"

            else:
                path = i[:index]
                if os.path.isdir(path):
                    if os.access(path, os.W_OK):
                        open(i, "a").close()
                        os.utime(i, None)
                    else:
                        print "Permission Denied"
                else:
                    print "Invalid Path"
    else:
        print "Invalid Argument"


def prRed(skk): sys.stdout.write("\033[91m{}\033[00m" .format(skk))


def grep(command):
    command = command[4:]
    try:
        ps = command.split("<<<")
        ps[0] = ps[0][2:len(ps[0])-2]
        ps[1] = ps[1][2:len(ps[1])-1]
        f=0
        while ps[1].find(ps[0]) != -1:
            x = ps[1].find(ps[0])
            sys.stdout.write(ps[1][0:x])
            prRed(ps[1][x:x+len(ps[0])])
            x = x+len(ps[0])
            ps[1] = ps[1][x:]
            f=1
        if f==1:
            sys.stdout.write(ps[1])
        print
    except:
        print "Invalid Syntex"


def head(command):
    if len(command) >= 2:
        for fname in command:
            if fname == "head":
                continue
            print "FileName-----", fname
            if os.path.isfile(fname):
                if os.access(fname, os.R_OK):
                    with open(fname) as f:
                        lines = f.readlines()
                    i = 0
                    for content in lines:
                        if i <= 10:
                            sys.stdout.write(content)
                        else:
                            break
                        i = i+1
                else:
                    print "Permission Denied"
            else:
                print "File does not exist"
    else:
        print "Invalid Argument"


def tail(command):
    if len(command) >= 2:
        sys.stdout.flush()
        for fname in command:
            if fname == "tail":
                continue
            print "FileName-----", fname
            if os.path.isfile(fname):
                if os.access(fname, os.R_OK):
                    with open(fname) as f:
                        lines = f.readlines()
                    i = 0
                    newlist = []
                    lines.reverse()
                    for content in lines:
                        if i <= 10:
                            newlist.append(content)
                        else:
                            break
                        i = i+1
                    newlist.reverse()
                    for i in newlist:
                        sys.stdout.write(i)
                else:
                    print "Permission Denied"
            else:
                print "File does not exist"
    else:
        print "Invalid Argument"


def tr(command):
    if len(command) == 3:
        print "$ to quit from tr command"
        while 1:
            inp = raw_input()
            if inp != '$':
                list1 = []
                list2 = []
                for i in command[1]:
                    list1.append(i)
                for i in command[2]:
                    list2.append(i)
                store = dict(zip(list1, list2))
                j = 0
                if len(list1) > len(list2):
                    for i in list1:
                        if j >= len(list2):
                            store[i] = list2[len(list2)-1]
                        else:
                            j = j+1
                #print store
                for i in inp:
                    if i in store:
                        sys.stdout.write(store[i])
                    else:
                        sys.stdout.write(i)
            else:
                break
    else:
        print "Invalid Argument"


def sed(command):
    print "Sed Command"


def diff(command):
    if len(command) == 3:

        if os.path.isfile(command[1]) and os.path.isfile(command[2]):

            if os.access(command[1], os.R_OK) and os.access(command[2], os.R_OK):
                # dd=difflib.ndiff(open(command[1]).readlines(),open(command[1]).readlines())
                # print ''.join(dd),

                with open(command[1]) as f:
                    lines = f.readlines()

                with open(command[2]) as f:
                    lines1 = f.readlines()

                getdiff = list(set(lines) - set(lines1))
                getdiff1 = list(set(lines1) - set(lines))
                print "FileName----", command[1]
                for i in getdiff:
                    sys.stdout.write(i)
                print "FileName----", command[2]
                for i in getdiff1:
                    sys.stdout.write(i)
            else:
                if os.access(command[1], os.R_OK):
                    print "Second file does not have read permission"
                elif os.access(command[2], os.R_OK):
                    print "First file does not have read permission"
                else:
                    print "Both files does not have read permission"
        else:
            if os.path.isfile(command[1]):
                print "Second file does not exist"
            elif os.path.isfile(command[2]):
                print "First file does not exist"
            else:
                print "Both files does not exist"

    else:
        print "Invalid Argument"


while 1:
    sys.stdout.flush()
    user_command = raw_input("Enter command\n")
    user_command = user_command.strip()
    if user_command == "":
        print "Please Enter Something"
        continue
    command = user_command.split()
    if command[0] == "cd":
        cd(command)
    elif command[0] == "ls":
        ls(command)
    elif command[0] == "pwd":
        pwd(command)
    elif command[0] == "touch":
        touch(command)
    elif command[0] == "grep":
        grep(user_command)
    elif command[0] == "head":
        head(command)
    elif command[0] == "tail":
        tail(command)
    elif command[0] == "tr":
        tr(command)
    elif command[0] == "sed":
        sed(command)
    elif command[0] == "diff":
        diff(command)
    elif command[0] == "exit":
        break
    else:
        print "Invalid command"

print "Thank You!!!"
