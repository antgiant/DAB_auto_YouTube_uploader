import feedparser
from urllib.parse import urlparse
from os.path import splitext
import requests
import os
NewsFeed = feedparser.parse("http://feeds.feedburner.com/dailyaudiobiblekids.xml")
i = 0
for entry in NewsFeed.entries :
	i += 1
	print("Title: " + entry["title"])
	print("Subtitle: " + entry["subtitle"])
	for link in entry["links"] :
		if link["rel"] == "enclosure" :
			parsed = urlparse(link["href"])
			root, ext = splitext(parsed.path)
			response = requests.get(link["href"])
			open(entry["episodeid"] + ext, "wb").write(response.content)
			if os.path.exists(entry["episodeid"] + ext):
				print("Do Stuff Here")
				os.remove(entry["episodeid"] + ext)
	if (i > 0) :
		break