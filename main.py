import time
import randfacts
import webbrowser
import sys
import os
import pyjokes
import random

def wait(sec):
    time.sleep(sec)

print("""

███████╗░█████╗░░░███╗░░
╚════██║██╔══██╗░████║░░
░░███╔═╝╚██████║██╔██║░░
██╔══╝░░░╚═══██║╚═╝██║░░
███████╗░█████╔╝███████╗
╚══════╝░╚════╝░╚══════╝
"""
)
wait(4)
print(f"A free fact just because you opened Z91 MEDCH: \n \n{randfacts.get_fact()}")
print("")
wait(3)
print("""

█░█ █▀▀ █░░ █▀█   █▀█ ▄▀█ █▄░█ █▀▀ █░░
█▀█ ██▄ █▄▄ █▀▀   █▀▀ █▀█ █░▀█ ██▄ █▄▄
__________
""")
print("")
wait(2)
print("1) Cmd - opens your command prompt.")
print("2) NGGYU - Something you don't want")
wait(3)
print("3) pjk - Not funny jokes that only programmers will understand")
print("4) fttk - It will bring you 25 random facts.")
wait(3)
print("5) uwbs - Opens 15 usefull & Useless websites.")
print("6) psg - Password Generator, which will generate 5 funny passwords for you!")
print("7) exit - For exiting Z91")
print("8) help - For seeing all these again.")
wait(4)

while True:
    print("")
    ask = input(">> ")

    if ask.lower() == "cmd":
        print("\nI am opening your command propt here, type exit to exit from that command propt and to come back here!")
        os.system("C:\\windows\\system32\cmd.exe")

    elif ask.lower() == "nggyu":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        wait(4)

    elif ask.lower() == "pjk":
        wait(2)
        print(f"\n{pyjokes.get_joke()}")
        wait(1)
        print(f"\n{pyjokes.get_joke()}")
        wait(1)
        print(f"\n{pyjokes.get_joke()}")
        wait(1)
        print(f"\n{pyjokes.get_joke()}")
        wait(1)
        print(f"\n{pyjokes.get_joke()}")
        wait(3)

    elif ask.lower() == "fttk":
        print("")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        wait(3)
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        wait(3)
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        wait(3)
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        wait(3)
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        print(f"\n{randfacts.get_fact()}")
        wait(3)

    elif ask.lower() == "uwbs":
        wait(3)
        print("\nLaunching all the websites...")
        wait(3)
        webbrowser.open("https://neal.fun/")
        webbrowser.open("https://thispersondoesnotexist.com/")
        webbrowser.open("http://radio.garden/")
        webbrowser.open("https://windowswap.com/")
        webbrowser.open("https://sreeharitheprogrammer.github.io/Mirdaco/")
        webbrowser.open("http://www.desktop-destroyer.net/")
        webbrowser.open("http://www.keyprank.com/")
        webbrowser.open("https://fakeupdate.net/")
        webbrowser.open("https://www.16personalities.com/")
        webbrowser.open("http://slither.io/")
        webbrowser.open("https://www.windows93.net/")
        webbrowser.open("https://en.akinator.com/")
        webbrowser.open("https://www.plot-generator.org.uk/")
        webbrowser.open("https://www.wolframalpha.com/")
        webbrowser.open("https://www.boredbutton.com/")
        wait(3)
        print("\nAll websites launched!")
        wait(2)

    elif ask.lower() == "psg":
        wait(3)
        adjs = ["brave", "smart", "dumb", "scary", "fatty", "white", "Proffessor", "King"]
        nouns = ["Elephant", "Dino", "Lion", "Deer", "Bear", "Spider"]
        verbs = ["sleeping", "dancing", "Studying", "Playing", "Jumping", "Exercising"]

        pas1 = "".join(random.choice(adjs)+random.choice(nouns)+"Is"+random.choice(verbs))
        pas2 = "".join(random.choice(adjs)+random.choice(nouns)+"Is"+random.choice(verbs))
        pas3 = "".join(random.choice(adjs)+random.choice(nouns)+"Is"+random.choice(verbs))
        pas4 = "".join(random.choice(adjs)+random.choice(nouns)+"Is"+random.choice(verbs))
        pas5 = "".join(random.choice(adjs)+random.choice(nouns)+"Is"+random.choice(verbs))

        print(f"\nThe first password is : {pas1}73")
        print(f"\nThe second password is : {pas2}37")
        print(f"\nThe third password is : {pas3}52")
        print(f"\nThe fourth password is : {pas4}53")
        print(f"\nThe fifth password is : {pas5}35")
        wait(3)

    elif ask.lower() == "win_shts":
        webbrowser.open()

    elif ask.lower() == "exit":
        sys.exit()

    elif ask.lower() == "help":
        print("")
        wait(3)
        print("""

        █░█ █▀▀ █░░ █▀█   █▀█ ▄▀█ █▄░█ █▀▀ █░░
        █▀█ ██▄ █▄▄ █▀▀   █▀▀ █▀█ █░▀█ ██▄ █▄▄
        __________
        """)
        print("")
        wait(2)
        print("1) Cmd - opens your command prompt.")
        print("2) NGGYU - Something you don't want")
        wait(3)
        print("3) pjk - Not funny jokes that only programmers will understand")
        print("4) fttk - It will bring you 25 random facts.")
        wait(3)
        print("5) uwbs - Opens 15 usefull & Useless websites.")
        print("6) psg - Password Generator, which will generate 5 funny passwords for you!")
        print("7) exit - For exiting Z91")
        print("8) help - For seeing all these again.")
        wait(4)

    else:
        print("\nCommand Not Found.")