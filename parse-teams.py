from bs4 import BeautifulSoup
import pandas as pd

years = list(range(1980,2022))
dfs = []
for year in years:
    with open(f'teams/{year}.html', encoding="utf-8") as f:
        page = f.read()
    
    soup = BeautifulSoup(page, "html.parser")
    for row in soup.find_all('tr', class_="thead"):
        row.decompose()
    team_table = soup.find(id="divs_standings_E")
    team = pd.read_html(str(team_table))[0]
    team["Year"] = year
    team["Team"] = team["Eastern Conference"]
    del team["Eastern Conference"]
    dfs.append(team)

    soup = BeautifulSoup(page, "html.parser")
    for row in soup.find_all('tr', class_="thead"):
        row.decompose()
    team_table = soup.find(id="divs_standings_W")
    team = pd.read_html(str(team_table))[0]
    team["Year"] = year
    team["Team"] = team["Western Conference"]
    del team["Western Conference"]
    dfs.append(team)

teams = pd.concat(dfs)
teams.to_csv("teams.csv")