import pyautogui
from random import randint

interval=10
linefish=1
found_fishs=0
fishes=[]
max_interval_btw_clicks=1300#1.3s

while True:
    for box in list(pyautogui.locateAllOnScreen("./src/static/fish_config.png")):
        pyautogui.click(box[0]+4,box[1]+4,duration=randint(30,max_interval_btw_clicks)/1000)
        dropdown=pyautogui.locateOnScreen("./src/static/fish_drop_down.png")
        pyautogui.sleep(0.2)
        if dropdown: 
            feed_button=pyautogui.locateOnScreen("./src/static/fish_feed.png")
            pyautogui.click(dropdown[0],dropdown[1],duration=randint(30,max_interval_btw_clicks)/1000)
            pyautogui.click(dropdown[0],dropdown[1]+42,duration=randint(30,max_interval_btw_clicks)/1000)
            pyautogui.click(feed_button[0]+4,feed_button[1]+4,duration=randint(30,max_interval_btw_clicks)/1000)
        close=pyautogui.locateOnScreen("./src/static/fish_close.png")
        pyautogui.click(close[0]+4,close[1]+4,duration=randint(30,max_interval_btw_clicks)/1000)
    pyautogui.sleep(interval)