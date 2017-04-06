from collections import defaultdict

from bs4 import BeautifulSoup
import requests

import constants


def parse_comment(text):
    data = defaultdict(str)

    for line in text.splitlines():
        line = line.strip()
        if line == 'Pro:':
            key = constants.PRO
            continue
        elif line == 'Contra:':
            key = constants.CON
            continue
        elif line == 'Altele:':
            key = constants.OTHER
            continue

        if not data[key]:
            data[key]
        data[key] += '%s\n' % line

    return data


def get_comments(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    comments = []
    for comment in bs.find_all('div', {'class': 'cw-comment'}):

        descriptions = comment.find_all('p', {'itemprop': 'description'})
        if not descriptions:
            continue

        for d in descriptions:
            comment_text = d.text.strip()
            parsed = parse_comment(comment_text)

            comments.append(parsed)

    return comments


def get_sentiment(text):
    data = {'text': text}
    r = requests.post(constants.SENTIMENT_API, json=data)

    sentiment = r.json()['sentiment']
    return constants.SENTIMENTS[sentiment]

