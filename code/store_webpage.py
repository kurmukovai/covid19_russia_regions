import requests
from bs4 import BeautifulSoup
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    date = argv[2]

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    with open(f'../data/html/{date}.txt', 'w') as f:
        f.write(soup.text)
