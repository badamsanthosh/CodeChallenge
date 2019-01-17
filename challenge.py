DICT_FILE_PATH = "/usr/share/dict/words"


class Anagrams:

    def __init__(self):
        pass

    @staticmethod
    def contains(bigger, smaller):
        if len(bigger) >= len(smaller):
            while smaller:
                this, smaller = smaller[0:1], smaller[1:]
                if this not in bigger:
                    return None
                bigger = bigger.replace(this, '', 1)
            return bigger

    @staticmethod
    def trim_word(word):
        return word.lower().strip()

    def find_anagrams(self, word, words, atleast):
        for word_index, current_word in enumerate(words):
            remaining_letters = Anagrams.contains(word, current_word)
            if remaining_letters == '':
                yield current_word
            elif remaining_letters is not None and len(remaining_letters) >= atleast:
                for x in self.find_anagrams(remaining_letters, words[word_index:], atleast):
                    yield (' '.join((current_word, x)))


if __name__ == '__main__':
    cc = Anagrams()
    input_string = "School master"
    words = Anagrams.trim_word(input_string)
    dictionary_file = DICT_FILE_PATH

    smallest = min(map(len, input_string.split(" ")))

    words_list = []
    with open(DICT_FILE_PATH) as word_file:
        for each_word in word_file:
            words_list.append(each_word.strip())

    solution_number = 0
    for _, word in enumerate(cc.find_anagrams(words, words_list, smallest), 1):
        print(word)
