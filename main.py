def get_book_text(book):
  with open(book) as f:
    return f.read()
  return(file_contents)

def count_words(book_string):
  num_words = len(book_string.split())
  print(f'{num_words} words found in the document')

def main():
  count_words(get_book_text("./books/frankenstein.txt"))

main()
