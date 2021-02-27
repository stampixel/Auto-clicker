import pyautogui, time, sys
from colorama import Fore,Style

title = Style.BRIGHT + Fore.GREEN + """                                        

                                    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╭╮
                                    ┃╭━╮┃╱╭╯╰╮╱╱╱╱╱┃┃╱╱╱╱┃┃
                                    ┃┃╱┃┣╮┣╮╭╋━━┳━━┫┃╭┳━━┫┃╭┳━━┳━╮
                                    ┃╰━╯┃┃┃┃┃┃╭╮┃╭━┫┃┣┫╭━┫╰╯┫┃━┫╭╯
                                    ┃╭━╮┃╰╯┃╰┫╰╯┃╰━┫╰┫┃╰━┫╭╮┫┃━┫┃
                                    ╰╯╱╰┻━━┻━┻━━┻━━┻━┻┻━━┻╯╰┻━━┻╯

(made by: ♛staMp1xel♛#1358    ❤️❤  ❤️❤   ❤️)
"""
print(title)


while True:
    infinite = input("Would you like the number of clicks be infinite or not (Y/N)").upper()
    if infinite == "N":
        while True:
            try:
                clicks = int(input("Please input the number of clicks you want:"))
            except ValueError:
                print("Sorry, I didn't understand that. ☹️")
                continue
            else:
                break
        while True:
            try:
                betweenClicks = float(input("Please enter the number of seconds you want between each click:"))
            except ValueError:
                print("Sorry, I didn't understand that. ☹️")
                continue
            else:
                break

        print("Auto clicking begins in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Auto clicking begins now!")
        for i in range(0, clicks):
            pyautogui.click()
            time.sleep(betweenClicks)

    elif infinite == "Y":
        # clicks = float("inf")
        while True:
            try:
                betweenClicks = float(input("Please enter the number of seconds you want between each click:"))
            except ValueError:
                print("Sorry, I didn't understand that. ☹️")
                continue
            else:
                break
        print("Press Ctrl+C to terminate...")
        print("Auto clicking begins in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Auto clicking begins now!")
        # pyautogui.click(clicks=float("inf"))
        try:
            while True:
                pyautogui.click()
                time.sleep(betweenClicks)
        except KeyboardInterrupt:
            sys.exit()
    elif infinite != "N" or "Y":
        print("Please do not input anything other then N/Y")
        continue


