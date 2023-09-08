from bs4 import BeautifulSoup
import requests

def get_dom(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        rates_table = soup.find('table', {'class': 'rb'})
        return rates_table
    else:
        print(f"Error fetching URL: {url}")
        return None