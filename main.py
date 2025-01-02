def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        characters = chars(file_contents)
        char_count = count(file_contents)
        print(f"There are {char_count} words in the text.")
        characters_sorted = sorted(characters.items(), key=lambda x: -x[1])
        for char, freq in characters_sorted:
            print(f"The character '{char}' appears {freq} times.")
        print("--- End of report ---")

def count(text):
    return len(text.split())

def chars(text):
    unique = {}
    text_lower = text.lower()
    for t in text_lower:
        if t.isalpha():
            if t not in unique:
                unique[t] = 1
            else:
                unique[t] += 1
    return(unique)

main()
