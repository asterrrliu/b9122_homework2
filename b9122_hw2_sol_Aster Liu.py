# Computing: Homework 2
# Aster Liu


from bs4 import BeautifulSoup
import urllib.request

out_file = open("HW2output.txt", "w")

# Question 1 - 1

url_1 = 'https://www.federalreserve.gov/newsevents/pressreleases.htm'


req = urllib.request.Request(url_1,headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()
# print(webpage)
soup = BeautifulSoup(webpage)
child_list = []

out_file.write("Question 1" + '\n')
out_file.write("(1)" + '\n')

for tag in soup.find_all('a', href = True):
    childUrl = tag['href'] 
    childUrl = urllib.parse.urljoin(url_1, childUrl)
    child_list.append(childUrl)

covid_url = []
for child_url in child_list:
    try:
        req = urllib.request.Request(child_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(webpage)
        web_low_str = soup.get_text().lower()
        if 'covid' in web_low_str:
            covid_url.append(child_url)
            out_file.write(child_url + '\n')

    except Exception as ex:
        continue 



# Question 1 - 2


url_2 = 'https://www.sec.gov/news/pressreleases'


req = urllib.request.Request(url_2,headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()
# print(webpage)
soup = BeautifulSoup(webpage)
child_list = []

out_file.write("Question 1" + '\n')
out_file.write("(2)" + '\n')

for tag in soup.find_all('a', href = True):
    childUrl = tag['href'] 
    childUrl = urllib.parse.urljoin(url_2, childUrl)
    child_list.append(childUrl)

# print(child_list)
charge_url = []
count = 0
for child_url in child_list:
    if count == 20:
        break
    try:
        req = urllib.request.Request(child_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(webpage)
        web_str = soup.get_text()
        web_lower_str = web_str.lower()
        
        if 'charges' in web_lower_str:
            charge_url.append(child_url)
            out_file.write(child_url + '\n')
            out_file.write(web_str + '\n')
            count += 1
    except Exception as ex:
        continue 


out_file.close()
print(len(charge_url))
