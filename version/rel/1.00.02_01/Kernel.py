import webbrowser
import os
foreverload = 1
ddc = ("0")
ver = {"isPre": False, "build": None, "ver": "1.00.02_01", "date": {"year": 2025, "month": "August", "day": 24}}
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
os.system('cls')
os.system('title DeskEdit Kernel')
if not ver["isPre"]:
    print(f"DESKEDIT KERNEL VERSION {ver['ver']}\nCOPYRIGHT(C) {ver['date']['year']} DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED")
else:
    print(f"DESKEDIT KERNEL VERSION {ver['ver']} Beta\nBuild {ver['build']}\nCOPYRIGHT(C) {ver['date']['year']} DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED")
while (foreverload) == 1:
    args = input("Kernel>>>$").lower().split()
    if (args[0]) == ("exit"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (args[0]) == ("ver"):
        if not ver["isPre"]:
            print(f"DESKEDIT KERNEL VERSION {ver['ver']}\nCOPYRIGHT(C) {ver['date']['year']} DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED RUNNING ON")
        else:
            print(f"DESKEDIT KERNEL VERSION {ver['ver']} Beta\nBuild {ver['build']}\nCOPYRIGHT(C) {ver['date']['year']} DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED RUNNING ON")
        os.system('ver')
    elif (args[0]) == ("help"):print("HELP: SHOWS THIS MENU\nVER: SHOWS THE KERNEL VERSION\nDADDRV: START DADDRIVE\nCMD: STARTS A SESSION OF WINDOWS COMMAND LINE\nEXIT/QUIT: EXITS KERNEL\nCOPYRIGHT [TOU | TOUS | DOCS]: TOU: FULL COPYRIGHT TERMS, TOUS: SHORT COPYRIGHT TERMS, DOCS: OPENS KERNEL DOCS IN WEB BROWSER\nCREWEB-VIEW: VIEW THE CREATORS WEBSITE")
    elif (args[0]) == ("quit"):
        print("Closing KERNEL")
        quit("ExitCMDUsed")
        print("KERNEL Failed to close")
    elif (args[0]) == ("copyright"):
        if len(args) != 1:
            if (args[1]) == "[tou]":print(f"COPYRIGHT(C) {ver['date']['year']} DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING DESKEDIT!\nKERNEL VERSION {ver['ver']}\nLAST UPDATED: {ver['date']['day']} {ver['date']['month']} {ver['date']['year']}")
            elif (args[1]) == "[tous]":print(f"COPYRIGHT(C) {ver['date']['year']} DESKEDIT CORPORATIONS, ALL RIGHTS RESERVED\nTHANKS FOR CHOOSING DESKEDIT!")
            elif (args[1]) == "[docs]":webbrowser.open("https://sites.google.com/view/deskeditkernel")
            else:print("COPYRIGHT [TOU | TOUS | DOCS]: TOU: FULL COPYRIGHT TERMS, TOUS: SHORT COPYRIGHT TERMS, DOCS: OPENS KERNEL DOCS IN WEB BROWSER")
        else:
            print("COPYRIGHT [TOU | TOUS | DOCS]: TOU: FULL COPYRIGHT TERMS, TOUS: SHORT COPYRIGHT TERMS, DOCS: OPENS KERNEL DOCS IN WEB BROWSER")
    elif (args[0]) == ("creweb-view"):webbrowser.open("https://sites.google.com/view/eags-official")
    elif (args[0]) == (""):pass
    elif (args[0]) == ("cls"):os.system('cls')
    elif (args[0]) == ("daddrv"):
        if (ddc) == ("0"):
            ddc = ["0.43", "home"]
            dt = "\n\nPROGRAM CFGNAME: DAASP KERNEL DEVICE 11001\nNAME: DSP11001\nversion " + ddc[0]
            if (ddc) == (ddc):
                print("----------\n|DADDRIVE|\n----------\n\nDadDrive is installed in Memory" + dt)
            else:
                SystemError("DADDRIVE_FAIL")
        else:
            print("----------\n|DADDRIVE|\n----------\n\nDadDrive is already installed in Memory" + dt)
    elif (args[0]) == ("cmd"):os.system("%systemroot%\System32\cmd.exe")
    else:print('"' + args[0] + '"' + " is an Illegal command.")
