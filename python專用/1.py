from selenium import webdriver
from selenium.webdriver.common.by import By



def nprint(np,npn):
    npl=0
    npl=len(np)
    for kk in range(npl):
        print(np[kk],end="")
    print("",end=npn)
def go(got):
    gotime=[]
    for t in range(len(got)):
        if got[t].text!="":
            gotime.append(got[t].text)
    for e in range(len(gotime)//10):
        fh=[]
        by=[]
        gy=[]
        for f in range(10):
            k=0
            k=(f+1)%10
            if gotime[f+e*10]=="正常白":
                fh.append(k)
            elif gotime[f+e*10]=="場外白":
                by.append(k)
            elif gotime[f+e*10]=="場內黑":
                gy.append(k)
                fh.append(k)
            else:
                pass
        if e==4 and by==[] and gy==[]:
            fh=["尾派全出"]
        nprint(fh," ")
        if by != []:
            nprint(by,"+ ")
        if gy!=[]:
            nprint(gy,"- ")
        print("")

browser = webdriver.Chrome()
browser.get("https://avalon.signage-cloud.org/")
hatg=int(input("最後玩到第幾輪(請輸入1~5):"))
whatg=0
if hatg==1:
    whatg=3
elif hatg==2 or hatg== 3:
    whatg=4
elif hatg== 4 or hatg== 5:
    whatg = 5

import time
from selenium.webdriver.common.action_chains import ActionChains
time.sleep(1)
name = browser.find_element(By.CLASS_NAME,'form-control')
name.send_keys("牌譜機器人")
time.sleep(1)
a=browser.find_element(By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-block.btn-signin")
a.click()

time.sleep(1)

#如果房間在第一個就用這一條V

try:
    b=browser.find_element(By.CSS_SELECTOR,"body > div > div > div:nth-child(1) > div.col-md-9 > ul > li > div > div:nth-child(3) > button")
except:
    b=browser.find_element(By.CSS_SELECTOR,"body > div > div > div:nth-child(1) > div.col-md-9 > ul > li > div:nth-child(7) > div:nth-child(2) > button > span")

#如果房間在第二個就用這一條V
#b=browser.find_element(By.CSS_SELECTOR,"body > div > div > div:nth-child(1) > div.col-md-9 > ul > li:nth-child(2) > div > div:nth-child(3) > button > span")
#警急用
#b=browser.find_element(By.CSS_SELECTOR,"body > div > div > div:nth-child(1) > div.col-md-9 > ul > li:nth-child(1) > div:nth-child(7) > div:nth-child(2) > button")
b.click()

time.sleep(1)
c=browser.find_element(By.CSS_SELECTOR,"body > div.container-fluid > div > div.col-sm-7 > div:nth-child(2) > div:nth-child(1) > button")

cwgo=browser.find_elements(By.CLASS_NAME,"btn.btn-primary")
wgo=[]
for lkl in range(len(cwgo)):
    if cwgo[lkl].text !="":
        wgo.append(cwgo[lkl].text)

gbp=browser.find_elements(By.CLASS_NAME,"img-rounded")
wgbp=[]
"""
for ngbp in range(len(gbp)):
    if gbp[ngbp].get_attribute('src') !="":
        wgbp.append(gbp[ngbp].get_attribute('src'))
"""
for ngbp in range(len(gbp)):
    if gbp[ngbp].get_attribute('src') =="https://avalon.signage-cloud.org/image/good_cup.jpg":
        wgbp.append("O")
    if gbp[ngbp].get_attribute('src') =="https://avalon.signage-cloud.org/image/bad_cup.jpg":
        wgbp.append("X")

try:
    c.click()
    time.sleep(1)
    d0=browser.find_elements(By.CSS_SELECTOR,"span[style='color: green;'], span[style='color: red;']")
    go(d0)
    c=browser.find_element(By.CSS_SELECTOR,"#game_statistics_modal > div > div > div.modal-body > div > ul > li:nth-child(2) > a")
    print(wgo[1],wgo[2],wgo[3],"=>",wgbp[whatg+0],wgbp[whatg+1],wgbp[whatg+2])
except:
    pass
try:
    c.click()
    time.sleep(1)
    d1=browser.find_elements(By.CSS_SELECTOR,"span[style='color: green;'], span[style='color: red;']")
    go(d1)
    print(wgo[4],wgo[5],wgo[6],wgo[7],"=>",wgbp[whatg+3],wgbp[whatg+4],wgbp[whatg+5],wgbp[whatg+6])
except:
    pass
try:
    c=browser.find_element(By.CSS_SELECTOR,"#game_statistics_modal > div > div > div.modal-body > div > ul > li:nth-child(3) > a")
    c.click()
    time.sleep(1)
    d2=browser.find_elements(By.CSS_SELECTOR,"span[style='color: green;'], span[style='color: red;']")
    go(d2)
    print(wgo[8],wgo[9],wgo[10],wgo[11],"=>",wgbp[whatg+7],wgbp[whatg+8],wgbp[whatg+9],wgbp[whatg+10])
except:
    pass    
try:
    c=browser.find_element(By.CSS_SELECTOR,"#game_statistics_modal > div > div > div.modal-body > div > ul > li:nth-child(4) > a")
    c.click()
    time.sleep(1)
    d3=browser.find_elements(By.CSS_SELECTOR,"span[style='color: green;'], span[style='color: red;']")
    go(d3)
    print(wgo[12],wgo[13],wgo[14],wgo[15],wgo[16],"=>",wgbp[whatg+11],wgbp[whatg+12],wgbp[whatg+13],wgbp[whatg+14],wgbp[whatg+15])
except:
    pass
try:
    c=browser.find_element(By.CSS_SELECTOR,"#game_statistics_modal > div > div > div.modal-body > div > ul > li:nth-child(5) > a")
    c.click()
    time.sleep(1)
    d4=browser.find_elements(By.CSS_SELECTOR,"span[style='color: green;'], span[style='color: red;']")
    go(d4)
    print(wgo[17],wgo[18],wgo[19],wgo[20],wgo[21],"=>",wgbp[whatg+16],wgbp[whatg+17],wgbp[whatg+18],wgbp[whatg+19],wgbp[whatg+20])
except:
    pass
goti=[]
whoplay=[]
whoplay=browser.find_elements(By.XPATH,'//p[@align="center"]')
for lll in range(len(whoplay)):
    if whoplay[lll].text!="":
        goti.append(whoplay[lll].text)
#print(goti)
l10=goti[6]
l9=goti[7]
goti[7]=goti[9]
goti[6]=goti[8]
goti[9]=l10
goti[8]=l9

npl=0
npl=len(goti)
for kk in range(npl):
    print(kk+1,"家",goti[kk])
"""
print(goti)
print(wgo)
print(wgbp)
"""

