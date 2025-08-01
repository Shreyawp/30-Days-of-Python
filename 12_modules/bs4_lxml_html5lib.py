from bs4 import BeautifulSoup
import requests

with open('./data/simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify())

match = soup.title
print(match)
# >> <title>Test - A Sample Website</title>

match = soup.title.text
print(match)
# >> Test - A Sample Website

m = soup.div
print(m)
# OR
# m = soup.find('div')
''' 
####################### OUTPUT ##########################
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>
##########################################################
'''

m = soup.find('div', class_='footer')
print(m)
''' 
####################### OUTPUT ##########################
<div class="footer">
<p>Footer Information</p>
</div>
##########################################################
'''

article = soup.find('div', class_='article')
print(article)
''' 
####################### OUTPUT ##########################
<div class="article">
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>
##########################################################
'''

headline = article.h2.a.text
print(headline)
# >> Article 1 Headline

summary = article.p.text
print(summary)
# >> This is a summary of article 1


for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
''' 
####################### OUTPUT ##########################
Article 1 Headline
This is a summary of article 1

Article 2 Headline
This is a summary of article 2
##########################################################
'''


src = requests.get('https://medium.com/@venkat3010/python-basics-for-beginners-a-complete-guide-a5f01b73232f').text

soup = BeautifulSoup(src, 'lxml')
#print(soup.prettify())

article = soup.find('article')
#print(article)

headline =  article.h1.text
print(headline)
# >> Python Basics for Beginners: A Complete Guide

summary = soup.find('p', id="3733").text
print(summary)
''' 
####################### OUTPUT ##########################
Python is a popular programming language that is widely used for a variety of tasks, such as web development, data analysis, machine learning, and more.
##########################################################
'''

## scraping video from webpage
url = 'https://www.unclebigbay.com/blog/how-to-embed-youtube-videos-into-your-web-projects'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
#print(soup.prettify())

video_src = soup.find('iframe')['src']
print(video_src)
# >> https://codepen.io/unclebay143/embed/qBPjQdG?default-tab=html%2Cresult

# grab id of the video
vid_id = video_src.split('/')[5]
vid_id = vid_id.split('?')[0]
print(vid_id)
# >> qBPjQdG

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
# >> https://youtube.com/watch?v=qBPjQdG


