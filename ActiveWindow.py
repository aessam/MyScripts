from AppKit import NSWorkspace
from time import sleep
from time import time
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: SCRIPT output_file.txt")

file = open(sys.argv[1],"a")
lastname = ""
t = time()
while True:
   activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
   if activeAppName != lastname:
       if lastname:
           file.write("\n" + "% 10d" % (int(time() - t),) + "\t" + lastname)
       lastname = activeAppName
       t = time()
       file.flush()

   sleep(1)
