from parser import get_dom
from bs4 import BeautifulSoup
import webbrowser
import os

from simpleServer import run_server

url = "https://rate.am/"
parsed_dom = get_dom(url)

# save enq anum pars exac html taza output.html filum
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(parsed_dom.prettify())

# vercnumenq index.html@ vor BeautifulSoup ov domin dimenq
with open('index.html', 'r') as file:
    html_content = file.read()

# ogtagorcumenq BeautifulSoup lib@ html-i analizi hamar
soup = BeautifulSoup(html_content, 'html.parser')

# gtnumenq mer uzac@ teg@ te urde pti avelcnenq pars exac html@
target_tag = soup.find('div', {'id': 'wrapper-for-inserting'})

target_tag.clear()
target_tag.append(BeautifulSoup(parsed_dom.prettify(), 'html.parser'))

with open('index.html', 'w') as file:
    file.write(str(soup))

# vercnumenq tvyal directorian
current_directory = os.getcwd()

full_path_to_index = os.path.join(current_directory, 'index.html')

# bacumenq index.html@ chrom brauwserum
webbrowser.get('chrome').open('file://' + full_path_to_index, new=2)

# server@ runenq anum
run_server(parsed_dom.prettify())