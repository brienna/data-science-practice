import sys
import json


def analyzeSentiment(tweet, scores):
    words = tweet.split()  # splits tweet into words
    total = 0
    for word in words:  # for word in tweet
        if word in scores:  # if word is a sentiment term
			total += scores[word]  # add sentiment score to total
    print total


def main():
	# creates dictionary of terms and sentiment scores
    afinnfile = open("AFINN-111.txt")
    scores = {}
    for line in afinnfile:
    	term, score = line.split("\t")  # cuz the file is tab-delimited
    	scores[term] = int(score)  # assigns score to term

    # parses tweets
    tweetFile = open(sys.argv[1])
    for line in tweetFile:
    	parsedJSON = json.loads(line)  # parses line into, for this, a dictionary
    	if 'text' in parsedJSON:  # if dictionary contains text as key
    		analyzeSentiment(parsedJSON['text'], scores)  # derive text's sentiment
    	else:  # if dictionary doesn't contain text field
    		print 0  # tweet contains no sentiment


if __name__ == '__main__':
    main()
