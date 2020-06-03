import requests,string
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def cleaning(text):
    lower = text.lower()
    cleaned = lower.translate(str.maketrans('','',string.punctuation))
    return cleaned
def sentiment(text):
    
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    p=score['pos']*100
    ne=score['neg']*100
    nu=score['neu']*100
    return p,ne,nu

d=0
#page= requests.get('https://www.flipkart.com/seiko-spc235p1-lord-analog-watch-men/p/itmf3zh4zbmunjga?pid=WATEZSJ8JHBQDJRZ&srno=s_1_22&otracker=search&otracker1=search&fm=SEARCH&iid=8972c83e-7d3c-4660-92ad-04ce9c82789f.WATEZSJ8JHBQDJRZ.SEARCH&ppt=sp&ppn=sp&qH=d2974c96dc96b3f3')
inputt=input()
page = requests.get(inputt)
soup = BeautifulSoup(page.content, 'html.parser')
text1 = soup.find_all(class_='_2t8wE0')
a=b=c=0
for i in text1:
    d+=1
for j in range(0,d):
    text2= text1[j].text
    clean = cleaning(text2)
    p,ne,nu=sentiment(clean)
    a+=p
    b+=ne
    c+=nu
a=a/d
b=b/d
c=c/d
print("possitive :",a,'%')
print("negative :",b,'&')
print("neutral :",b,'%')

