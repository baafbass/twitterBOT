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
		time.sleep(1000)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	print(follower.name) # will print all the my followers
	if follower.name == 'Nabila Bassirou':
		follower.follow() # Will follow 'Nabila' From my followers
