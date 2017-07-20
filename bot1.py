#! python3

#This will be a twitter bot trial and error - may evolve into something more useful.

import tweepy, time
from random import randint

consumer_key = "7j0MW9w0TpO7GzHlOIlUxTyt9"
consumer_secret = "8J9bTvQUH9gynASVnrq0wJ4TGrZSFxYlzR5nS5jjyOEYjHEjlT"
access_key = "885552913522860033-XwXX7V6c5f0VUbHxIVrEa7zXa0ohqP2"
access_secret = "Z9m1qPXqZAn0gpvf3y4yZLZm0toAyi0MqDkrPAidc7fCJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

user_id = "Chris Kansas"

responses = ["Spiderman?! What has that creep been up to?",
"Spiderman?!?!? Get me some pictures now!",
"What a menace to society!",
"Why wear a mask? Why doesn't he show his face?",
"Spider-Man, Hero or Menace? Exclusive Daily Bugle Photos."]

#api.update_status("#HelloWorld - This is JonahBot's first tweet!")
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        #print(status.text)
        print(status.user.screen_name)
        api.update_status("@" + status.user.screen_name + " " + responses[randint(0, 4)])

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow=["348260063"], track = ["#spiderman"]) #This will track a specific user by user_id and it will track anytime someone tweets "spiderman"

#for follower in tweepy.Cursor(api.followers).items():
    #follower.follow()
    #print(follower.screen_name)

#for i in range(5):
    #random_number = randint(0, 100)
    #api.update_status("%s is my favorite number right now." % (random_number))
    #time.sleep(20)
