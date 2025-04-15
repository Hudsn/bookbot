def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_char_freq(text: str) -> dict[str, int]:
    d = {}
    for char in text:
        c = char.lower()
        if c in d:
            d[c] +=1
        else:
            d[c] = 1
    return d

def sort_freqs(freq: dict[str, int]) -> list[dict[str, any]]:
    ret = []
    for char in freq:
        count = freq[char]
        char_dict = {}
        char_dict["char"] = char
        char_dict["count"] = count
        ret.append(char_dict)
    ret.sort(reverse=True, key=freq_sort)
    return ret

def freq_sort(dict):
    return dict["count"]