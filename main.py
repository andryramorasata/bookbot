def main():
    #for PAT
	path_to_file = "books/frankenstein.txt"
	text = read_book_text(path_to_file)
	print(f"--- Begin report of {path_to_file} ---")
	print(f"{get_count_words(text)} words found in the document\n")
	letters_dict = get_count_letter(text)
	sorted_letters = dict_to_sorted_list(letters_dict)
	for item in sorted_letters:
		if item["letter"].isalpha():
			print(f"The \'{item["letter"]}\' character was found {item["count"]} times")
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
def dict_to_sorted_list(dict):
	list = []
	for char in dict:
		list.append({"letter": char, "count": dict[char]})
	list.sort(reverse = True,  key=sort_key)
	return list
def sort_key(dict):
	return dict["count"]
main()
