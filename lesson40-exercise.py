import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elements = soup.select('#product-price-17720 > span')
    return elements[0].text.strip()





price = getAmazonPrice('https://www.grasscity.com/glass-ice-bong-with-triple-perc-14-inches.html')

print('The price is ' + price)