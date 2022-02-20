import time
import string
import requests
from bs4 import BeautifulSoup

D4SV2 = "https://intl-outdoor.com/tint-ramping-instant-channel-swiching-led-flashlights/new-emisar-d4s-v2-with-tint-ramping-instant-channel-switching.html"

def checkstock():
    html_text = requests.get(D4SV2).text
    soup = BeautifulSoup(html_text, "html.parser")

    stockid = soup.find('select', id = 'select_137').text

    #print(stockid)
    print()
    print("Colors in stock: " + stockid[19:35])
    print()

    stockid = stockid.lower()

    color_picker = input("What color's stock do you want to check?: ")

    if(color_picker in stockid):
        color_picker = string.capwords(color_picker)
        print()
        print(color_picker + " Tint Ramping/Channel Switching D4SV2 IS in stock")
        print()
        time.sleep(2)
        input("Press any key to exit")
    else:
        color_picker = string.capwords(color_picker)
        print()
        print(color_picker + " Tint Ramping/Channel Switching D4SV2 is NOT in stock")
        print()
        time.sleep(2)
        input("Press any key to exit")

    time.sleep(60)
    checkstock()
