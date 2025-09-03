from stats import *

def get_book_text(book):
  with open(book) as f:
    return f.read()
  return(file_contents)

def main():
  word_count = count_words(get_book_text("./books/frankenstein.txt"))

  char_count_dict = count_chars(get_book_text("./books/frankenstein.txt"))

  sorted_dict_list = chars_dict_to_sorted_list(char_count_dict)

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f'Found {word_count} total words')
  print("--------- Character Count -------")
  for item in sorted_dict_list:
    if item["char"].isalpha():
      print(f"{item['char']}: {item['num']}")
  print("============= END ===============")

main()
