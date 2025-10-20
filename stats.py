def get_num_words(text):
    num_words = text.split()
    return f"Found {len(num_words)} total words"

def get_num_chars(text):
    counts = {}
    for c in text:
        char = c.lower()
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list = []
    for key, value in dict.items():
        list.append({ "char": key, "num": value })

    list.sort(reverse=True, key=sort_on)
    return list

def print_report(path, word_count, char_count):
    print(
        f"""
        ============ BOOKBOT ============
        Analyzing book found at {path}...
        ----------- Word Count ----------
        Found {word_count} total words
        --------- Character Count -------
        """
    )
    list = sort_dict(char_count)
    for c in list:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")