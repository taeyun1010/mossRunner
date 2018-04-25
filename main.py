import subprocess
import urllib
from lxml import html
from lxml import etree
import os
import os.path
import re

#
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
#

# put the desired extension here
extension = ".cpp"
# also change this to desired extension
extensionCmd = "cc"

coin1path = "C:\Users\User\Desktop\moss\coins/bitcoin/"
coin2path = "C:\Users\User\Desktop\moss\coins/BTCGPU/"

# get max percentage of the file happening in this page
def getPercentage(page, coinpath):
    maxPercentage = 0
#     html = etree.HTML(page)
#     table = etree.HTML(page).find("body/table")
#     rows = iter(table)
#     headers = [col.text for col in next(rows)]
#     for row in rows:
#         values = [col.text for col in row]
#         print dict(zip(headers, values))
    
    
    #indexes = [m.start() for m in re.finditer(coinpath, page)]

    parsed_html = BeautifulSoup(page, "lxml")
    table = parsed_html.body.table
    rows = table.find_all('tr')
    
    # contents in the table
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
    for thisdata in data:
        if(len(thisdata) != 0):
            thedata = thisdata[0]
            if(coinpath in thedata):
                print("thedata = " + thedata)
                beginindex = page.find(coinpath) + len(coinpath) + 2
                coinpercentage = page[beginindex:].split("%")[0]
                thispercentage = coinpercentage
                if(maxPercentage < thispercentage):
                    maxPercentage = thispercentage
    
    #coinindex = page.find("<TR><TD><A HREF=") + len(coinpath) + 2
    
    #coinpercentage = page[coinindex:].split("%")[0]
    return maxPercentage

def queryServer(file1, file2):
    pipe = subprocess.Popen(["perl", "C:\Users\User\Desktop\moss\moss.pl", "-l", extensionCmd, file1, file2], stdout=subprocess.PIPE)
    while(1):
        url = pipe.stdout.readline()
        if ("http://moss.stanford.edu" in url):
            break
    #page = html.fromstring(urllib.urlopen(url).read())
    
    page = urllib.urlopen(url).read()
    
    #parsedhtml2 = urllib.urlopen(url)
    
#     #
#     soup = BeautifulSoup(page, 'lxml') # Parse the HTML as a string
#     
#     table = soup.find_all('table')[0] # Grab the first table
#     
#     new_table = pd.DataFrame(columns=range(0,2), index = [0]) # I know the size 
#     
#     row_marker = 0
#     for row in table.find_all('tr'):
#         column_marker = 0
#         columns = row.find_all('td')
#         for column in columns:
#             new_table.iat[row_marker,column_marker] = column.get_text()
#             column_marker += 1
#     #
    
            
    #print(page)
    coin1percentage = getPercentage(page, file1)
    #coin2percentage = getPercentage(page, file2)
    return coin1percentage
    

if __name__ == '__main__':
#     coin1path = "C:\Users\User\Desktop\moss\coins/bitcoin/src/"
#     coin2path = "C:\Users\User\Desktop\moss\coins/BTCGPU/src/"
    #pipe = subprocess.Popen(["perl", "C:\Users\User\Desktop\moss\moss.pl", "-l",extensionCmd, (coin1path + "/src/*.cpp"), (coin2path+"/src/*.cpp")], stdout=subprocess.PIPE)
    
#     for root, dirs, files in os.walk("C:\Users\User\Desktop\moss\coins/bitcoin"):
#         for name in files:
#             print(os.path.join(root, name))
#         for name in dirs:
#             print(os.path.join(root, name))
#             
#             
    # consider every file with the given extension in coin1 directory
    for dirpath, dirnames, filenames in os.walk(coin1path):
        for filename in [f for f in filenames if f.endswith(extension)]:
            thisfile = os.path.join(dirpath, filename)
            percentage1 = queryServer(thisfile, "C:\Users\User\Desktop\moss\coins\BTCGPU\src/*.cpp")
            print(str(percentage1) + "\n")
#     temp = os.walk("C:\Users\User\Desktop\moss\coins/bitcoin/")
#     print(x[0] for x in temp)
#     


#     while(1):
#         url = pipe.stdout.readline()
#         if ("http://moss.stanford.edu" in url):
#             break
#     #page = html.fromstring(urllib.urlopen(url).read())
#     page = urllib.urlopen(url).read()
#     print(page)
#     coin1percentage = getPercentage(page, coin1path)
#     coin2percentage = getPercentage(page, coin2path)
#     print(coin1percentage)
#     print(coin2percentage)

#     for link in page.xpath("//a"):
#         if((coin1path in link.test) or (coin2path in link.test)):
#             print "Name", link.text, "URL", link.get("href")