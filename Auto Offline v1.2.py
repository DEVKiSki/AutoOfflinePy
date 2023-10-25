import os

os.system("color 1")

import pickle
with open("config_autooff", "rb") as pickle_file:
    color_mai = pickle.load(pickle_file)

import ctypes

ctypes.windll.kernel32.SetConsoleTitleW('Auto Offline v1.2 by KiSki')

def drawMenu():
    os.system("color " + color_mai)
    os.system("cls")

    print("       ___         __           ____  ___________                        ")
    print("      /   | __  __/ /_____     / __ \/ __/ __/ (_)___  ___               ")
    print("     / /| |/ / / / __/ __ \   / / / / /_/ /_/ / / __ \/ _\               ")
    print("    / ___ / /_/ / /_/ /_/ /  / /_/ / __/ __/ / / / / /  __/              ")
    print("   /_/  |_\__,_/\__/\____/   \____/_/ /_/ /_/_/_/ /_/\___/               ")
    print("        by KiSki                   V. 1.2                                ")
    print("                                                                         ")
    print("                                                                         ")
    print("   [1] Seconds                                                           ")
    print("   [2] Minutes                                                           ")
    print("   [3] Hours                                                             ")
    print("   [4] Days                                                              ")
    print("   [5] Weeks                                                             ")
    print("   [6] Advanced                                                          ")
    print("                                                                         ")
    print("   [S] Settings                                                          ")
    print("   [E] Exit                                                              ")
    print("                                                                         ")


drawMenu()

while True:

    option = input("   > ")

    if option == "1":
        #seconds
        os.system("cls")
        basic_sec = input("Time in Seconds: ")
        print("Press any key to continue...")
        input("")
        os.system("shutdown -s -t " + str(basic_sec))
        print("Your PC are stopping " + str(basic_sec) + " Seconds")
        print("")
        print("Thanks for using Auto Offline by KiSki!")
        print("Join Our Discord Server for Updates and More! https://discord.gg/7qTcubBrxZ")
        print("")


    elif option == "2":
        #minutes
        os.system("cls")
        basic_minu = input("Time in Minutes: ")
        basic_min = int(basic_minu) * 60
        os.system("shutdown -s -t " + str(basic_min))
        print("Your PC are stopping " + str(basic_min) + " Seconds")
        print("")
        print("Thanks for using Auto Offline by KiSki!")
        print("Join Our Discord Server for Updates and More! https://discord.gg/7qTcubBrxZ")
        input("")
        exit(2)

    elif option == "3":
        #hours
        os.system("cls")
        basic_hours = input("Time in Hours: ")
        basic_hour = int(basic_hours) * 60 * 60
        os.system("shutdown -s -t " + str(basic_hour))
        print("Your PC are stopping " + str(basic_hour) + " Seconds")
        print("")
        print("Thanks for using Auto Offline by KiSki!")
        print("Join Our Discord Server for Updates and More! https://discord.gg/7qTcubBrxZ")
        input("")
        exit(3)

    elif option == "4":
        #days
        os.system("cls")
        basic_days = input("Time in Days: ")
        basic_day = int(basic_days) * 60 * 60 * 24
        os.system("shutdown -s -t " + str(basic_day))
        print("Your PC are stopping " + str(basic_day) + " Seconds")
        print("")
        print("Thanks for using Auto Offline by KiSki!")
        print("Join Our Discord Server for Updates and More! https://discord.gg/7qTcubBrxZ")
        input("")
        exit(4)

    elif option == "5":
        #weeks
        os.system("cls")
        basic_weeks = input("Time in Weeks: ")
        basic_week = int(basic_weeks) * 60 * 60 * 24 * 7
        os.system("shutdown -s -t " + str(basic_week))
        print("Your PC are stopping " + str(basic_week) + " Seconds")
        print("")
        print("Thanks for using Auto Offline by KiSki!")
        print("Join Our Discord Server for Updates and More! https://discord.gg/7qTcubBrxZ")
        input("")
        exit(5)

    elif option == "6":
            #advenced
            os.system("cls")
            print("       ___         __           ____  ___________                        ")
            print("      /   | __  __/ /_____     / __ \/ __/ __/ (_)___  ___               ")
            print("     / /| |/ / / / __/ __ \   / / / / /_/ /_/ / / __ \/ _\               ")
            print("    / ___ / /_/ / /_/ /_/ /  / /_/ / __/ __/ / / / / /  __/              ")
            print("   /_/  |_\__,_/\__/\____/   \____/_/ /_/ /_/_/_/ /_/\___/               ")
            print("        by KiSki                   V. 1.2                                ")
            print("                                                                         ")
            print("                                                                         ")
            print("   [] Soon...                                                           ")

            while True:
                settings = input(" > ")
                if settings == "F22":
                    print("Developer mode activate")
                    exit(69)
                print("Soon...")
                input("")
                exit(1)

    elif option.lower() == "e":
        #exit
        os.system("cls")
        exit(7)

    elif option.lower() == "s":
        #Settings MainMenu
        os.system("cls")
        print("         ")
        print(" Colors    [1]  ")
        print(" About Us  [2]  ")
        print(" Back      [E]  ")
        print("         ")

        while True:
            settings = input(" > ")
            if settings == "1":
                    #Color
                    os.system("cls")
                    print(" Color 01 [DEFAULT]")
                    print(" Color 02          ")
                    print(" Color 03          ")
                    print(" Color 04          ")
                    print(" Color 05          ")
                    print(" Color 06          ")
                    print(" Color 07          ")
                    print(" Color 08          ")
                    print(" Color 09          ")
                    print(" Color 10          ")
                    print(" Color 11          ")
                    print(" Color 12          ")
                    print(" Color 13          ")
                    print(" Color 14          ")
                    print(" Color 15          ")
                    print(" Color 16          ")
                    print("                   ")
                    print(" Youre currently using color ")
                    print(" Test a color [T]  ")
                    print("")

                    while True:
                        color = input(" > ")

                        if color.lower() == "t":
                            #Color-Test
                            os.system("cls")
                            print(" Which Color will you Test? ")
                            print("")
                            print(" Color 1 [DEFAULT]")
                            print(" Color 2          ")
                            print(" Color 3          ")
                            print(" Color 4          ")
                            print(" Color 5          ")
                            print(" Color 6          ")
                            print(" Color 7          ")
                            print(" Color 8          ")
                            print(" Color 9          ")
                            print(" Color 10         ")
                            print(" Color 11         ")
                            print(" Color 12         ")
                            print(" Color 13         ")
                            print(" Color 14         ")
                            print(" Color 15         ")
                            print(" Color 16         ")
                            print("                  ")

                            while True:
                                color_test = input(" > ")
                                if color_test == "1":
                                    os.system("cls")
                                    os.system("color 1")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 1 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "2":
                                    os.system("cls")
                                    os.system("color 2")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 2 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "3":
                                    os.system("cls")
                                    os.system("color 3")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 3 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "4":
                                    os.system("cls")
                                    os.system("color 4")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 4 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "5":
                                    os.system("cls")
                                    os.system("color 5")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 5 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()


                                elif color_test == "6":
                                    os.system("cls")
                                    os.system("color 6")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 6 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "7":
                                    os.system("cls")
                                    os.system("color 7")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 7 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "8":
                                    os.system("cls")
                                    os.system("color 8")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 8 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "9":
                                    os.system("cls")
                                    os.system("color 9")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 9 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "9":
                                    os.system("cls")
                                    os.system("color 9")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then press 9 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "10":
                                    os.system("cls")
                                    os.system("color 10")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then type 10 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "11":
                                    os.system("cls")
                                    os.system("color 11")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then type 11 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "12":
                                    os.system("cls")
                                    os.system("color 12")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then type 12 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "13":
                                    os.system("cls")
                                    os.system("color 13")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then type 13 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "14":
                                    os.system("cls")
                                    os.system("color 14")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then type 14 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "15":
                                    os.system("cls")
                                    os.system("color 15")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then type 15 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()

                                elif color_test == "16":
                                    os.system("cls")
                                    os.system("color 16")
                                    print("")
                                    print("Thanks for Using Auto Offline by KiSki")
                                    print("Check out our Discord for Updates and More: https://discord.gg/7qTcubBrxZ")
                                    print("Or go in Settings > About Us > And then Click 1 for Discord")
                                    print("")
                                    print("If you want this one: ")
                                    print("go again in Settings > Colors > Then type 16 and then Enter")
                                    print("")
                                    print("End Test? ")
                                    input("")
                                    drawMenu()


                        elif color == "1":
                            import pickle
                            color_main = "1"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "2":
                            import pickle

                            color_main = "2"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "3":
                            import pickle

                            color_main = "3"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "4":
                            import pickle

                            color_main = "4"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "5":
                            import pickle

                            color_main = "5"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "6":
                            import pickle

                            color_main = "6"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "7":
                            import pickle

                            color_main = "7"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "8":
                            import pickle

                            color_main = "8"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "9":
                            import pickle

                            color_main = "9"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "10":
                            import pickle

                            color_main = "10"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "11":
                            import pickle

                            color_main = "11"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "12":
                            import pickle

                            color_main = "12"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "13":
                            import pickle

                            color_main = "13"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "14":
                            import pickle

                            color_main = "14"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "15":
                            import pickle

                            color_main = "15"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)

                        elif color == "16":
                            import pickle

                            color_main = "16"
                            with open("config_autooff", "wb") as pickle_file:
                                pickle.dump(color_main, pickle_file)
                                with open("config_autooff", "rb") as pickle_file:
                                    color_mai = pickle.load(pickle_file)
                                    exit(11)


            elif settings == "E":
                drawMenu()

            elif settings == "e":
                drawMenu()

            elif settings == "2":
                #Social Media
                print(" Discord [1]")
                print(" YouTube [2]")
                print(" Twitch  [3]")
                print(" TikTok  [4]")
                print("            ")
                print(" Back    [E]")
                print("            ")

                while True:
                    team = input(" > ")
                    if team == "1":
                        os.system("start https://discord.gg/7qTcubBrxZ ")

                    elif team == "2":
                        os.system("start https://www.youtube.com/channel/UCxIZgQEZeEHrkF3bmU5dSJQ ")

                    elif team == "3":
                        os.system("start https://www.twitch.tv/killerskiller_ ")

                    elif team == "4":
                        os.system("start https://vm.tiktok.com/ZMLE7uHuL/ ")

                    elif team == "E":
                        os.system("cls")
                        drawMenu()

                    elif team == "e":
                        os.system("cls")
                        drawMenu()
    os.system("cls")
    drawMenu()
