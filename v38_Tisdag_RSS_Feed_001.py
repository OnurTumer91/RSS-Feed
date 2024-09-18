# RSS FEED
import feedparser

def parse_rss(url):
    feed = feedparser.parse(url)

    print(f"{feed.feed.title}")

    for entry in feed.entries:
        print(f"Title: {entry.title},\nLink: {entry.link}")

rss_url= 'https://feeds.bbci.co.uk/news/stories/rss.xml/'
parse_rss(rss_url)