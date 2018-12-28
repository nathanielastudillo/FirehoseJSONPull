import json
import datetime

'''
Hey, you! Yeah, you. Want to pull something specific? (As this file is, it only writes user IDs)

Read this:

https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html

Filename is whatever you named it in PullJSONFromTwitterStream.
'''

filename = ''
date = str(datetime.date.today())
idLIST = open(date + 'IDLIST.txt','w')

with open(filename,'r') as f:

	for tweet in f: #I just want to pull the user ID.
		line = f.readline() #brings the line for a whole tweet into memory
		tweet = dict(json.loads(line)) #loads the line as a string, casts it as a dictionary
		idLIST.write(str(tweet['id'])+'\n')

#maybe modify this to write screen_name to a text file that can then be read out by another program that
#actually hits those users' profiles via. twitter.com/screen_name (use the automater thing?)