import feedparser
from urllib.parse import urlparse
from os.path import splitext
import requests
import os

def download_episode(url, filename):
	"""
	Function to download the audio files from Podcast episodes
	"""
	try:
		#Download Podcast Episode
		response = requests.get(url)
	except requests.exceptions.RequestException as e:
		print("Failed to download " + filename)
		print(e)
	else:
		try:
			#Save audio file locally for processing
			with open(filename, "wb") as f:
				f.write(response.content)
		except:
			print("Failed to save file")

def podcast_processor(url, limit = -1):
	"""
	Function to parse podcast URLs, turn audio episodes into videos, and upload them to YouTube
	"""
	NewsFeed = feedparser.parse(url)
	i = 0
	for entry in NewsFeed.entries :
		i += 1
		print("Title: " + entry["title"])
		print("Subtitle: " + entry["subtitle"])
		for link in entry["links"] :
			if link["rel"] == "enclosure" :
		
				parsed = urlparse(link["href"])
				root, ext = splitext(parsed.path)
				filename = entry["episodeid"] + ext
				download_episode(link["href"], filename)
		if os.path.exists(filename):
			print("Do Stuff Here")

			#Delete proccesed audio file
			os.remove(filename)
		if (limit != -1 and i >= limit) :
			break

podcast_processor("http://feeds.feedburner.com/dailyaudiobiblekids.xml", 1)