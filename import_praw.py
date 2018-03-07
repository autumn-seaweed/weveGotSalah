import praw
import pdb
import re
import os

reddit = praw.Reddit('weveGotSalah')

# reddit =  praw.Reddit(client_id='u3F2faOGbGCp9Q', client_secret='uHxlzJ6XT-6eYbG1ysQLH2Q_E3g',password='AZc1zRxFr4P3',username='weveGotSalah',user_agent='Salah Bot 0.1')

subreddit = reddit.subreddit('akitest')

for submission in subreddit.hot(limit=5):
	print('Title: ', submission.title)
	print('Score: ', submission.score)
	print('---------------------------\n')

