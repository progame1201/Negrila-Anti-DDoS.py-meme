import sys
from this import s
from time import sleep
import os
# inports
os.system('TITLE NADpy')  # title

print ("────────── /")
sleep(0.2)
os.system('CLS') 
print ("━───────── |")
sleep(0.2)
os.system('CLS') 
print ("━━──────── \ ")
sleep(0.2)
os.system('CLS') 
print ("━━━─────── - ")
sleep(0.2)
os.system('CLS') 
print ("━━━━────── /")
sleep(0.2)
os.system('CLS') 
print ("━━━━━───── |")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━──── \ ")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━─── - ")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━── /")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━── |")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━━─ \ ")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━━━ - ")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━━━ /")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━━━ |")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━━━ \ ")
sleep(0.2)
os.system('CLS') 
print ("━━━━━━━━━━ - ")
sleep(0.2)
os.system('CLS') 
print("NAD.py 1.1") # version
sleep(2)
os.system('CLS')
print("|\    |     /\     ###      ███ █   █")
print("| \   |    /  \    #  #    █  █  █ █ ")
print("|  \  |   -----#   #  #    ███    █  ")
print("|   \ |  /      #  #  #    █      █  ")
print("|    \| /        # ###  ▄  █      █  ")
print("")
print("---  |---  \   /   |    | |---   |---\      /\     ----- |--- ");
print("|    |      \ /    |    | |   \  |   |     /  \      |   |    ");
print("---  |---   / \    |    | |---   |   |    ------     |   |--- ");
print("  |  |     /   \   |    | |      |   |   /      \    |   |    ");
print("---  |--- /     \  |----| |      |---/  /        \   |   |--- ");
print("")
print("System is online. NADpy 1.1.1, progame1201")
print("type help to see all commands")
st = False
usn = 0 # - user name
usp = 0 # - user password
usc = 0 # - user created?
login = False # - LogIn
ips = False # - ip seted?
ip = False # - ip 
i100 = False
if i100 == True :
   print("and now you fucked 1000000000000 people!");
while True: 
  S = input() # s - input command
  if S == "start" : 
    if st == False :
     sleep(1);
     print("Opening Negrila Anti-DDoS");
     print("loading settings of anti ddos"); 
     sleep(2);
     print("successfully");
     sleep(1);
     print(" ");
     if ips == False :
      print("████████████████████████████████")
      print("██")
      print("██ Negrila Anti-DDoS started")
      print("██       IP: 0.0.0.0")
      print("██")
      print("██")
      print(" ");
      st = True # st - started
      S = 0;
     else :
      print("████████████████████████████████")
      print("██")
      print("██ Negrila Anti-DDoS started")
      print("██       IP: " + ip)
      print("██")
      print("██")
      print(" ");
      st = True # st - started
      S = 0;

  if S == "stop" :
    if st == True : 
      print("stoping");
      sleep(2);
      print("stoping");
      sleep(1);
      print(" ");
      print("████████████████████████████████")
      print("██")
      print("██ Negrila Anti-DDoS stoped")
      print("██")
      print("██")
      print("██")
      print(" ");
      st = False
      S = 0;

  if S == "help" :
     print("")
     print("start - start Anti-DDoS")
     print ("stop - Stop Anti-DDoS")
     print ("clear - clear the terminal")
     print ("adduser - add user")
     print ("su - now you can be user")
     print ("myuser - your user is...")
     print("system - information of system")
     print("setip - set ip")
     print("exit - exit")
     print("restart - restart the program")
     print ("i.. i dont know what this command doing")
     S = 0;
  if S == "Log" :
    print("Loging of valuves")
    print(S)
    print (st)
    print(usn)
    print(usp)
    print(usc)
    print(login)
    print(ip)
    print(ips)
  if S == "clear" :
     os.system('CLS')
     print("|\    |     /\     ###      ███ █   █");
     print("| \   |    /  \    #  #    █  █  █ █ ");
     print("|  \  |   -----#   #  #    ███    █  ");
     print("|   \ |  /      #  #  #    █      █  ");
     print("|    \| /        # ###  ▄  █      █  ");
     print("");
     print("---  |---  \   /   |    | |---   |---\      /\     ----- |--- ");
     print("|    |      \ /    |    | |   \  |   |     /  \      |   |    ");
     print("---  |---   / \    |    | |---   |   |    ------     |   |--- ");
     print("  |  |     /   \   |    | |      |   |   /      \    |   |    ");
     print("---  |--- /     \  |----| |      |---/  /        \   |   |--- ");
     print("")
     print("System is online. NADpy 1.1.1, progame1201");
     print("type help to see all commands");
     S = 0
     if i100 == True :
         print("")
         print("and now you fucked 1000000000000 people!")
  if S == "adduser" :
    usn = input("User name:")
    usp = input("User password:")
    print("user created!")
    usc = True
    S = 0
  if S == "su" :
    if usc == True :
     ssu = input("User name:")
     ssp = input("User password:")
     if ssu == usn :
        if ssp == usp :
          print("You are logined")
          login = True
          S = 0
        else :
         print("invalid password")
     else :
      print("invalid user name")
    else :
     print("You don't create account")
       
  if S == "myuser" :
      print(usn)
  if S == "system" :
    print("██████████████████████████")
    print("")
    print("NADpy system 1.1.0")
    print(os.system('ver'))
    print("██████████████████████████")
  if S == "setip" :
    ip = input("IP:")
    if len(ip) > 15 :
       print ("Error in ip format")
       ips = False
       continue
    else :
      print("IP seted")
      ips = True
  if S == "restart" :
      print ("")
      print ("closing programs...")
      sleep(2)
      os.system('CLS') 
      sleep(5)
      print ("────────── /")
      sleep(0.2)
      os.system('CLS') 
      print ("━───────── |")
      sleep(0.2)
      os.system('CLS') 
      print ("━━──────── \ ")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━─────── - ")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━────── /")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━───── |")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━──── \ ")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━─── - ")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━── /")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━── |")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━━─ \ ")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━━━ - ")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━━━ /")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━━━ |")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━━━ \ ")
      sleep(0.2)
      os.system('CLS') 
      print ("━━━━━━━━━━ - ")
      sleep(0.2)
      os.system('CLS') 
      print("NAD.py 1.1") # version
      sleep(2)
      os.system('CLS')
      print("|\    |     /\     ###      ███ █   █")
      print("| \   |    /  \    #  #    █  █  █ █ ")
      print("|  \  |   -----#   #  #    ███    █  ")
      print("|   \ |  /      #  #  #    █      █  ")
      print("|    \| /        # ###  ▄  █      █  ")
      print("")
      print("---  |---  \   /   |    | |---   |---\      /\     ----- |--- ");
      print("|    |      \ /    |    | |   \  |   |     /  \      |   |    ");
      print("---  |---   / \    |    | |---   |   |    ------     |   |--- ");
      print("  |  |     /   \   |    | |      |   |   /      \    |   |    ");
      print("---  |--- /     \  |----| |      |---/  /        \   |   |--- ");
      print("")
      print("System is online. NADpy 1.1.1, progame1201")
      print("type help to see all commands")
      st = False
      usn = 0 
      usp = 0 
      usc = False 
      login = False 
      ips = False 
      ip = False 
      if i100 == True :
         print("")
         print("and now you fucked 1000000000000 people!");
  if S == "exit" :
      sys.exit()
  if S == "i100" :
      os.system('CLS')
      sleep(4)
      print("i fucked 100 people!")
      sleep(0.5)
      os.system('CLS')
      print("i fucked 200 people!")
      sleep(0.5)
      os.system('CLS')
      print("i fucked 500 people!")
      sleep(0.5)
      os.system('CLS')
      print("i fucked 1000 people!")
      sleep(1)
      os.system('CLS')
      print("i fucked 5000 people!")
      sleep(1)
      os.system('CLS')
      print("i fucked 10000 people!")
      sleep(2)
      os.system('CLS')
      print("i fucked 20000 people!")
      sleep(1.5)
      os.system('CLS')
      print("i fucked 70000 people!")
      sleep(1.5)
      os.system('CLS')
      print("i fucked 100000 people!")
      sleep(2.5)
      os.system('CLS')
      print("i fucked 300000 people!")
      sleep(2.5)
      os.system('CLS')
      print("i fucked 600000 people!")
      sleep(2.5)
      os.system('CLS')
      print("i fucked 800000 people!")
      sleep(2.5)
      os.system('CLS')
      print("i fucked 900000 people!")
      sleep(5)
      os.system('CLS')
      print("i fucked 999999 people!")
      sleep(3)
      os.system('CLS')
      print("i fucked 1000000 people!")
      sleep(4)
      os.system('CLS')
      print("i fucked 10000000 people!")
      sleep(4)
      os.system('CLS')
      print("i fucked 1000000000 people!")
      sleep(4)
      os.system('CLS')
      print("i fucked 10000000000 people!")
      sleep(5)
      os.system('CLS')
      print("i fucked 1000000000000 people!")
      sleep(3)
      os.system('CLS')
      sleep(1)
      print (" / ")
      sleep(0.1)
      os.system('CLS') 
      print (" | ")
      sleep(0.1)
      os.system('CLS') 
      print (" \ ")
      sleep(0.2)
      os.system('CLS') 
      print (" - ")
      sleep(0.1)
      os.system('CLS') 
      print (" / ")
      sleep(0.1)
      os.system('CLS') 
      print (" | ")
      sleep(0.1)
      os.system('CLS') 
      print (" \ ")
      sleep(0.2)
      os.system('CLS') 
      print (" - ")
      sleep(0.1)
      os.system('CLS') 
      print (" / ")
      sleep(0.2)
      os.system('CLS') 
      print (" | ")
      sleep(0.1)
      os.system('CLS') 
      print (" \ ")
      sleep(0.1)
      os.system('CLS') 
      print (" - ")
      sleep(0.1)
      os.system('CLS') 
      print (" / ")
      sleep(0.1)
      os.system('CLS') 
      print (" | ")
      sleep(0.1)
      os.system('CLS') 
      print (" \ ")
      sleep(0.1)
      os.system('CLS') 
      print (" - ")
      sleep(0.1)
      os.system('CLS') 
      sleep(3)
      print (".")
      sleep(1.5)
      os.system('CLS') 
      print ("..")
      sleep(1.5)
      os.system('CLS') 
      print ("...")
      sleep(1.5)
      os.system('CLS') 
      print("Hello!")
      sleep(2)
      print("|\    |     /\     ###      ███ █   █")
      print("| \   |    /  \    #  #    █  █  █ █ ")
      print("|  \  |   -----#   #  #    ███    █  ")
      print("|   \ |  /      #  #  #    █      █  ")
      print("|    \| /        # ###  ▄  █      █  ")
      print("")
      print("---  |---  \   /   |    | |---   |---\      /\     ----- |--- ");
      print("|    |      \ /    |    | |   \  |   |     /  \      |   |    ");
      print("---  |---   / \    |    | |---   |   |    ------     |   |--- ");
      print("  |  |     /   \   |    | |      |   |   /      \    |   |    ");
      print("---  |--- /     \  |----| |      |---/  /        \   |   |--- ");
      print("")
      print("and now you fucked 1000000000000 people!")
      i100 = True
