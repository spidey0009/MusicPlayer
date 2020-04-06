import os
print("Welcome to the music player")
while True:
    option=int(input("Enter 1 - Alan Walker-Alone\n"
                 "Enter 2 - PUBG\n"
                 "Enter 3 - Attention\n"
                 "Enter any number to quit"))
    if option==1:
        file="Alone.mp3"
        os.system(file)
    elif option==2:
        fil2="C:\\Users\\Shlok\\Desktop\\PUBG.mp3"
        os.system(fil2)
    elif option==3:
        fil3="C:\\Users\\Shlok\\Desktop\\Attention.mp3"
        os.system(fil3)
    else:
        quit()



