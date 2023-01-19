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

# Search for tweets containing the keyword
tweets = api.search(q="Keyword", count=10)

# Print the tweets and user information
for tweet in tweets:
    print("Username: ", tweet.user.screen_name)
    print("Followers: ", tweet.user.followers_count)
    print("Tweet: ", tweet.text)
    print()
