#python.go

#import webbrowser functions to open Websites
import webbrowser
#import os functions to clear the screen
import os
#variable used to keep kernel running
foreverload = 1

#definition of the "SystemError()" function
def SystemError(err):
    exit(err)
#code start
#prints the tous function
print("EANDGAMES KERNEL VERSION 1.00.01\nCOPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED")
#constantly bring up the "Kernel>>>$" dialog
while (foreverload) == 1:
    mndat = input ("Kernel>>>$")
    if (mndat) == ("exit"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (mndat) == ("EXIT"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (mndat) == ("ver"):
        print("EANDGAMES KERNEL VERSION 1.00.01\nCOPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED")
    elif (mndat) == ("VER"):
        print("EANDGAMES KERNEL VERSION 1.00.01\nCOPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED")
    elif (mndat) == ("help"):
        print("HELP: SHOWS THIS MENU\nVER: SHOWS THE KERNEL VERSION\nEXIT/QUIT: EXITS KERNEL\nCOPYRIGHT [TOU | TOUS | DOCS]: TOU: FULL COPYRIGHT TERMS, TOUS: SHORT COPYRIGHT TERMS, DOCS: OPENS KERNEL DOCS IN WEB BROWSER\nCREWEB-VIEW: VIEW THE CREATORS WEBSITE")
    elif (mndat) == ("HELP"):
        print("HELP: SHOWS THIS MENU\nVER: SHOWS THE KERNEL VERSION\nEXIT: EXITS KERNEL\nCOPYRIGHT [TOU | TOUS]: TOU: FULL COPYRIGHT TERMS, TOUS: SHORT COPYRIGHT TERMS")
    elif (mndat) == ("copyright [tou]"):
        print ("COPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING EANDGAMES!\nEANDGAMES SOFTWARE LICENSE TERMS: KERNEL VERSION 1.00.01\nLAST UPDATED: 21 MAY, 2023\nTHIS SOFTWARE IS FULLY TRUSTED AS IT IS MADE IN PYTHON\nDO NOT WORRY ABOUT KERNEL DELETING AND STORING PERSONAL FILES")
    elif (mndat) == ("COPYRIGHT [TOU]"):
        print ("COPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING EANDGAMES!\nEANDGAMES SOFTWARE LICENSE TERMS: KERNEL VERSION 1.00.01\nLAST UPDATED: MAY 2023\nTHIS SOFTWARE IS FULLY TRUSTED AS SAID IN PYTHON\nDO NOT WORRY ABOUT KERNEL DELETING AND STORING PERSONAL FILES")
    elif (mndat) == ("copyright [tous]"):
        print("COPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING EANDGAMES!")
    elif (mndat) == ("COPYRIGHT [TOUS]"):
        print("COPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING EANDGAMES!")
    elif (mndat) == ("quit"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (mndat) == ("QUIT"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (mndat) == ("copyright[docs]"):
        webbrowser.open("https://sites.google.com/view/kernelofficialsite/legal/docs")
    elif (mndat) == ("COPYRIGHT[DOCS]"):
        webbrowser.open("https://sites.google.com/view/kernelofficialsite/legal/docs")
    elif (mndat) == ("creweb-view"):
        webbrowser.open("https://sites.google.com/view/eags-official")
    elif (mndat) == ("CREWEB-VIEW"):
        webbrowser.open("https://sites.google.com/view/eags-official")
    elif (mndat) == (""):
        print(" \n ")
    elif (mndat) == ("cls"):
        os.system('cls')
    elif (mndat) ==("DADDRV"):
        SystemError("INCORRECT_SYSTEM_CONFIG")
    elif (mndat) == ("daddrv"):
        SystemError("INCORRECT_SYSTEM_CONFIG")
        


    

