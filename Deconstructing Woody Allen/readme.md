Who is who and which file does what:

woody_allen_screenplays.py and woody_allen_reviews.py --> we get screenplays from springfieldspringfield.co.uk and reviews on Woody Allen's films from rottentomatoes.com

rating_per_topics_maker.py --> it counts how many topics out of our 5 main themes appear in the topics of each screenplay

frequent_words_counter.py --> it makes a frequency dictionary of words out of set of reviews on each films (we ignore stopwords!)

en.txt --> file with stopwords used for mallet and frequency dictionary

xlsx-table --> frequency dictionary in Excel table

clusterization.png --> rezults of stylo cluster analysis of screenplays

Deconstructing Woody.pptx --> our Power-Point presentation


Folders:

screenplays --> all our analysed screenplays

reviews --> all our analysed reviews

keys, mallet, topics --> results of mallet analysis of screenplays (number of topics = 3)

main_topics.txt --> 5 themes made with mallet out of all topics of all Allen's screenplays
