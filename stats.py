def get_word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_text = text.lower()
    dict = {}
    for char in lower_text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(d):
    return d["num"]

def character_sort(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append({"char": key, "num":dictionary[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list