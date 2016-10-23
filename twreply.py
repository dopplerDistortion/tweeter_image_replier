import tweepy
import time
import datetime
import sys
import picamera
from random import randint

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
camera = picamera.PiCamera()
filename = ''


class streamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        user = status.user.screen_name
        randQuote = 'It is ' + st + ' and test tweet.'
        #gets their tweetid so you can reply to it
        tweetId = status.id
        #takes photo with picamera.
        camera.capture(filename)
        print("User:" + user + "\n    Message: " + status.text)
        message = "@{username} {quotation}".format(username=user, quotation=randQuote)
        #api.update_status(message, tweetId)
        api.update_with_media(filename, status=message)
		#prints what tweet was sent
        print("    Sent Tweet: {0}".format(message))
		
        return True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
 
    def on_timeout(self):
        print('Timeout...')
        return True
 
if __name__ == '__main__':
   

    print("Program initialized. Ready.")
    listener = streamListener()
    stream = tweepy.Stream(auth, listener)
	#checks for whatever you want. #seanrandomness was unused so i used it
    stream.filter(track=['#hastagtofollow'])
