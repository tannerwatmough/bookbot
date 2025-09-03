from stats import count_words, count_chars

def get_book_text(book):
  with open(book) as f:
    return f.read()
  return(file_contents)

def main():
  word_count = count_words(get_book_text("./books/frankenstein.txt"))

  print(f'{word_count} words found in the document')

  print(count_chars(get_book_text("./books/frankenstein.txt")))

main()
