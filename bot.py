import feedparser

url = "https://news.google.com/rss/search?q=Fenerbahce&hl=en-US&gl=US&ceid=US:en"

feed = feedparser.parse(url)

print("===== FENERBAHÇE YABANCI BASIN =====")

for entry in feed.entries[:15]:
    title = entry.title
    link = entry.link

    if "source" in entry:
        source = entry.source.title
    else:
        source = "Bilinmeyen Kaynak"

    print(f"Kaynak: {source}")
    print(f"Başlık: {title}")
    print(f"Link: {link}")
    print("-" * 50)
