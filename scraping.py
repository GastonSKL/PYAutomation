import requests 
import bs4
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-' * 50 +'<br>')
    response = requests.get(url)
    content = response.content
    soup = bs4.BeautifulSoup(content,'html.parse')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','yaling':''})):
        cnt += ((str(i+1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        #print(tag.prettify) #find all('span', attrs={'class':'sistestr}))
        return(cnt)
    

cnt = extract_news('https://news.vcombinator.com/') ;   
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

print('Composing Email...')


SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'gastonlskamlec@gmail.com' 
TO = 'gastonlskamlec@gmail.com'
PASS = 'Apolo15235506'

msg = MIMEMultipart()