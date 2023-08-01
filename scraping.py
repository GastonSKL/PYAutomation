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
    soup = bs4.BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valing':''})):
        cnt += ((str(i+1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        #print(tag.prettify) #find all('span', attrs={'class':'sistestr}))
        return(cnt)
    

# cnt = extract_news('https://www.google.com/') ;   
cnt = ""
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

print('Composing Email...')


SERVER = 'smtp.gmail.com'
PORT = 587
FROM = '************' 
TO = '**************'
PASS = '***********'

msg = MIMEMultipart()

msg['Subject'] = "Historias de hackernews! " + str(now.day) + '/' + str(now.month)+ '/' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initializing server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent...')

server.quit()