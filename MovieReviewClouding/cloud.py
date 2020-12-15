import requests
from bs4 import BeautifulSoup
import re
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
from collections import Counter


def filter(s):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

    result = hangul.sub('', s)
    return result


url_page = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=196843&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"

page = 0
list_text = []
nnpy = Okt()

while page < 40:
    page += 1
    if page > 1:
        url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=196843&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"
        url_page = url + "&page=" + str(page)
    else:
        pass

    res = requests.get(url_page, verify=False)
    soup = BeautifulSoup(res.text, "lxml")
    div = soup.find_all(class_="score_reple")

    count = 0
    list = []
    for i in div:
        span_id = "_filtered_ment_" + str(count)
        list.append(i.p.find(id=span_id))
        count += 1

    for j in list:
        text = filter(j.text)
        noun = nnpy.nouns(text)
        list_text += noun

list_keywords = [n for n in list_text if len(n) > 1]

counts = Counter(list_keywords)
tags = counts.most_common(50)
keywords = dict(tags)
stoplist = ['영화', '연기', '너무', '정말', '배우', '내내', '영상', '자체','진짜','지금','보고','평점','스토리','주인공','여자','남자','그','도대체','이제','완전','극장','개봉','내용','그냥','영화관','제목','댓글','정도','대체',]

for word in stoplist:
    if word in keywords.keys():
        keywords.pop(word)

print(keywords)


wordcloud = WordCloud(font_path='NanumGothic.ttf'
                      , background_color='white', width=800, height=600)
cloud = wordcloud.generate_from_frequencies(keywords)

plt.rcParams['font.family'] = 'nanumGothic'
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

