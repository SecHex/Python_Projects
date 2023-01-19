import tweepy

# Set up the API keys
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Gather information
user = api.get_user("username")
print("Username: ", user.screen_name)
print("Followers: ", user.followers_count)
print("Bio: ", user.description)

# Get user's tweets
tweets = api.user_timeline(screen_name="username", count=10)
for tweet in tweets:
    print(tweet.text)
