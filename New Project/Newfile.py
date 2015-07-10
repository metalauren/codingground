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
    wordsintweet.append(len(tweets[i]))
    runningmedians.append(median(wordsintweet))
    
print tweets[0][7]
    