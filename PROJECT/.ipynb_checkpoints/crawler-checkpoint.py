# Crawler for weblinks

# Get page input from user


def record_user_click(index, keyboard, url):
    urls = lookup(index, keyword) # check if we have  urls
    if urls:
        for entry in urls:
            if entry[0] == url: # check if we have that entry in list index
                entry[1] += entry[1] + 1 #add entry to count

def add_to_index(index, keyword, url):
    # format of index: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword: # check keyword
            for element in entry[1]: # loop [url,count] for duplicates
                if element[0] == url: # check if [0] is our url
                    return
            entry[1].append([url,0]) # if not in list, append to it
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])



def lookup(index, keyword):
    result = []
    for entry in index:
        if entry[0] == keyword:
            result.append(entry[1])
    return result


def get_page(page):
    try:
        import  urllib
        return urllib.urlopen(url).read()
    except:
        return "No page"


def get_next_target():
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',  start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# Union of pages into crawler function

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links = links.append(url) # links.append(url) - links =
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = [] # len(crawled) in lenght of crawled
    next_depth = [] # new list to store the next level of links
    depth = 0
    while tocrawl:
        page = tocrawl.pop()
        # test if the page has already been crawled
        if page not in crawled and len(crawled) < max_pages:
            # use union to add pages, to avoid dupplication
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl: # when we finish going through list in level, change var
            tocrawl, next_depth = next_depth, [] # change variables
        return crawled


def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = [] # keeps track of the next pages to crawl
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled # and len(crawled) <= tocrawl[:max_depth + 1]
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth += +1
    return crawled
