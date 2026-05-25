
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len()>15]
    re_df = df[['tweet_id']]
    return re_df