import time, keyboard
from pynput.mouse import Button, Controller

print("made by: ♛staMp1xel♛#1358")

mouse = Controller()

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
            mouse.click(Button.left)
            time.sleep(betweenClicks)
            try:
                if keyboard.is_pressed("x"):
                    print("You pressed a key, auto clicker terminated.")
                    break
            except:
                pass

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
        print("Press and hold 'x' for about 2 seconds to terminate auto clicker.")
        time.sleep(3)
        print("Auto clicking begins in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Auto clicking begins now!")
        # pyautogui.click(clicks=float("inf"))

        while True:
            mouse.click(Button.left)
            time.sleep(betweenClicks)
            try:
                if keyboard.is_pressed("x"):
                    print("You pressed a key, auto clicker terminated.")
                    break
            except:
                pass


    elif infinite != "N" or "Y":
        print("Please do not input anything other then N/Y")
        continue
