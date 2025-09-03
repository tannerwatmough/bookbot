import sys
from stats import *

def get_book_text(book):
  try:
    with open(book) as f:
      return f.read()
  except Exception as e:
    print(f"Error encountered: {e}")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  word_count = count_words(get_book_text(sys.argv[1]))
  char_count_dict = count_chars(get_book_text(sys.argv[1]))

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
