#!/usr/bin/python3

import os
import sys

WHERE_TO_WORK="."
HOW_MANY_IS_REQUIRED=2

print("Collecting data...")

listOfTasks = {}
for path,d,f in os.walk(WHERE_TO_WORK):
    exts = {
        ".pdf": False,
        ".html": False,
        ".mobi": False,
        ".epub": False
    }
    for filename in f:
        splited = os.path.splitext(filename)
        name = splited[0]
        ext = splited[1].lower()
        choosenName = "unavailable"
        if ext in exts:
            exts[ext] = True
            choosenName = name
    howMany = sum(1 for v in exts.values() if v==True)
    if (howMany >= HOW_MANY_IS_REQUIRED):
        newPath = os.path.dirname(path) + "/" + choosenName
        if (newPath != path):
            listOfTasks[path] = newPath

dryRun = True;
if (len(sys.argv) > 1 and sys.argv[1] == 'apply'):
    dryRun = False;

if (dryRun):
    print("Executing (dry run):")
else:
    print("Executing:")

for source,destination in listOfTasks.items():
    print(source + " -> " + destination)
    if (not dryRun):
        os.system("mv \"" + source + "\" \"" + destination + "\"")
