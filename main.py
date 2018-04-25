import subprocess
import urllib
from lxml import html

def getPercentage(page, coinpath):
    coinindex = page.find(coinpath) + len(coinpath) + 2
    coinpercentage = page[coinindex:].split("%")[0]
    return coinpercentage

if __name__ == '__main__':
    coin1path = "C:\Users\User\Desktop\moss\coins/bitcoin/src/"
    coin2path = "C:\Users\User\Desktop\moss\coins/BTCGPU/src/"
    pipe = subprocess.Popen(["perl", "C:\Users\User\Desktop\moss\moss.pl", "-d", "-cc", (coin1path + "*.cpp"), (coin2path+"*.cpp")], stdout=subprocess.PIPE)
    while(1):
        url = pipe.stdout.readline()
        if ("http://moss.stanford.edu" in url):
            break
    #page = html.fromstring(urllib.urlopen(url).read())
    page = urllib.urlopen(url).read()
    coin1percentage = getPercentage(page, coin1path)
    coin2percentage = getPercentage(page, coin2path)
    print(coin1percentage)
    print(coin2percentage)

#     for link in page.xpath("//a"):
#         if((coin1path in link.test) or (coin2path in link.test)):
#             print "Name", link.text, "URL", link.get("href")