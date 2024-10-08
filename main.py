def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = words_counter(text)
    num_char = char_counter(text)
    new_list = convert_dict_into_list(num_char)
    new_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for element in new_list:
        print(f"the {element['letter']} character was found {element['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def words_counter(text):
    words = text.split()
    return len(words)

def char_counter(text):
    letters = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

    return letters

def convert_dict_into_list(dict):
    list = []
    
    for key in dict:
        list.append({"letter": key, "num": dict[key]})

    return list


def sort_on(dict):
    return dict["num"]


main()