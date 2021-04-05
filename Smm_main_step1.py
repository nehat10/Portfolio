
import requests
import time
import csv
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## In the following segment, we interact with the browser in automation mode to load 10 pages of articles
## After the articles are loaded, we extract a list of news article URLs based on a keyword search.

list_url = "https://www.nytimes.com/search?query=election+2020"

domain_url = "https://nytimes.com"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(list_url)

button = driver.find_element_by_css_selector('[data-testid="search-show-more-button"]')

count = 11
while count > 1:
     button.click()

     count -= 1
     time.sleep(2)

timeout = 20
while True:
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/main/div/div[2]/div[1]/ol/li[103]'))
        WebDriverWait(driver, timeout).until(element_present)
        break
    except TimeoutException:
        print("Timed out waiting for page to load")

uClient = uReq(list_url)
read_html = uClient.read()
uClient.close()
html = driver.page_source
page_soup = soup(html, "html.parser")
text_sections = page_soup.find("div", {"class": "css-46b038"}).find_all("a")


article_urls = []

for i in text_sections:

    if "/2020/" in i.get("href"):
        if "/dejoy-postal-service" in i.get("href") or "/vote-by-mail-us-states" in i.get("href") or "/the-digital-vp-rollout." in i.get("href") or "/biden-vs-trump." in i.get("href") or "/trump-biden." in i.get("href") or "/trump-rnc-approval-rating" in i.get("href") or "/dnc-michelle-obama." in i.get("href"):
            
            pass
        else:
            t = domain_url + i.get("href")
            print(t)
            article_urls.append(t)


### The following is the code to  extract each news article. For multiple URLs,
### we iterate over the list of URLs scraped in the previous step.

cnn_url = "https://www.nytimes.com/2020/09/16/us/politics/michael-caputo-hhs-leave-of-absence.html"


my_list3 = []
for i in article_urls:
    cnn_url = i
    uClient = uReq(cnn_url)
    read_html = uClient.read()
    uClient.close()
    
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "css-rsa88z e1h9rw200"})
    if headline is None:
        headline = page_soup.find("h1", {"class": "css-hzs6w4 e1h9rw200"})
        if headline is None:
            headline = page_soup.find("h1", {"class": "interactive-heading css-rsa88z e1h9rw200"})
            if headline is None:
                headline = page_soup.find("h1", {"class": "css-kzuvc5 e1h9rw200"})

        
    text_sections = page_soup.find("div", {"class": "css-53u6y8"})

    if text_sections is None:
        text_sections = page_soup.find("div", {"class": "g-story g-freebird g-max-limit"})

    text_sections= text_sections.find_all("p")
    article = ""

    for i in text_sections:

        article += i.text


    my_list3.append([headline.text, article])


# opening the csv file in 'w+' mode 
file = open('smm_step1.csv', 'w+', newline ='') 
  
# writing the data into the file 
with file:     
    write = csv.writer(file) 
    write.writerows(my_list3)

