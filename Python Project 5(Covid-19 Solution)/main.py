# In window to display notification we have differnet modues we are going to use the plyer moduels
""""
Author: Bablu
Date: 28 july 2020
Purpose: Learning the practical implementaion of covid 19 notification on the windows machine
"""
# pip install plyer

# if you wnat to runt everyhour then keep into the while loop

from plyer import notification
from bs4 import BeautifulSoup
import time
# soup = BeautifulSoup(html_doc, 'html.parser')

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="icon.ico",
        timeout=10
    )

def getdata(url):
    import requests
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    # notifyMe("Bablu ", "Let get it done")
    myHtmlData = getdata("https://www.mohfw.gov.in/")
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())
    myDatastr = ""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        #print(tr.get_text())
        myDatastr = tr.get_text()
    myDatastr = myHtmlData[1:]
    itemlist = myDatastr.split("\n\n")

    states = ['chandighar','telangana','haryana','telangana']
    for item in itemlist[0:22]:
        datalist = item.split("\n")
        if datalist[1] in states:
            print(datalist)
            nTitle = 'Cases of Covid 19'
            nText = f" State {datalist[1]} \n Indian: {datalist[2]} \n Foriegn : {datalist[3]}  \n  Cured : {datalist[4]}\n Deaths:{datalist[5]}\n"
            notifyMe(nTitle,nText)
            time.sleep(5)
        #print(item)



