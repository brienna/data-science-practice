import sys
import json


def termCount(tweet, counted):
	tweet = tweet.encode("ascii", "ignore")
	words = tweet.split() # splits tweet into words
	for word in words: # for each word
		if word in counted: # if word exists in 'count'
			counted[word] += 1 # add 1 to its frequency
		else: # if word doesn't exist in 'count'
			counted[word] = 1 # add the word with initial frequency of 1
	return counted


def main():
	tweetFile = open(sys.argv[1])
	counted = {}
	for line in tweetFile:
		parsedJSON = json.loads(line)  # parses line into, for this, a dictionary
		if 'text' in parsedJSON:  # if dictionary contains text as key
			termCount(parsedJSON['text'], counted)
	
	totalCount = 0 # occurrences of all terms in all tweets
	for term in counted:
		totalCount += counted[term]
	for term in counted: 
		count = counted[term] # occurrences of the term in all tweets	
		frequency = count/float(totalCount)
		print term, ("%.10f" % frequency)


if __name__ == '__main__':
	main()
