import webbrowser
import os
foreverload = 1
ddc = ("0")
build = "0822-25a"
def SystemError(err):
    os.system('cls')
    os.system('color b0')
    print("KERNEL has ran into a problem and needs to restart...")
    print("Please refer to the StopCode and contact Support")
    print("  Stop Code: " + err)
    if (err) == ("DADDRV_CFG_ERR"):
        print("The system seems to have not initialised properly")
    elif (err) == ("DADDRIVE_FAIL"):
        print("This copy of Kernel appears to be tampered with or has a bug in the codedadd for DADDRV. Please download it from our website by using \"CREWEB-VIEW\" in the terminal.")
os.system('color 0f')
os.system('title DeskEdit Kernel')
print("DESKEDIT KERNEL VERSION 1.00.02 Beta\nBuild 0822-25a\nCOPYRIGHT(C) 2025 DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED")
while (foreverload) == 1:
    mndat = input("Kernel>>>$").lower()
    if (mndat) == ("exit"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (mndat) == ("ver"):
        print("DESKEDIT KERNEL VERSION 1.00.02 Beta\nCOPYRIGHT(C) 2023 DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED RUNNING ON")
        os.system('ver')
    elif (mndat) == ("help"):print("HELP: SHOWS THIS MENU\nVER: SHOWS THE KERNEL VERSION\nDADDRV: START DADDRIVE(REQUIRES SETCFG FIRST!\nSETCFG: SETS THE SYSTEM CONFIGURATION VARIABLES\nCMD: STARTS A SESSION OF WINDOWS COMMAND LINE\nEXIT/QUIT: EXITS KERNEL\nCOPYRIGHT [TOU | TOUS | DOCS]: TOU: FULL COPYRIGHT TERMS, TOUS: SHORT COPYRIGHT TERMS, DOCS: OPENS KERNEL DOCS IN WEB BROWSER\nCREWEB-VIEW: VIEW THE CREATORS WEBSITE")
    elif (mndat) == ("copyright [tou]"):print ("COPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING EANDGAMES!\nEANDGAMES SOFTWARE LICENSE TERMS: KERNEL VERSION 1.00.01\nLAST UPDATED: 21 MAY, 2023\nTHIS SOFTWARE IS FULLY TRUSTED AS IT IS MADE IN PYTHON\nDO NOT WORRY ABOUT KERNEL DELETING AND STORING PERSONAL FILES")
    elif (mndat) == ("copyright [tous]"):print("COPYRIGHT(C) 2023 EANDGAMES STUDIOS CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING EANDGAMES!")
    elif (mndat) == ("quit"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (mndat) == ("copyright[docs]"):webbrowser.open("https://sites.google.com/view/kernelofficialsite/legal/docs")
    elif (mndat) == ("creweb-view"):webbrowser.open("https://sites.google.com/view/eags-official")
    elif (mndat) == (""):pass
    elif (mndat) == ("cls"):os.system('cls')
    elif (mndat) == ("daddrv"):
        if (ddc) == ("0"):
            ddc = ["0.43", "home"]
            dt = "\n\nPROGRAM CFGNAME: DAASP KERNEL DEVICE 11001\nNAME: DSP11001\nversion " + ddc[0]
            if (ddc) == (ddc):
                print("----------\n|DADDRIVE|\n----------\n\nDadDrive is installed in Memory" + dt)
            else:
                SystemError("DADDRIVE_FAIL")
        else:
            print("----------\n|DADDRIVE|\n----------\n\nDadDrive is already installed in Memory" + dt)
    elif (mndat) == ("cmd"):os.system("%systemroot%\System32\cmd.exe")
    else:print('"' + mndat + '"' + " is an Illegal command.")
