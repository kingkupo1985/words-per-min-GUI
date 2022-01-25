# Please note this was originally stand alone and still has lines I should remove vs commenting out
# Author: David S. Kuhs
# Created on: 2022/20/01
# Project Name: Words Per Minute Checker
# Package Name: Word Generator and Error Checker

import random

class WordChecker():

    def __init__(self):
        self.word_list = []
        self.words_type = []
        self.users_word_list = []
        self.all_word_list = []
        self.total_words_typed = 0
        self.original_word_string = ''
        self.error_count = 0
        self.total_char_count = 0
        self.word_count = 0

    # Function Gets Data for Words from TXT file
    def get_data(self):
        self.word_list = []
        with open('english_words copy.txt', mode='r') as f:
            for line in f:
                word = line.strip()
                self.word_list.append(word)
        return self.word_list

    # Generates 10 random words to a list to be used in typing test
    def words_to_type(self, words):
        self.word_count = 0
        self.words_type = []
        while self.word_count != 3:
            random_word = random.randint(0, len(words) - 1)
            self.words_type.append(words[random_word])
            self.word_count += 1
        return self.words_type


    def start_words(self):
        ### Probably going to be the initialize function
        # Getting Data
        self.all_word_list = self.get_data()
        # Creating List
        self.original_word_list = self.words_to_type(self.all_word_list)
        # Show words you should match
        print(' '.join(self.original_word_list))
        self.original_word_string = ' '.join(self.original_word_list)
        # Get users input to see if they match need to add timer function to calculate WPM and loop for 10 sets of 10 words
        users_original_word_string = input("Please enter the words you see above as quickly and accurately as possible!\n"
                                           "It is case insensitive: ").upper()
        # get users words and split by ' ' to create a list to compare
        self.users_word_list = [word for word in users_original_word_string.split(' ')]
        self.total_words_typed = len(self.users_word_list)
        return self.count_errors(self.original_word_list, self.users_word_list)

    ### Function for checking words and getting wrror count
    def count_errors(self, original_list, user_list):
        # Initalize Error counter
        self.error_count = 0
        self.total_char_count = 0
        # Iterate through original wordlist
        for word in original_list:
            self.total_char_count += len(word)
        if len(original_list) == len(user_list):
            pass
            # print(f'You input {len(user_list)}')
        else:
            if user_list[0] == '' or user_list[0] == ' ':
                user_list = []
                # print(f'Total missing words: {len(original_list)}')
            missing_words = len(original_list) - len(user_list)
            # print(f'Total missing words: {missing_words}')
            for word in original_list[-missing_words:]:
                #print(f"missing word: {word} | word length: {len(word)}")
                self.error_count += len(word)
                # print(f'line 78 in loop errors currently {self.error_count}, word: {word}, word length{len(word)}')

        for o_word in original_list:
            # Iterate through users wordlist
            for u_word in user_list:
                # Compare original word to user word if matching ok and pass to next word
                if o_word == u_word:
                    # print(f'MATCHING PAIR: Original word: {o_word} | User Word: {u_word}')
                    break
                # Compare word if not matching && it is the same index we need to check the characters and word length
                elif o_word != u_word and original_list.index(o_word) == user_list.index(u_word):
                    # print(f'DID NOT MATCH: Original word: {o_word} | User Word: {u_word}')
                    # Compare word lengths and if not the correct length count missing spaces and increase error counter by len difference
                    if len(o_word) > len(u_word):
                        # print(f'line 55: {o_word}, total missing chars: {len(o_word) - len(u_word)}')
                        self.error_count += len(o_word) - len(u_word)
                    elif len(o_word) < len(u_word):
                        # print(f'line 55: {o_word}, total xtra chars: {(len(o_word) - len(u_word)) * -1}')
                        self.error_count += len(u_word) - len(o_word)
                    # iterate through each character in original word
                    for i in range(len(o_word)):
                        try:
                            if o_word[i] == u_word[i]:
                                pass
                                # print(f'Match @ o_word index: {i} / o_word char {o_word[i]} | u_word index: {i} / u_word char {u_word[i]}')
                            else:
                                self.error_count += 1
                                # print(f'NO Match @ o_word index: {i} / o_word char {o_word[i]} | u_word index: {i} / u_word char {u_word[i]}')
                        except IndexError as err:
                            pass
                            # print(f'Missing Char @ o_word index: {i} / o_word char {o_word[i]} | u_word index: {i} / u_word char None')
        # print(f'Total Errors: {self.error_count} / Total Characters: {self.total_char_count}')
        return self.error_count, self.total_char_count