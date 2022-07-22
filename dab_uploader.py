import feedparser
NewsFeed = feedparser.parse("http://feeds.feedburner.com/dailyaudiobiblekids.xml")
for entry in NewsFeed.entries :
	print("Title: " + entry["title"])
	print("Subtitle: " + entry["subtitle"])
	for link in entry["links"] :
		if link["rel"] == "enclosure" :
			print("Link: " + link["href"])
	print("Episode ID: " + entry["episodeid"])