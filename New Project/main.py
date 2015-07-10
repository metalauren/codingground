# Hello World program in Python
   
tweetfile = open("tweets.txt", "r") 	#open file
alltweets = tweetfile.read() 		#read the file
tweets = alltweets.splitlines() 	#a list where each element is an tweet 

runningmedians = []
wordsintweet = []

def median(x):
    x.sort()
    mid = len(x) // 2
    if len(x) % 2:
        return x[mid]
    else:
        return (x[mid - 1] + x[mid]) / 2.0

for i in range(0,(len(tweets))):
    tweets[i] = tweets[i].split()	#splits each tweet into a list of words
    for j in range(0,(len(tweets[i]))):
        if tweets[i][j][-1] in [".",",","?","!",":",";"]:
            tweets[i][j] = tweets[i][j][0:-1] #cuts off basic punctuation from the end of a word
    wordsintweet.append(len(tweets[i]))
    runningmedians.append(median(wordsintweet))
print tweets
print wordsintweet
print runningmedians

print tweets[0][7][0:7]


