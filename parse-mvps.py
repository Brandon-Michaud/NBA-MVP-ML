from bs4 import BeautifulSoup
import pandas as pd

years = list(range(1980,2022))
dfs = []
for year in years:
    with open(f'mvps/{year}.html', encoding="utf-8") as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="over_header").decompose()
    mvp_table = soup.find(id="mvp")
    mvp = pd.read_html(str(mvp_table))[0]
    mvp["Year"] = year

    dfs.append(mvp)
mvps = pd.concat(dfs)
mvps.to_csv("mvps.csv")