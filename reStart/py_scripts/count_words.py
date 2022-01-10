
import boto3 

def no_words(filename):
    number_of_words = 0
    with open(filename,'r') as file:
        data = file.read()
        lines = [i for i in data.split() if i.isalnum()]
        number_of_words += len(lines)
    # Printing total number of words
    return f'The word count in the file {filename} is {number_of_words}.' 

# text_filename, number = no_words('files/UserData.txt')
# text_filename = text_filename.split('/')[-1] 
# text_filename, number = no_words(filename)

# print(f'The word count in the file {text_filename} is {number}.')
print(no_words('files/UserData.txt'))


# [i for i in string.split() if i.isalnum()]
