import tweepy
import time

auth = tweepy.OAuthHandler('es1YvJmHHUsxB9y9eyxLeDB0R','tDyAkniVzcuyfung0PLWqJIUlG2JKj9arzEi4lY39v0tlctVTu')
auth.set_access_token('1302250654535221251-UmMSwLneYzMLSldeiBba3AQOlkJdFb', 'aCnzx2PzIvXACG0zHmHoO3rvqnI3Z10R2H1Hy4iX0YDjY')

api = tweepy.API(auth)

user = api.me() # Get my twitter profile

def limit_handler(cursor):
	try:
	     while True:
		     yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(numbersOfTweets):
	try:
		tweet.favorite() # like the tweet
		tweet.retweet()
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

