def anagrams(word, word_list):
    sorted_word = sorted(word)
    anagrams_list = []

    for w in word_list:
        sorted_w = sorted(w)
        if sorted_w == sorted_word:
            anagrams_list.append(w)

    return anagrams_list


word = "cinema"
word_list = ["iceman", "anemic", "manic", "camera", "dog", "icemen"]
anagrams_list = anagrams(word, word_list)
print(anagrams_list)