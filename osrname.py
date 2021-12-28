import osrparse
import os

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
        osrEditNamePath = filedialog.askopenfilename()

        replay = osrparse.parse_replay_file(osrEditNamePath)

        print("Insert player name for .osr file (example: RyuK)")
        print("")

        replay.player_name = input(">> ")

        replay.dump(osrEditNamePath)

        print("")
        print("Replay has been saved. Open the replay file you picked and it will be updated with the player's name!")

editName()
