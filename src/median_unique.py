'''
median_unique_v1a
Created on Jul 10, 2015
@author: MatthewRubashkin
'''

#import modules
import os
import csv
import numpy

#Establish directories for extracting tweet information and writing tweet outputs
src_DIR = os.path.join( os.path.dirname( __file__ ), '..' )
GLOBAL_DIR=os.path.dirname(os.path.dirname(src_DIR))

#Declare text file names for future operations 
tweet_input_filename= "".join((GLOBAL_DIR, 'tweet_input/tweets.txt'))
tweet_output_ft1_filename= "".join((GLOBAL_DIR, 'tweet_output/ft1.txt'))
tweet_output_ft2_filename= "".join((GLOBAL_DIR, 'tweet_output/ft2.txt'))

#Create output counters
median_words_per_tweet = [] #counts individual tweets
median_unique = [] #analyzes median unique by homework parameters

#Open tweets and save as a list of lists
with open(tweet_input_filename, 'r') as f:
    tweets = f.readlines() #read all tweets line by line
    for line in tweets:
        words = line.split() #seperate words by spaces
        
        #Solve for median_unique ft2 output
        unique_words = [] #list from individual tweets
        for word in words:
            if word not in unique_words: ##skips replicates in a given list
                unique_words.append(word)    
        median_words_per_tweet.append(len(unique_words)) #store words per tweet
        
        #use numpy to get median of an array
        median_unique.append(numpy.median(numpy.array(median_words_per_tweet)))

#Write median_unique to file
file = open(tweet_output_ft2_filename, "w")
for median in median_unique:
    file.write(str(median)+ '\n')
#file.writelines(map(str,median_unique)) #use map command to convert to string
file.close()
print 'median_unique answer: ', median_unique
