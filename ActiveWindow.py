from collections import defaultdict
from AppKit import NSWorkspace
from time import sleep
from time import time
import sys


lastname = ""
t = time()
knownApps = defaultdict(int)
while True:
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    if activeAppName != lastname:
        lastname = activeAppName
        knownApps[activeAppName] += int(time() - t)
        t = time()
    sleep(1)
    for k in knownApps:
        print(f"{knownApps[k]}\t{k}")
    print("*"*80)