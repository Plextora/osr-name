from osrparse import parse_replay_file
from osrparse import dump_replay_file

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

        replay = parse_replay_file(osrEditNamePath)

        print("Insert player name for .osr file (example: RyuK)")
        print("")

        replay.player_name = input("")
        dump_replay_file(replay, osrEditNamePath)

        print("")
        print("Replay has been saved. Open the replay file you picked and it will be updated with the player's name!")
    except:
        print("osr!name has run into a fatal error! Is your .osr corrupted? Did you select a .osr file?")

editName()
