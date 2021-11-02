import requests
from bs4 import BeautifulSoup


class Topic:
    id = 0
    title = None
    resources = []
    templates = []
    problems = []
    difficulty = 0
    def __init__(self,id,title,resources,problems,templates,difficulty):
        self.title = title
        self.id = id
        self.resources = resources
        self.templates = templates
        self.difficulty = difficulty
        self.problems = problems



URL = "https://codeforces.com/blog/entry/95106"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

spoiler = soup.find("div",class_="spoiler")

spoiler_content = spoiler.find("div",class_="spoiler-content")
tables = spoiler_content.find_all("table")
headings = spoiler_content.find_all("h3")
headings = list(headings)
index = 0

Ultimate_list = {}

for table in tables:
    index+=1

    if index==1:
        continue
    category = headings[index-1].text
    Ultimate_list[category] = []
    body = table.find("tbody")
    rows = body.find_all("tr")
    row_index = 0
    for row in rows:
        row_index+=1
        if row_index==1:
            continue
        data = row.find_all("td")
        data = list(data)
        if(len(data)<6):
            continue
        id = data[0].text
        title = data[1].text
        resources = []
        links = data[2].find_all("a",href=True)
        for link in links:
            resources.append(link['href'])
        problems = []
        links = data[3].find_all("a",href=True)
        for link in links:
            problems.append(link['href'])
        templates = []
        links = data[4].find_all("a",href=True)
        for link in links:
            templates.append(link['href'])
        difficulty = data[5].text
        t = Topic(id,title,resources,problems,templates,difficulty)
        Ultimate_list[category].append(t)


for item in Ultimate_list[' Category: Math']:
    print(item)
        

