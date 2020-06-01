def GetLink(url):
    from urllib.request import urlopen, Request, urlretrieve
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin, urlparse
    from time import sleep

    #req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

    sleep(5)
    url = 'https://zenhabits.net/archives/'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(req).read()
    bs_obj = BeautifulSoup(url, "html.parser")

    # FIXME: pretty print
    pretty_html = bs_obj.prettify
    with open('html_pretty.html', 'w') as w_html:
        print(pretty_html, file=w_html)


    # FIXME: def a link collector
    html_a = bs_obj.findAll('a', href=True)
    hreflist = []
    with open('links.txt', 'w') as wfile:
        for i in html_a:
            print(i['href'], file=wfile)
            hreflist.append(i['href'])

    # FIXME: parsed link collectorr
    # newlink
    with open('article_links.txt', 'w') as wfile:
        for url in hreflist:
            if url.startswith('/'):
                url = urljoin('https://zenhabits.net', url)
                print(url, file=wfile)


def ReadArticles(link):
    #url = "https://zenhabits.net/uncertain/"

    from bs4 import BeautifulSoup
    from urllib.request import urlopen, Request
    from time import sleep
    sleep(3)

    req = Request(link,headers = {'User-Agent':'Mozilla/5.0'})
    url = urlopen(req).read()
    bs_obj = BeautifulSoup(url, "lxml")

    #html-all
    title = bs_obj.findAll('div',{'class':'container'})
    html_all = title[0]
    #print(html_all)

    #text-title
    title = bs_obj.findAll('div',{'class':'container'})
    text_title = title[0].h2.text
    print(text_title)

    #text-body
    body = bs_obj.findAll('div',{'class':'post'})
    for row in body:
        print(row.text)

    foldername = text_title.strip().replace(' ','_')
    with open('{}.txt'.format(foldername),'w') as wf:
         #text-title
        title = bs_obj.findAll('div',{'class':'container'})
        text_title = title[0].h2.text
        print(text_title, file = wf)
        print('-'*50, file = wf)
        #text-body
        body = bs_obj.findAll('div',{'class':'post'})
        for row in body:
            print(row.text, file = wf )
        print('Resource:\t' ,link , file =wf )
        
