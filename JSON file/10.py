"""
Author: passa-
Problem: 10 L14 twitter
Student Code: 6510503310
Branch: Computer Engineering
"""

import json

def read_file():
    file_name = input("File name: ")
    data = json.loads(open(file_name).read())
    return data

def tweet_count(data):
    print(len(data))

def user_count(data):
    user = []
    for tweet in data:
        if tweet["author"] not in user:
            user.append(tweet["author"])
    print(len(user))

def most_active(data):
    author_lst, tweet_lst, most_active_lst = [], [], []
    for tweet in data:
        if tweet["author"] not in author_lst:
            author_lst.append(tweet["author"])
            tweet_lst.append(1)
        else:
            idx = author_lst.index(tweet["author"])
            tweet_lst[idx] += 1
    for i in range(len(author_lst)):
        most_active_lst.append([author_lst[i], tweet_lst[i]])
    maxx = sorted(most_active_lst, key = lambda x:x[1])[-1][1]
    for most_active in most_active_lst:
        if most_active[1] == maxx:
            print(most_active[0])

def topic_count(data):
    topic = []
    for tweet in data:
        if tweet["topic"] not in topic:
            topic.append(tweet["topic"])
    print(len(topic))

def alert_count(data):
    count = 0
    for tweet in data:
        if tweet["topic_priority"] == "ALERT":
            count += 1
    print(count)

def unimportant_count(data):
    count = 0
    for tweet in data:
        if tweet["topic_priority"] == "UNIMPORTANT":
            count += 1
    print(count)

def is_any_not_eng(data):
    for tweet in data:
        if tweet["language"] != "EN":
            print(True)
    print(False)

def most_word_count(data):
    maxx = 0
    for tweet in data:
        word_count = len(tweet["text"].split())
        if word_count > maxx:
            maxx = word_count
    print(maxx)

## main ##

data = read_file()
option = int(input("input: "))
if option == 1:
    tweet_count(data)
elif option == 2:
    user_count(data)
elif option == 3:
    most_active(data)
elif option == 4:
    topic_count(data)
elif option == 5:
    alert_count(data)
elif option == 6:
    unimportant_count(data)
elif option == 7:
    is_any_not_eng(data)
elif option == 8:
    most_word_count(data)