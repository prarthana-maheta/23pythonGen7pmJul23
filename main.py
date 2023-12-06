import pyautogui,time
while True:
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
        time.sleep(.2)
    pyautogui.keyUp('alt')
    time.sleep(300)