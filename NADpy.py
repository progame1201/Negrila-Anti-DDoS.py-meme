from time import sleep
import ctypes
import os 
# inports
os.system('TITLE NADpy')  # title

print("NAD.py 1.0") # version
sleep(2)
print("#  # ### #   #   ### #")
print("#  # #   #   #   # # #")
print("#### ### #   #   # # #")
print("#  # #   #   #   # # ")
print("#  # ### ### ### ### #")
sleep(2)
os.system('CLS') 

print("|\    |     /\     ###     ███  █   █")
print("| \   |    /  \    #  #    █  █  █ █")
print("|  \  |   -----#   #  #    ███    █")
print("|   \ |  /      #  #  #    █      █")
print("|    \| /        # ###  ██ █      █")

print("System is online. NADpy 1.0.0, progame1201")
print("type help to see all commands")
st = False
usn = 0 # - user name
usp = 0 # - user password
usc = False # - user created?
login = False # - LogIn
while True: 
  S = input() # s - input command
  if S == "start" : 
    if st == False :
     sleep(1);
     print("Opening Negrila Anti-DDoS");
     print("Opened Negrila Anti-DDoS"); 
     sleep(2);
     print("successfully");
     sleep(1);
     print("##########################################")
     print("          Negrila Anti-DDoS system")
     print("                 launched")
     print("        Anti-DDoS runed to IP: 0.0.0.0")
     print("##########################################")
     st = True # st - started
     S = 0;

  if S == "stop" :
    if st == True : 
      print("stoping");
      sleep(2);
      print("stoping");
      sleep(1);
      print("Negrila Anti-DDoS system stoped");
      st = False
      S = 0;

  if S == "help" :
     print("start - start Anti-DDoS")
     print ("stop - Stop Anti-DDoS")
     print ("clear - clear the terminal")
     print ("adduser - add user")
     print ("su - now you can be user")
     print ("myuser - your user is...")
     S = 0;
  if S == "Log" :
    print(S)
    print (st)
    print(usn)
    print(usp)
    print(usc)
    print(login)
  if S == "clear" :
   os.system('CLS')
   print("|\    |     /\     ###     ███  █   █")
   print("| \   |    /  \    #  #    █  █  █ █")
   print("|  \  |   -----#   #  #    ███    █")
   print("|   \ |  /      #  #  #    █      █")
   print("|    \| /        # ###  ██ █      █")
 
   print("System is online. NADpy 1.0.0, progame1201")
   print("type help to see all commands")
   S = 0
  if S == "adduser" :
    usn = input("User name:")
    usp = input("User password:")
    print("user created!")
    usc = True
    S = 0
  if S == "su" :
    ssu = input("User name:")
    ssp = input("User password:")
    if ssu == usn :
        if ssp == usp :
            if usc == True :
              print("You are logined")
              login = True
              S = 0
    else:
        print("Information not correct")
              
  if S == "myuser" :
      print(usn)
    
