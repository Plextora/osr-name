import osrtools

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print('''

░█████╗░░██████╗██████╗░██╗███╗░░██╗░█████╗░███╗░░░███╗███████╗
██╔══██╗██╔════╝██╔══██╗██║████╗░██║██╔══██╗████╗░████║██╔════╝
██║░░██║╚█████╗░██████╔╝██║██╔██╗██║███████║██╔████╔██║█████╗░░
██║░░██║░╚═══██╗██╔══██╗╚═╝██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░
╚█████╔╝██████╔╝██║░░██║██╗██║░╚███║██║░░██║██║░╚═╝░██║███████╗
░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
''')

def editName():
    try:
        osrEditNamePath = filedialog.askopenfilename()

        with open(osrEditNamePath, "rb") as f:
            replay = osrtools.parsef(f)

        print("Insert player name for .osr file (example: RyuK)")
        print("")

        replay.player_name = input("")

        with open(osrEditNamePath, "wb") as f:
            osrtools.dumpf(f, replay)

        print("")
        print("Replay has been saved. Open the replay file you picked and it will be updated with the player's name!")
    except:
        print("osr!name has run into a fatal error! Is your .osr corrupted? Did you select a .osr file?")

editName()
