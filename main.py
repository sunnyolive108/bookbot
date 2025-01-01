def count_words(text):
    
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()

    character_count = {}

    for char in text:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1

            else:
                character_count[char] = 1
            
    return character_count

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()
    
    print("--- Begin report of books/frankenstein.txt ---")

    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")

    character_count = count_characters(file_contents)
    for char, count in character_count.items():
        print(f"The {char} character was found {count} times")
        
    print("--- End report ---")

if __name__ == "__main__":
    main()
