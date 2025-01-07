class Book:
    def __init__(self, title, author, genre, year):
        self.title = title 
        self.author = author 
        self.genre = genre
        self.year = year
        
frankenstein = Book("Frankenstein", "Mary Shelley", "Horror", 1818)
it = Book("The IT Book", "The IT Book", "IT", 2019)
james_bond = Book("James Bond", "James Bond", "Action", 2019)
bible = Book("The Bible", "The Bible", "Religion", 0)
new_testament = Book("The New Testament", "The New Testament", "Religion", 100) 

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
