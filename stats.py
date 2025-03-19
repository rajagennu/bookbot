def get_num_words(words):
	# empty dict

	letter_count = {}

	# count words 
	for word in words:
	    for char in word.lower():
	        if char in letter_count:
	            letter_count[char] += 1
	        else:
	            letter_count[char] = 1

	# print(letter_count)
	return letter_count