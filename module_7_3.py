from idlelib.iomenu import encoding


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        znaki = ',.=!?:; - '
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                words = []
                for line in f:
                    line = line.lower()
                    for char in znaki:
                        line = line.replace(char, ' ')  # Заменяем пунктуацию на пробел
                    words.extend(line.split())
                all_words[file] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file in all_words:
            if word in all_words[file]:
                result[file] = all_words[file].index(word) + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file in all_words:
            result[file] = all_words[file].count(word)
        return result




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего