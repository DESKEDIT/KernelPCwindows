import webbrowser
import os
foreverload = 1
syscfg = ("0")
ddc = ("0")
def SystemError(err):
    os.system('cls')
    os.system('color b0')
    print("KERNEL has ran into a problem and needs to restart...")
    print("Please refer to the StopCode and contact Support")
    print("  Stop Code: " + err)
    if (err) == ("DADDRV_CFG_ERR"):
        print("Extra notes: Try typing SETCFG in the Command Prompt before running DadDrive again.")
    os.system("pause")
    quit(err)
os.system('cls')
os.system('color 0f')
os.system('title DeskEdit Kernel')
print("DESKEDIT KERNEL VERSION 1.00.02 Beta\nBuild 0813-25a\nCOPYRIGHT(C) 2025 DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED")
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
        print("DESKEDIT KERNEL VERSION 1.00.02 Beta\nCOPYRIGHT(C) 2023 DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED")
    elif (mndat) == ("VER"):
        print("DESKEDIT KERNEL VERSION 1.00.02 BETA\nCOPYRIGHT(C) 2023 DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED")
    elif (mndat) == ("help"):
        print("HELP: SHOWS THIS MENU\nVER: SHOWS THE KERNEL VERSION\nDADDRV: START DADDRIVE(REQUIRES SETCFG FIRST!\nSETCFG: SETS THE SYSTEM CONFIGURATION VARIABLES\nCMD: STARTS A SESSION OF WINDOWS COMMAND LINE\nEXIT/QUIT: EXITS KERNEL\nCOPYRIGHT [TOU | TOUS | DOCS]: TOU: FULL COPYRIGHT TERMS, TOUS: SHORT COPYRIGHT TERMS, DOCS: OPENS KERNEL DOCS IN WEB BROWSER\nCREWEB-VIEW: VIEW THE CREATORS WEBSITE")
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
        if (syscfg[0]) == ("0"):
            SystemError("DADDRV_CFG_ERR")
        else:
            if (ddc) == ("0"):
                ddc = ["1","1","0","0","1"]
                if (ddc) == ["1","1","0","0","1"]:
                    print("----------\n|DADDRIVE|\n----------\n\nDadDrive is installed in Memory\n\nDriver: ASP KERNEL DEVICE 11001\nNAME: UDASP11001")
                else:
                    SystemError("DADDRIVE_FAIL")
            else:
                print("----------\n|DADDRIVE|\n----------\n\nDadDrive is already installed in Memory")
    elif (mndat) == ("daddrv"):
        if (syscfg[0]) == ("0"):
            SystemError("DADDRV_CFG_ERR")
        else:
            if (ddc) == ("0"):
                ddc = ["1","1","0","0","1"]
                if (ddc) == ["1","1","0","0","1"]:
                    print("----------\n|DADDRIVE|\n----------\n\nDadDrive is installed in Memory\n\nDriver: ASP KERNEL DEVICE 11001\nNAME: UDASP11001")
                else:
                    SystemError("DADDRIVE_FAIL")
            else:
                print("----------\n|DADDRIVE|\n----------\n\nDadDrive is already installed in Memory")
    elif (mndat) == ("setcfg"):
        syscfg = ["1"]
        if (syscfg) == ["1"]:
            print("System configuration set.")
        else:
            SystemError("CFG_ERRF")
    elif (mndat) == ("cmd"):
        os.system("%systemroot%\System32\cmd.exe")
    elif (mndat) == ("CMD"):
        os.system("%systemroot%\System32\cmd.exe")
    else:
        print('"' + mndat + '"' + " is an Illegal command.")
