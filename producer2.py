from kafka import KafkaProducer
from kafka.errors import KafkaError
import tweepy, json
import unicodedata
import json
import logging

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.coordinates != None:
            coord = status.coordinates['coordinates']
        #coord={'lat':coord,'lng':10}
            msg=unicodedata.normalize('NFKD', status.text).encode('ascii','ignore')
            tweetData={'status': msg, 'lat': coord[1],'lng':coord[0]}
        #with open('stream1.json', 'a') as outfile:
        #tweetData={'status': str.encode(msg), 'lat': coord['lat'],'lng':coord['lng']}
#producer.send('test',key=b'tweet:',value=str.encode(msg))
        #json.dump(data, outfile)

            producer.send('test',key=b'tweet:',value=str.encode(json.dumps(tweetData)))

producer = KafkaProducer(bootstrap_servers=['52.23.195.196:9092'])

auth = tweepy.OAuthHandler("If0fS3VKZdyUan6O1JcSq2bjX", "wYRfUfdnses56sLPy1wK6TwDJd4Upcs9Xar0I1l4Fq681O7fMa")
auth.set_access_token("1559610186-hXMVpia7UoYq63RS3OzZURgAmJKJVOt9ityG0hG", "0X43VBxCd9pzRZsRjoT4LiW4bIQiO6DaWwbaAf437RNjv")
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

searchlist = ['Love','Trump', 'Hillary','Hate']
myStream.filter(track = searchlist)
                                    
