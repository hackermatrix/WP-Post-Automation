import feedparser
import urllib
# URL of the Pune Mirror RSS feed on Google News
def rss_feed(query):
    query = urllib.parse.quote(query)
    rss_url = f"https://news.google.com/rss/search?q={query}"

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)


    feeds = [{"title":entry.title,"link":entry.link,"comp_stat":False} for entry in feed.entries]
    
    return feeds
