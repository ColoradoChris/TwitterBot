#! python3

#This will be a twitter bot trial and error - may evolve into something more useful.

import tweepy

consumer_key = "7j0MW9w0TpO7GzHlOIlUxTyt9"
consumer_secret = "8J9bTvQUH9gynASVnrq0wJ4TGrZSFxYlzR5nS5jjyOEYjHEjlT"
access_key = "885552913522860033-XwXX7V6c5f0VUbHxIVrEa7zXa0ohqP2"
access_secret = "Z9m1qPXqZAn0gpvf3y4yZLZm0toAyi0MqDkrPAidc7fCJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
