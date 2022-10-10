# b9122_homework2

### Author: Aster Liu

### Description of the code files: 
## Question 1 (80 points)
In this question you are tasked with writing modified versions of the web crawler that we covered in class.
More specifically, you asked to create two webcrawlers for the following tasks: 
1. Crawl pages whose seed url is the press releases page of the Federal Reserve System: 
https://www.federalreserve.gov/newsevents/pressreleases.htm and collect pages that contain the 
word “covid” found within the page. The goal is to collect at least 10 such urls. At the end of the crawling 
the code should output the urls of the webpages found to contain the word “covid”. When checking whether the word is 
present on the webpage you should consider lower- and upper-case word versions (Covid, COVID, covid). One way to do this
is to lowercase the webpage text prior to doing word matching.

2. Crawl pages whose seed url is the press releases page of the Securities and Exchange Commission:
https://www.sec.gov/news/pressreleases and collect urls of press releases that contain the word “charges”. The code should 
output the first 20 such links that it finds. For each link output the url and the text. Similar to the previous task, 
when checking for the presence of the word “charges” you should consider lower- and upper-case versions.



