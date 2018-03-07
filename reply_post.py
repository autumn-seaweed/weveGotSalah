

import praw
import pdb
import re
import os
import time

# create new Reddit instance
reddit = praw.Reddit('weveGotSalahBot')

# Have we run this code before? If not, create an empty list


def get_comments():
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))
    return comments_replied_to
    f.close()

# Write our updated list back to the file
def append_comments(com_list):
    with open("comments_replied_to.txt", "w") as f:
        for comment_id in com_list:
            f.write(comment_id + "\n")
    f.close()

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('liverpoolFC')


while True:
    print('Getting comments previously replied to...')
    comments_replied_to = get_comments()
    # print(comments_replied_to)

    print('Getting 100 comments...')
    for comment in subreddit.comments(limit=100):
        # print(comment.body)
        if comment not in comments_replied_to:
            if re.search("weve got Salah", comment.body.replace("'",""), re.IGNORECASE):
                # Store the current id into our list
                bot_reply = "Oh Mane Mane dododoodo do doo dodooo"
                comment.reply(bot_reply)
                print('Replied to comment ', comment.body)
                comments_replied_to.append(comment.id)
    print('Appending comments to list of comments...')
    append_comments(comments_replied_to)

    time.sleep(10)
