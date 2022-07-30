'''Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(5)

'''By ID'''

# button = chrome.find_element(By.ID,'submit')
# button.click()
# sleep(3)

# male = chrome.find_element(By.ID, 'sex-0')
# male.click()
# sleep(3)

# UFT = chrome.find_element(By.ID, 'tool-0')
# UFT.click()
# sleep(3)

'''By link text'''

# download_file = chrome.find_element(By.LINK_TEXT, 'Click here to Download File')
# download_file.click()
# sleep(3)

# automate_amazon = chrome.find_element(By.LINK_TEXT, 'Automate Amazon like E-Commerce website with Selenium')
# automate_amazon.click()
# sleep(3)

# java_tutorial = chrome.find_element(By.LINK_TEXT, 'Java Tutorial')
# java_tutorial.click()
# sleep(3)

'''By parțial link text'''

# selenium_ide = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Selenium IDE (No Cod')
# selenium_ide.click()
# sleep(3)

# selenium_webdriver = chrome.find_element(By.PARTIAL_LINK_TEXT, '50+ Selenium WebDriv')
# selenium_webdriver.click()
# sleep(3)

# email_us = chrome.find_element(By.PARTIAL_LINK_TEXT, 'email')
# email_us.click()
# sleep(3)

'''By name'''

# first_name = chrome.find_element(By.NAME, 'firstname')
# first_name.send_keys('Petrit')
# sleep(3)

# last_name = chrome.find_element(By.NAME, 'lastname')
# last_name.send_keys('Octavian')
# sleep(3)

# continents = chrome.find_element(By.NAME, 'continents')
# continents.click()
# sleep(3)

'''By tag*'''

# chrome.get('https://formy-project.herokuapp.com/keypress')
# sleep(5)

# full_name = chrome.find_element(By.TAG_NAME, 'input')
# full_name.send_keys('Petrit Octavian')
# sleep(3)

# chrome.get('https://the-internet.herokuapp.com/key_presses')
# input = chrome.find_element(By.TAG_NAME, 'input')
# input.send_keys('1234')
# sleep(3)

# chrome.get('https://the-internet.herokuapp.com/geolocation')
# button = chrome.find_element(By.TAG_NAME, 'button')
# button.click()
# sleep(3)

'''By Class name*'''

# chrome.get('http://automationpractice.com/index.php?controller=order')
# sleep(5)
# login = chrome.find_element(By.CLASS_NAME, 'login')
# login.click()
# sleep(3)

# contact = chrome.find_element(By.CLASS_NAME, 'shop-phone')
# contact.click()
# sleep(3)

# chrome.get('http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=&submit_search=')
# sleep(5)
# categories = chrome.find_element(By.CLASS_NAME, 'home')
# categories.click()
# sleep(3)

'''By CSS'''

# chrome.get('http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=&submit_search=')
# sleep(3)

'''class name'''
# chrome.find_element(By.CSS_SELECTOR, "h2[class='title_block']").click()
# sleep(3)

# chrome.find_element(By.CSS_SELECTOR, "section[id='informations_block_left_1'] p[class='title_block']").click()
# sleep(3)

# chrome.find_element(By.CSS_SELECTOR, "p[class='title_block'] a[title='Specials']").click()
# sleep(3)

'''atribut=valoare_partiala'''
# chrome.find_element(By.CSS_SELECTOR, "button[name='submit_search']").click()
# sleep(3)

# chrome.find_element(By.CSS_SELECTOR, "a[title='View my shopping cart'] b").click()
# sleep(3)

# chrome.find_element(By.CSS_SELECTOR, "section[class='blockcategories_footer footer-block col-xs-12 col-sm-2'] h4").click()
# sleep(3)

'''Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.'''


'''3 după atribut valoare'''

# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.XPATH, "//a[@title='Women']").click()
# sleep(3)

# chrome.find_element(By.XPATH, "//div[@id='htmlcontent_top']//li[@class='htmlcontent-item-1 col-xs-4']//img[@class='item-img']").click()
# sleep(3)

# chrome.find_element(By.XPATH, "//img[@alt='My Store']").click()
# sleep(3)

'''3 după textul de pe element'''

# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.XPATH, "//a[normalize-space()='A/B Testing']").click()
# sleep(3)

# chrome.find_element(By.XPATH, "//a[normalize-space()='Broken Images']").click()
# sleep(3)

# chrome.find_element(By.XPATH, "//a[normalize-space()='Hovers']").click()
# sleep(3)

'''1 după parțial text'''

# chrome.find_element(By.XPATH, "").click()
# sleep(3)

'''1 cu SAU, folosind pipe |'''

# chrome.find_element(By.XPATH, "//a[normalize-space()='Checkboxes']|//a[normalize-space()='Context Menu']").click()
# sleep(3)

'''1 cu *'''

# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//*[@id="job-title"]').send_keys('Maintenance Technician')
# sleep(3)

'''1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]'''

# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '/html[1]/body[1]/div[1]/form[1]/div[1]/div[4]/div[4]/input[1]').click()
# sleep(3)

'''1 în care să folosești parent::'''

chrome.get('https://www.phptravels.net/')
chrome.find_element(By.XPATH, '/html[1]/body[1]/div[1]/form[1]/div[1]/div[4]/div[4]/input[1]').click()
sleep(3)


