# Write a program to replace some words in the sentence below
# "Amazon Web Services" with its value in the following dictionary

sentence = "Amazon Web Services"
repWords = {
    "Amazon": "Amz",
    "Services": "Serves"
} 

# sentence_list = sentence.split()
# answer = [None] * len(sentence_list)

# for item in sentence_list:
#     if item in repWords.keys():
#         pos = sentence_list.index(item)  
#         answer[pos] = repWords[item] 
#     else:
#         new_pos = sentence_list.index(item) 
#         answer[new_pos] = item 
# answer = ' '.join(answer)
# print(answer) 

# final_string = ' '.join(repWords.get(word, word) for word in sentence_list)
# print(final_string)

# print(sentence.split())
# print(repWords.get('Aman', 'gh'))



