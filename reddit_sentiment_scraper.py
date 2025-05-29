import praw
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

REDDIT_CLIENT_ID = 'H6MBg-N454MP5d9jN-2rrw'
REDDIT_SECRET = 'atzaqZF_2Kn6L54sw_9W5Cqk0wEvRg'
REDDIT_USER = 'Dischargezz'
REDDIT_PWD = 'Copper1.'

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent='sentiment_bot',
    username=REDDIT_USER,
    password=REDDIT_PWD
)

analyzer = SentimentIntensityAnalyzer()

# TODO: tweak this search to fetch more relevent and meaningful posts
def fetch_sentiment(coin_keyword, subreddits=None, limit_per_sub=100, max_comments=10):
    if subreddits == None:
        subreddits = [
            'cryptomoonshots',
            'SatoshiStreetBets',
            'CryptoCurrency',
            'CryptoMarkets',
            'AltcoinTalk',
            'ShitcoinStreet'
            ]
    
    results = []
    
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        query = f'title:"${coin_keyword}" OR "{coin_keyword.lower()}coin" OR "{coin_keyword.upper()}"'
        posts = subreddit.search(query, sort='new', time_filter='year', limit=limit_per_sub)

        for post in posts:
            post.comments.replace_more(limit=0)
            comments = post.comments[:max_comments]
            comments_sentiments = []
            for comment in comments:
                text = comment.body
                if text: 
                    sentiment = analyzer.polarity_scores(text)['compound']
                    comments_sentiments.append(sentiment)

            avg_comments_sentiments = sum(comments_sentiments) / len(comments_sentiments) if comments_sentiments else 0.0

            title_sentiment = analyzer.polarity_scores(post.title)['compound']

            body_sentiment = analyzer.polarity_scores(post.selftext)['compound'] if post.selftext else 0.0

            sentiments = [title_sentiment]

            if post.selftext: 
                sentiments.append(body_sentiment)
            if comments_sentiments:
                sentiments.append(avg_comments_sentiments)

            avg_sentiment = sum(sentiments) / len(sentiments)

            post_score = max(post.score, 1)  # avoid zero weights

            results.append({
                'Date': datetime.fromtimestamp(post.created_utc).date(),
                'Coin': coin_keyword.upper(),
                'Subreddit': subreddit_name,
                'Title': post.title,
                'Sentiment': avg_sentiment * post_score,
                'Score': post_score
            })

    return pd.DataFrame(results)

if __name__ == "__main__":
    subs = []
    df = fetch_sentiment('PEPE', limit_per_sub=100)
    df.to_csv("data/reddit_sentiment_pepe.csv", index=False)
    print(df.head())