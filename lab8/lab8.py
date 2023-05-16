from abc import ABC, abstractmethod


class FrequencyCounter(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_list = [0] * 26
        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        index = ord(char.lower()) - ord('a')
                        frequency_list[index] += 1
        for i, freq in enumerate(frequency_list):
            letter = chr(i + ord('a'))
            print(f'{letter} = {freq}')


class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_dict = {}
        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        frequency_dict[char] = frequency_dict.get(char, 0) + 1
        for letter, freq in frequency_dict.items():
            print(f'"Updated version: "{letter}" {freq}')


list_counter = ListCount("weirdWords.txt")
list_counter.calculateFreqs()

print("")

dict_counter = DictCount("weirdWords.txt")
dict_counter.calculateFreqs()
