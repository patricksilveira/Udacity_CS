# exercise from https://www.youtube.com/watch?v=XQgXKtPSzUI


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = input('Your Url')

#Open connect and grab the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Parsing
page_soup = soup(page_html, "html.parser")

# Grabs part of the page
containers = page.soup.findAll("div",{"class":"item-container"})

# export to csv
filename = "product.csv"
f = open(filename, 'w')

headers = "brand, product_name, shipping\n"
f.write(headers)


#grabs item inside container

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text #grabs only text inside title_cont

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    brand("brand:" + brand)
    product_name("product_name:" + product_name )
    shipping("shipping:" + shipping )

    f.write(brand + ',' +product_name.replace(|) + '' +shipping + "\n")

f.close()
