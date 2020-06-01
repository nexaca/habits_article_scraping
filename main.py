from modules import GetLink,ReadArticles

url = 'https://zenhabits.net/archives/'

GetLink(url)

with open('article_links.txt','r') as rf:
    data = rf.readlines()
    for link  in data: 
        link = link.replace('\n','').strip()
        ReadArticles(link)