def count_words(book_string):
  return len(book_string.split())

def count_chars(book_string):
  book_string = book_string.lower()
  char_count = {}
  for c in book_string:
    if c in char_count:
      char_count[c] += 1
    else:
      char_count[c] = 1
  return char_count