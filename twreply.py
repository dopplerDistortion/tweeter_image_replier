import tweepy
import time
import datetime
import sys
import picamera
from random import randint

CONSUMER_KEY = "UvibSZAxxs7YrBkJX7tYHiTQa"
CONSUMER_SECRET = "FxORXf9fxcx42TjS2zs7QQPhMLWdIbVhg21x3zPwYbZr8FQlVl"
ACCESS_KEY = "3354785446-XBPcIpXcilNWUAdqXC0tt2hw24kw5aobcCikd61"
ACCESS_SECRET = "wIYknOPFUwlsI0cVnzegD9qtrzTQpJFfsSYXSqroNVHV6"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
camera = picamera.PiCamera()
filename = '/home/pi/Desktop/Yeni/temp.jpg'


class streamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        user = status.user.screen_name
        randQuote = 'It is ' + st + ' and welcome to MakerDay #live #makermovement #beta #makercocuk'
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
    stream.filter(track=['#makerlablive'])
