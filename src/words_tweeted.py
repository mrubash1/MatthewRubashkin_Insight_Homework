'''
median_unique_v1a
Created on Jul 10, 2015
@author: MatthewRubashkin
'''

#import modules
import os
import csv
from collections import Counter

#Establish directories for extracting tweet information and writing tweet outputs
src_DIR = os.path.join( os.path.dirname( __file__ ), '..' )
GLOBAL_DIR=os.path.dirname(os.path.dirname(src_DIR))

#Declare text file names for future operations 
tweet_input_filename= "".join((GLOBAL_DIR, 'tweet_input/tweets.txt'))
tweet_output_ft1_filename= "".join((GLOBAL_DIR, 'tweet_output/ft1.txt'))
tweet_output_ft2_filename= "".join((GLOBAL_DIR, 'tweet_output/ft2.txt'))

#Create output list of lists
all_words = []
unique_words = []
unique_word_count= []
count = 0

#Open tweets and save as a list of lists
with open(tweet_input_filename, 'r') as f:
    tweets = f.readlines() #read all tweets line by line
    for line in tweets:
        words = line.split() #separate words by spaces
        
        #Solve for words_tweeted ft1 output
        for word in words:
            if word not in unique_words: #keep track of the unique words there are in an array
                unique_words.append(word)
                unique_word_count.append(1) #increase the size of the unique word counting array
            else:
                unique_word_count[unique_words.index(word)] += 1 #store the count of this repeated word

                
                
#Combine unique_word array and unique_word_count array into a matrix, and sort
ft2_output = zip(unique_words, unique_word_count)
ft2_output = sorted(ft2_output, key=lambda y: y[0])

#output to command line
print 'words_tweeted answer: ', ft2_output

#Output data to ft2.txt file
unique_words, unique_word_count = zip(*ft2_output)
file = open(tweet_output_ft1_filename, "w")
counter=0
for word in unique_words:
    file.write(word +'       ' + str(unique_word_count[counter]) + '\n')
    counter += 1

