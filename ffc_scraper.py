import requests
from bs4 import BeautifulSoup
import re

## write adps to new csv
scr = open("2010-23_player_adp_ppr.csv", 'w')
start, end = 2010, 2024
for year in range(start, end+1):
    # search each year by changing url
    pg = requests.get("https://fantasyfootballcalculator.com/adp/ppr/12-team/all/" + str(year))
    if pg.status_code == 200:
        #change response object to text
        pg_content = pg.text
    else:
        print(pg.status_code)
        exit()
    soup = BeautifulSoup(pg_content, features="html.parser")

    # get name attributes with "/players/" in brackets using re
    # name_html = soup.find_all('a', href=re.compile(r'/players'))
    attrs_html = soup.find_all('tr', class_=re.compile(r'(RB|WR|QB|TE|FB|DEF|PK|)'))
    for line in attrs_html:
        # remove all \n
        # get text is a bs method that converts to text
        row = line.get_text().strip().split('\n')
        #iterate for .write, 10 is n of items in list
        for item in range(0, 10):
            scr.write(row[item])
            # don't want comma at end of row
            if item != 9:
                scr.write(", ")
            else:
                # make year an element of the list
                scr.write("," + str(year) + "\n")
scr.close()

# with open("adp.csv", 'r') as anls:
#     print(read())
