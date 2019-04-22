#!/usr/bin/python3
# connect.py
# Author: Nate Sales (@nwsnate)

import os
import sys
import termtool

CONFILE = "/home/nate/.conrc"

db = {}

with open(CONFILE, 'r') as servers:
    # Loads db with servers from the specified file.
    for server in servers:
        server = server.split(':')
        db[server[0]] = server[1]

def main():
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print(termtool.event("Usage: c [server/command] {server}", termtool.Level.MID, timestamp=False))
        exit(1)

    try:
        arg2 = sys.argv[2]
    except IndexError:
        arg2 = None

    if arg1 in db and not arg2:
        os.system(db[arg1])

    elif arg1 == "list":
        for server in db:
            print(termtool.event(server, termtool.Level.SUCCESS, timestamp=False))
        exit()

    elif arg2 == "gen":
        print(db[arg1].strip())

    elif arg2 == "ping": # TODO: Make this cross platform.
        os.system("ping " + db[arg1].strip("ssh").split('@')[1].strip() + " -c 1")

    elif arg2 == "trace": # TODO: Make this cross platform.
        os.system("traceroute " + db[arg1].strip("ssh").split('@')[1].strip() + "")

    else:
        print(termtool.event("Command " + arg1 + " not found.", termtool.Level.MID, timestamp=False))

if __name__ == "__main__":
    main()
