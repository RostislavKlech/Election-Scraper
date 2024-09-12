"""
volby.py: Třetí projekt do Engeto Online Python Akademie

Author: Rostislav Klech
email: KlechRostislav@seznam.cz
discord: Rosta K
"""




import requests
from bs4 import BeautifulSoup
import sys
import csv



def get_info_area(soup):
    tables = soup.find_all("table")
    rows = tables[0].find_all("tr")[2:]
    for row in rows:
        columns = row.find_all("td")
        if len(columns) > 4:
            registered = columns[3].text.strip()
            envelopes = columns[4].text.strip()
            valid = columns[-2].text.strip()
    return registered, envelopes, valid

def get_info_parties(soup):
    tables = soup.find_all("table")
    parties = []
    votes = []
    for i in [1,2]:
        rows = tables[i].find_all("tr")[2:]  
        for row in rows:
            columns = row.find_all("td")
            if len(columns) > 2:
                parties.append(columns[1].text.strip())
                votes.append(columns[2].text.strip())
    return parties, votes

def scrape(main_url):
    print(f"Downloading data from URL: {main_url}...")
    answer = requests.get(main_url)
    if answer.status_code != 200:
        print("Invalid URL or the page is not accesible.")
        sys.exit(1)    
    soup = BeautifulSoup(answer.content, "html.parser")    
    links = soup.select("td.cislo a")    
    if not links:
        print("The page is not as expected.")
        sys.exit(1) 
    print("Data was successfully downloaded. Processing individual municipalities...")       
    full_data = []
    parties = []
    for link in links:
        below_url = f"https://volby.cz/pls/ps2017nss/{link['href']}"
        code = link.text
        below_answer = requests.get(below_url)
        below_soup = BeautifulSoup(below_answer.content, "html.parser")
        parent_row = link.find_parent("tr")
        name_column = parent_row.find_all("td")[1]
        name = name_column.text.strip()
        registered, envelopes, valid = get_info_area(below_soup)
        if not parties:  
            parties, votes = get_info_parties(below_soup)
        else:
            _, votes = get_info_parties(below_soup)
        full_data.append([code, name, registered, envelopes, valid] + votes)
    print("All data has been processed.")
    return full_data, parties

def create_csv(data, parties, filename):
    head = ["Kód obce", "Název obce", "Počet voličů", "Počet obálek", "Platné obálky"] + parties
    
    with open(filename, mode="w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(head)
        for row in data:
            writer.writerow(row)

    print(f"Data has been saved to the file: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python volby.py <URL> <output_file_name>")
        sys.exit(1) 

    url = sys.argv[1]
    filename = sys.argv[2]
    if not url.startswith("http"):
        print("The first argument must be a valid URL.")
        sys.exit(1)
    if not filename.endswith(".csv"):
        print("The second argument must be of the form 'name'.csv.")
        sys.exit(1)
    
    try:
        data, parties = scrape(url)
        create_csv(data, parties, filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


   





