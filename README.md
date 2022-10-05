# Overview
This project was developed as a way to introduce myself to machine learning. I chose to create ML models for the NBA Most Valuable Player (MVP) award because I have always been a fan of basketball (especially the OKC Thunder) and had long wanted to play with AI/ML algorithms as it pertains to sports to see what kind of insights I could draw. The project is split into several parts: Scraping HTML, parsing HTML, cleaning the data, and making machine learning models. I have chosen not to include the .csv files that I scraped because that information is not my own and can be found at https://www.basketball-reference.com/.

# Scraping and Parsing Data
There are three files whose names start with "scrape" that scrape HTML for MVP voting, player statistics, and team statistics. When these files are run, they will request the web pages and download the HTML content to the folders called mvps, stats, and teams, respectively. After this has been done, there are three files whose names start with "parse" that parse the downloaded HTML files, select the desired data, create a data frame, and save the data as a .csv.

# Cleaning the Data and Creating ML Models
After I generated the .csv files for the MVP voting, player statistics, and team statistics, I began cleaning the data to make it suitable for creating machine learning models. I did this in a Jupyter Notebook file named data-cleaning.ipynb. I also created a combined data frame for the MVP voting, player statistics, and team statistics in this file. After I cleaned and combined the data, I created ML models on it in a Jupyter Notebook file named machine-learning.ipynb. I created a ridge regression model and a random forest regression model for the data measured the performance using average precision. The average precision for both models can be found in the machine-learning.ipynb file.

# Relevant Topics and Skills
- Python
- Pandas
- scikit-learn
- Web scraping
- HTML parsing
- Data cleaning
- Machine learning

# References
- All of the data is courtesy of https://www.basketball-reference.com/
- The data cleaning and machine learning parts of this project were developed with the help of Dataquest (see more: https://www.dataquest.io/)
