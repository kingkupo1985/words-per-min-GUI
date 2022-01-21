import random

# Function Gets Data for Words from TXT file
def get_data():
    word_list = []
    with open('english_words copy.txt', mode='r') as f:
        for line in f:
            word = line.strip()
            word_list.append(word)
    return word_list

# Generates 10 random words to a list to be used in typing test
def words_to_type(words):
    word_count = 0
    words_type = []
    while word_count != 10:
        random_word = random.randint(0, len(words) - 1)
        words_type.append(words[random_word])
        word_count += 1
    return words_type


def start_words():
    ### Probably going to be the initialize function
    # Getting Data
    all_word_list = get_data()
    # Creating List
    original_word_list = words_to_type(all_word_list)
    # Show words you should match
    print(' '.join(original_word_list))
    # Get users input to see if they match need to add timer function to calculate WPM and loop for 10 sets of 10 words
    users_original_word_string = input("Please enter the words you see above as quickly and accurately as possible!\n"
                                       "It is case insensitive: ").upper()
    # get users words and split by ' ' to create a list to compare
    users_word_list = [word for word in users_original_word_string.split(' ')]
    return count_errors(original_word_list, users_word_list)

### Function for checking words and getting wrror count
def count_errors(original_list, user_list):
    # Initalize Error counter
    error_count = 0
    total_char_count = 0
    # Iterate through original wordlist
    for word in original_list:
        total_char_count += len(word)
    print(total_char_count)
    if len(original_list) > len(user_list):
        missing_words = len(original_list) - len(user_list)
        print(f'Total missing words: {missing_words}')
        for word in original_list[-missing_words:]:
            print(f"missing word: {word} | word length: {len(word)}")
            for char in word:
                error_count += 1
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
                    error_count += len(o_word) - len(u_word)
                elif len(o_word) < len(u_word):
                    # print(f'line 55: {o_word}, total xtra chars: {(len(o_word) - len(u_word)) * -1}')
                    error_count += len(u_word) - len(o_word)
                # iterate through each character in original word
                for i in range(len(o_word)):
                    try:
                        if o_word[i] == u_word[i]:
                            pass
                            #print(f'Match @ o_word index: {i} / o_word char {o_word[i]} | u_word index: {i} / u_word char {u_word[i]}')
                        else:
                            error_count += 1
                            # print(f'NO Match @ o_word index: {i} / o_word char {o_word[i]} | u_word index: {i} / u_word char {u_word[i]}')
                    except IndexError as err:
                        pass
                            # print(f'Missing Char @ o_word index: {i} / o_word char {o_word[i]} | u_word index: {i} / u_word char None')
    print(f'Total Errors: {error_count} / Total Characters: {total_char_count}')
    return error_count, total_char_count

print(start_words())