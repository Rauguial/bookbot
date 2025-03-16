def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text):
    lower_case = text.lower()
    dictionary = {}
    for character in lower_case:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
    return dictionary

def sort_on(item):
    return item["count"]

def sort_characters(char_dict):
    char_list = [{"char": char, "count": count} for char, count in char_dict.items() if char.isalpha()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    