from fetch import get_comments, get_sentiment
from models import Comment


if __name__ == '__main__':

    url = 'http://www.pcgarage.ro/televizoare-led/samsung/32j5100-seria-j5100-80cm-negru-full-hd/comentarii/'
    comments = get_comments(url)

    for comment in comments:
        c = Comment(text=comment.values()[0], type=comment.keys()[0])
        c.text = c.text.strip()
        c.sentiment = get_sentiment(c.text)
        c.save()

