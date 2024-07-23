import praw 
import pandas as pd
from datetime import datetime

# Reddit API credentials
redit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent=''
)

def collect_data():
    # Connect to the worldnews subreddit
    subreddit = reddit.subreddit('worldnews')

    # Retrieve the 100 most recent posts
    new_posts = subreddit.new(limit=100)

    # Create a list to store past data
    post_data = []
    for post in new_posts:
        # Append each post's data to the list
        posts_data.append({
            'id': post.id, 
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'created_utc': post.created_utc,
            'upvote_ratio': post.upvote_ratio
        })

        # Convert the list of posts to a DataFrame and save to CSV
        df = pd.DataFrame(post_data)
        # Conver timestamp to datetime
        df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
        # Save DataFrame to CSV file
        df.to_csv('reddit_worldnews.csv', index=False)

if __name__ == "__main__":
    # Run the function to collect data
    collect_data()