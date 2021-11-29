import os, sys, subprocess, pyautogui
import urllib.request

from random import randint
from datetime import datetime

discord_name="berrytern#6619"
interval=2
linefish=5
found_fishs=0
fishes=[]
max_interval_btw_clicks=100#1.3s
exp_date=datetime(2021,11,30,12,46)
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
def get_file(file):
    return os.path.abspath(os.path.join(bundle_dir, file))
def GetUUID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid

def check_change(box):
    tries=0
    change=False
    print(box)
    color=pyautogui.pixel(int(box[0]),int(box[1]))
    while not change and tries<10:
        if color!=pyautogui.pixel(int(box[0]),int(box[1])):
            change=True
        tries+=1
        pyautogui.sleep(0.2)
def run():
    print("STARTING BOT!!!")
    while True:
        pos=pyautogui.locateOnScreen(get_file("fish_config.png"))
        if pos:
            pyautogui.scroll(1800, pos[0],pos[1])
            pos=pyautogui.locateOnScreen(get_file("fish_config.png"))
            if pos:
                for line in range(linefish):
                    boxes=list(pyautogui.locateAllOnScreen(get_file("fish_config.png"),region=(0,pos[1],1800,40)))
                    for box in boxes:
                        if boxes:
                            pyautogui.click(box[0]+4,box[1]+4,duration=randint(30,max_interval_btw_clicks)/1000)
                        check_change(box)
                        dropdown=pyautogui.locateOnScreen(get_file("fish_drop_down.png"))
                        if dropdown: 
                            feed_button=pyautogui.locateOnScreen(get_file("fish_feed.png"))
                            if feed_button:
                                print("FEEDING FISH")
                                pyautogui.click(dropdown[0],dropdown[1],duration=randint(30,max_interval_btw_clicks)/1000)
                                pyautogui.click(dropdown[0],dropdown[1]+42,duration=randint(30,max_interval_btw_clicks)/1000)
                                pyautogui.click(feed_button[0]+4,feed_button[1]+4,duration=randint(30,max_interval_btw_clicks)/1000)
                        close=pyautogui.locateOnScreen(get_file("fish_close.png"))
                        if close:
                            pyautogui.click(close[0]+4,close[1]+4,duration=randint(30,max_interval_btw_clicks)/1000)
                        #print("box")
                    [pyautogui.press('down') for i in range(5)]
                    pyautogui.sleep(0.2)
        pyautogui.sleep(interval)

hwids = urllib.request.urlopen("https://raw.githubusercontent.com/berrytern/hwid/main/_ctft").read().decode("utf-8") .splitlines()
if(GetUUID() in hwids):
    if datetime.utcnow()>exp_date:
        print("TIME EXPIRED")
        #[os.remove(i) for i in os.listdir() if i.endswith(".exe")]
        print("contact us on discord to get extra time\n"+discord_name)
        pyautogui.sleep(4)
        exit()
    else:
        print("AUTHORIZED")
        pyautogui.sleep(3)
        run()
else:
    print("UNAUTHORIZED")
    pyautogui.sleep(4)
    exit()
