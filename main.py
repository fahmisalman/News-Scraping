from newspaper import Article
import argparse
import json

def parser(url):
    article = Article(url)
    article.download()
    article.parse()

    res = {}
    
    res['text'] = article.text
    res['authors'] = article.authors
    res['publish_date'] = article.publish_date
    res['keywords'] = article.keywords

    return res

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=False,
	help="Input url that will be parsed")
ap.add_argument("-t", "--title", required=False,
	help="Input title that will be saved")
args = vars(ap.parse_args())

url = 'https://en.wikipedia.org/wiki/Ice_cream'
title = 'data'

if args['url']:
    url = args['url']

if args['title']:
    title = args['title']

try:
    with open('Result/{}.txt'.format(title), 'w') as f:
        json.dump(parser(url), f)
        print('Success')
except:
    print('There is a problem connecting to URL')