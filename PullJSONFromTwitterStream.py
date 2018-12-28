from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import datetime

ckey = ''
csecret = ''
atoken = ''
asecret = ''
date = str(datetime.date.today())

keyword = 'song'

class listener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(date + 'TwitterStreamFilter_' + keyword + '.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[keyword])
