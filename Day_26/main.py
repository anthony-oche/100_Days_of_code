import pandas


#Todo 1: read the csv file using panda
nato_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

#Todo 2: convert the file to a dictionary
nato_dict = {row.letter: row.code for (index, row) in nato_frame.iterrows()}

#Todo 3: create a list of the code words from a word the user inputs
word = input("Enter a word: ").upper()

code_list = [nato_dict[item] for item in word]
print(code_list)



