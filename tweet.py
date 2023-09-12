import tweepy

auth = tweepy.OAuthHandler('es1YvJmHHUsxB9y9eyxLeDB0R','tDyAkniVzcuyfung0PLWqJIUlG2JKj9arzEi4lY39v0tlctVTu')
auth.set_access_token('1302250654535221251-UmMSwLneYzMLSldeiBba3AQOlkJdFb', 'aCnzx2PzIvXACG0zHmHoO3rvqnI3Z10R2H1Hy4iX0YDjY')

api = tweepy.API(auth)

public_tweets = api.home_timeline() 
for tweet in public_tweets:
    print(tweet.text) # Will print the tweets from our home_timelines

user = api.me() # Get my twitter profile
print(user.name) # To get our profile name
print(user.follwers_count)
