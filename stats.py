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

def sort_on(d):
  return d["num"]

def chars_dict_to_sorted_list(char_count_dict):
  sorted_list = []
  for c in char_count_dict:
    sorted_list.append({"char": c, "num": char_count_dict[c]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list