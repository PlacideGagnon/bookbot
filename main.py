def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = book_length(text)
    characters = character_count(text)
    sorting = sorting_func(characters)
    print("---------Info about books/frankenstein.txt---------")
    print(f"{word_count} words in the document.")
    print('\n')
    for x in sorting:
        print(f"The {x['character']} character was used {x['number']} times.")
    print("---------End about books/frankenstein.txt---------")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def book_length(words):
    return len(words.split())

def character_count(text):
    number_of_characters = {}
    for character in text.lower():
        if character.isalpha():
            if character not in number_of_characters:
                number_of_characters[character] = 1
            elif character in number_of_characters:
                number_of_characters[character] += 1
    return number_of_characters

def sort_on(dict):
    return dict["number"]

def sorting_func(d):
    new_list = []
    for i in d:
        temp_dict = {"character": i, "number": d[i]}
        new_list.append(temp_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

main()