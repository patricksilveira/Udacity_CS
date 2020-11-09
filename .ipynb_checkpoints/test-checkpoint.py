index=[]

def add_to_index(index,keyword,url):
    while index:
        if keyword in index:
            keyword.append(url)
        if keyword not in index:
            keyword = [url]
            index.append(keyword)

add_to_index(index,'udacity','http://udacity.com')
print (index)
add_to_index(index,'computing','http://acm.org')
print (index)
add_to_index(index,'udacity','http://npr.org')
print (index)
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]






