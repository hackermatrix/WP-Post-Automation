import requests
from bs4 import BeautifulSoup
import nltk
from newspaper import Article
# nltk.download('punkt')

def scrape(url):
    # url = 'https://news.google.com/rss/articles/CBMiZGh0dHBzOi8vcHVuZW1pcnJvci5jb20vZW50ZXJ0YWlubWVudC91bndpbmQvdGhpbmdzLXRvLWRvLWluLXB1bmUtdGhpcy13ZWVrZW5kLTAwMzUvY2lkMTY5Mzg4MjY1MS5odG3SAQA?oc=5'

    content = Article(url)
    content.download()
    content.parse()
    content.nlp()

    # Retur the extracted values 
    return {"title":f"{content.title}", "content":f"{content.text}"}