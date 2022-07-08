from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import time

class getgpa:
    def apply(self,id, passwordd):
        #heroku的chrome driver
        GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        time.sleep(0.5)
        
        #browser = webdriver.Chrome("D:/google_download/chromedriver_win32/chromedriver.exe")
        browser.get('https://sys.ndhu.edu.tw/CTE/Ed_StudP_WebSite/Login.aspx')

        print("2")
        window_before = browser.window_handles[0]
        print(f"start fetching from {id}")
        student_id = id
        password = passwordd
        credits = list()
        grades = list()
        name = list()
        convert = {'A+': 4,'A': 4, 'A-': 3.67 , 'B+': 3.33, 'B': 3,'B-': 2.67,'C+': 2.33,'C': 2, 'C-': 1.67, 'D': 1.33, 'E': 0}
        credit = 0
        gp = 0
        print("3")
        try:
            #帳號
            std_id = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtUID"]')
            std_id.send_keys(student_id)
            #密碼
            passwordd= browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtPassword"]')
            passwordd.send_keys(password)
        except:
            browser.close()
            browser.quit()
            print("登入失敗")
            return(0,0,[])
        #登入
        try:
            print("4")
            browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_imgbtnLogin"]').click()
            time.sleep(1.2)
            browser.find_element_by_xpath('/html/body/form[2]/div[4]/div/ul/li[3]/a').click()
            time.sleep(1.2)
            window_after = browser.window_handles[1]
            time.sleep(1)
            browser.switch_to_window(window_after)
        except:
            browser.close()
            browser.quit()
            print("卡住")
            return("可能一次太多人用，卡住了QQ","再試一次",[])
        print("5")
        time.sleep(0.5)
        try:
            browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_YearSemeDDList"]/option[@value="0:0"]').click()
        except:
            browser.close()
            browser.quit()
            print("找無成績")
            return(0,0,[])
        time.sleep(0.5)
        html = browser.page_source
        
        soup = BeautifulSoup(html, 'html.parser')
        print("6")
        try:
            for td in soup.find_all("td"):
                if td.get('data-th') == "成績":
                    grades.append(td.text.replace(' ',''))
                if td.get('data-th') == "學分":
                    credits.append(float(td.text.replace(' ','')))
                if td.get('data-th') == "科目名稱":
                    name.append(td.text.replace(' ',''))
        except:
            browser.close()
            browser.quit()
            print("data錯誤")
            return(0,0,[])
        print("7")
        last60credits = 0
        pass60 = 0
        last60gp = 0
        try:
            for i in range(len(credits)):
                if grades[i] in convert:
                    gs = convert[grades[i]]
                    credit += credits[i]
                    gp += gs*credits[i]
                else:
                    continue
            print("8")
            for i in range(len(credits)):
                pass60 += credits[i]
                if pass60 >= sum(credits)-60:
                    if grades[i] in convert:
                        gs = convert[grades[i]]
                        last60credits += credits[i]
                        last60gp += gs*credits[i]       
                else:
                    continue
        except:
            browser.close()
            browser.quit()
            return(0,0,[])
        print("9")
        zipped = zip( name, credits, grades)
        zipped_list = list(zipped)
        print("10")
        browser.close()
        browser.quit()
        print("成功")
        return(round(gp/credit,2),round(last60gp/last60credits,2),zipped_list)

        

