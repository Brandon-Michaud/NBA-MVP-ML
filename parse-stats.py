from bs4 import BeautifulSoup
import pandas as pd

years = list(range(1980,2022))
dfs = []
for year in years:
    with open(f'stats/{year}.html', encoding="utf-8") as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    for row in soup.find_all('tr', class_="thead"):
        row.decompose()
    player_table = soup.find(id="per_game_stats")
    player = pd.read_html(str(player_table))[0]
    player["Year"] = year
    
    dfs.append(player)
mvps = pd.concat(dfs)
mvps.to_csv("stats.csv")