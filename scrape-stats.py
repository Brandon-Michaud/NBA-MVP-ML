import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:/webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)

years = list(range(1980,2022))
url_start = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
for year in years:
    url = url_start.format(year)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,100000)")
    time.sleep(5)
    html = driver.page_source

    with open('stats/{}.html'.format(year), 'w+', encoding="utf-8") as f:
        f.write(html)