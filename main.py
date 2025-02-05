def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    counted_chars = count_chars(file_contents)
    counted_words = count_words(file_contents)
    print_report(counted_chars, counted_words)

def count_words(text):
    return len(str.split(text))

def count_chars(text):
    text = str.lower(text)
    all_letters = {}
    for letter in text:
        if letter not in all_letters.keys():
            all_letters[letter] = 1
        else:
            all_letters[letter] += 1

    return all_letters

def sort_on(dict):
    return dict["amount"]

def print_report(dict, words):
    filtered_list = []
    for key in dict.keys():
        if key.isalpha():
            filtered_list.append({"letter": key, "amount": dict[key]})
    print(filtered_list)

    filtered_list.sort(reverse=True, key=sort_on)
    print('--- Begin report of books/frankenstein.txt ---')
    print(str(words) + " words found in the document\n")

    for counted in filtered_list:
        print(f'The \'{counted["letter"]}\' character was found {counted["amount"]} times')
        
    
    print("--- End report ---")
    


main()