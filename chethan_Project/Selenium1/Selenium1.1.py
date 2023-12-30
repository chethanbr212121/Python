# 1) open web browser (chrome/firefox/edge).
# 2) Open url https://opensource-demo.orangehrmlive.com/
# 3) Enter username (Admin).
# 4) Enter password (admin123).
# 5) Click on Login.
# 6) capture title of the home page.(Actual title).
# 7) verify title of the page: OrangeHRM  (expected).
# 8) Close browser.
"""
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("G:\ETL\Selenium\Driversfolder\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

driver.find_element(By.ID,"txtUsername").send_keys("Admin")

driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.maximize_window()

driver.find_element(By.ID,"btnLogin").click()

act_titile = driver.title
exp_title = "OrangeHRM"
if act_titile == exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close()


## 2.0
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("G:\ETL\Selenium\Driversfolder\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("Nokia Lumia 1020")
#driver.find_element(By.LINK_TEXT,"noopener noreferrer").click()
driver.close()
driver.quit()


##3.0
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("G:\ETL\Selenium\Driversfolder\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")

#sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
#print(len(sliders)) ## Number of slide Images from having "class" name "homeslider-container"

### we can use By.CLASS, By.ID.By.NAME,By.TAG_NAME,By.CLASS_NAME etc

#sliders = driver.find_elements(By.CLASS_NAME,"item-img")
#print(len(sliders))  ## Number of Images from having "class" name "item-img" .

#links = driver.find_elements(By.TAG_NAME,'a')
#print(len(links))  ## Number of links  having "TAG_NAME" of "a" (here 149 links are there).



## 4.0 facebook by "CSS Selectors"
## CSS Selectors are TAG & ID, CLASS  & TAG, TAG & ATTRIBUTES , CLASS & TAG & ATTRIBUTES.
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("G:\ETL\Selenium\Driversfolder\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

## Tag and Id.
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")
##or
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc@gmail.com")

## Tag and Class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
##or
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")


##Tag and Attributes.
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
##or
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc@gmail.com")

##Tag, Class and Attributes.
'''It is used in case like below example where user name and password have same "Tag" and "Class" but have different
 "Attribute" if we give Tag and Attribute it will find only user name, to find password field use combination of 3'''
#driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal_email').send_keys("abc@gmail.com")

## For Password field
#driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal_pass').send_keys("adc123")
"""















