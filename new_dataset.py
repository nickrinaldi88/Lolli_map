# import breitbart data
# create csv of word, word_count
# for each word, get sum of all word_count
# store value in word_count column
# Create lollipop graph, x axis = total, y axis = word

import csv


with open("breitbartData.csv") as the_csv:
	csv_reader = csv.reader(the_csv)
	data = list(csv_reader)
	del data[0]
	print(data)
	our_dict = {}
	keys_ = []
	total = 0
	for row in csv_reader:
		if row[1] not in keys_ and row[1] != "Word":
			keys_.append(row[1])

	for line in data:
		our_dict[l]


	# for key in keys_:
		# for newrow in csv_reader:
		# 	print(newrow)
	
		
