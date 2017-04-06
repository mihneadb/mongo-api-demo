from fetch import get_comments, get_sentiment
from models import Comment


PRODUCT_URL = 'http://www.pcgarage.ro/televizoare-led/samsung/32j5100-seria-j5100-80cm-negru-full-hd/comentarii/'


if __name__ == '__main__':
    comments = get_comments(PRODUCT_URL)

    for comment in comments:
        c = Comment(**comment)
        c.sentiment = get_sentiment(c.text)
        c.save()

