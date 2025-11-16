def word_count(text):
    words = text.split()
    return len(words)

def get_character_num(text):
    char_count = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(char):
    return char["num"]

def sort_char(char_count):
    char_list = []
    for char in char_count:
        new_dict = {"char": char, "num": char_count[char]}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list