from numpy.core.fromnumeric import put
import pyautogui
import time

path = "E:\\HP\\Desktop\\"

if __name__ == "__main__":
    while True:
        try:
            pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(path + 'guanbi.png',confidence=0.9))) # 
            time.sleep(0.5)
            pyautogui.click()
        except:
            pass
        