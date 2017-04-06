from collections import defaultdict

from bs4 import BeautifulSoup
import requests

import constants


def parse_comment(text):
    """Given raw comment data, formats it as a dict.

    Returns dicts such as `{'type': 'pro', 'text': 'foo'}`.
    """

    data = defaultdict(str)

    for line in text.splitlines():
        line = line.strip()
        if line == 'Pro:':
            type = constants.PRO
            continue
        elif line == 'Contra:':
            type = constants.CON
            continue
        elif line == 'Altele:':
            type = constants.OTHER
            continue

        data['text'] += '%s\n' % line

    data['type'] = type
    data['text'] = data['text'].strip()
    return data


def get_comments(url):
    """Fetches comments from a `/comentarii/` edge on PCGarage.

    Returns a list of dicts. See `parse_comment`.`.
    """

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
    """Calls external API to detect the sentiment of `text`."""

    data = {'text': text}
    r = requests.post(constants.SENTIMENT_API, json=data)

    sentiment = r.json()['sentiment']
    return constants.SENTIMENTS[sentiment]

