def main():

	path_to_file = "books/frankenstein.txt"
	text = read_book_text(path_to_file)
	print(f"--- Begin report of {path_to_file} ---")
	print(f"{get_count_words(text)} words found in the document\n")
	letters_dict = get_count_letter(text)
	for letter in letters_dict: 
		if letter.isalpha(): 
			print(f"The \'{letter}\' character was found {letters_dict[letter]} times")
	print("--- End report ---")
def read_book_text(book_path):
	with open(book_path) as f:
		book_text = f.read()
		return book_text
def get_count_words(text):
	words = text.split()
	return len(words)
def get_count_letter(text):
	letter_frequency = {}
	lowercase_text = text.lower()
	for letter in lowercase_text:
		if letter not in letter_frequency:
			letter_frequency[letter] = 1
		else:
			letter_frequency[letter] += 1
	return letter_frequency		
	
main()
