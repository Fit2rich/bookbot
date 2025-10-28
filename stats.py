def count_words(text):
    words = text.split()
    num_words  = len(words)
    return num_words



def count_characters(text):
    char_counts = {}
    text = text.lower()

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(item):
    return item["num"]


def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        sorted_list.append({"char": char, "num": num})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list