from word_checker import WordChecker
import time

the_word_checker = WordChecker()
all_words = the_word_checker.get_data()
active_word = the_word_checker.words_to_type(all_words)

def run_spell_checker():
    i = 0
    total_error = 0
    total_char_count = 0
    total_typed_words = 0
    start = time.time()
    while i < 10:
        the_word_checker.start_words()
        total_error += the_word_checker.error_count
        total_char_count += the_word_checker.total_char_count
        total_typed_words += the_word_checker.total_words_typed
        i += 1

    print(total_error,  total_char_count)
    total_time = round(time.time()-start, 2)
    time_seconds = total_time / 60
    wpm = total_typed_words / time_seconds
    error_rate = round((total_error / total_char_count) * 100, 2)
    return wpm, error_rate

wpm_er = run_spell_checker()
accuracy = 100 - wpm_er[1]
print(f'WPM: {wpm_er[0]} |\nErrorRate: {wpm_er[1]}% |\nAccuracy: {accuracy}%')