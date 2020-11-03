import requests

page = requests.get("https://www.thecrimson.com/")

#print(page.content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, "html.parser")
first_col = soup.find(id = 'primary-first')
f_col_names = first_col.find_all(class_ = 'preview-content')

names = []

for i in range(len(f_col_names)):
   names.append(f_col_names[i].find('a').get_text())

second_col = soup.find(id = 'primary-second')
f_col_names2 = second_col.find_all(class_ = 'preview-content')
for i in range(len(f_col_names2)):
   names.append(f_col_names2[i].find('a').get_text())

print(names)

