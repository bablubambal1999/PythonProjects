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
        timeout=6
    )

def getdata(url):
    import requests
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    # notifyMe("Bablu ", "Let get it done")
    myHtmlData = getdata("https://www.mygov.in/covid-19#info-2")
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup)
    mystringdata = ""
    for item in soup.find_all(id="stateCount"):
        mystringdata = item.get_text()

        #print(item.get_text())
    #print(mystringdata)
    mystringdata = mystringdata.split("\n")
    #print(mystringdata)
    mystringdata = [string for string in mystringdata if len(string)!=0]
    print(mystringdata)
    states = [ "Andhra Pradesh","Haryana","Madhya Pradesh","Telengana"]
    for item in range(len(mystringdata)):
        if mystringdata[item] in states:
            ntitle = "Covid 19 State wise Status India 2020 "
            nText = f" State is :{mystringdata[item]} \nTotal infected: {mystringdata[item+1]} \nConfirmed : {mystringdata[item+2]}  \nActive: {mystringdata[item+3]} \nRecoverd: {mystringdata[item+4]} \nDeceased {mystringdata[item+5]} \n "
            notifyMe(ntitle, nText)
            time.sleep(15)





    #mystringdata = mystringdata[1:]
    #print(mystringdata[1])
    # andhra = mystringdata[1].split("\n")
    # #an = mystringdata[1].split("\n")
    # #print(an)
    # print(andhra)
    # ntitle = "Covid 19 State wise Status"
    # nText = f" State is :{andhra[1]} and infected are: {andhra[2]}"
    #
    #
    # notifyMe(ntitle, nText)










