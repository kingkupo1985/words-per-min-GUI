from tkinter.ttk import *
from time import time
from tkinter import *
import word_checker

BACKGROUND_COLOR = '#445E78'
TEXT_LABEL_FONT = ('Arial', 20, 'bold')
TEXT_LABEL_FONT_TWO = ('Arial', 48, 'bold')
words = word_checker.WordChecker()
all_word_list = words.get_data()

class WpmGui():
    def __init__(self, master):
        # creating frame
        frame = Frame(master)
        frame.config(bg=BACKGROUND_COLOR)
        frame.grid(row=0, column=0, sticky="NESW")
        master.configure(background='#445E78')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # attributes we'll need for the object
        self.words_to_type = StringVar()
        self.total_chars_string = StringVar()
        self.total_counts_string = StringVar()
        self.error_rate = DoubleVar()
        self.accuracy = DoubleVar()
        self.original_words_list = []
        self.user_word_list = []
        self.start_time = 0
        self.char_count = 0
        self.error_count = 0
        self.wpm = DoubleVar()
        self.total_typed_words = 0
        self.rounds = 0

        # GUI controls and labels
        self.start_button = Button(frame, text="Start Typing Test",
                                   font=('Arial', 30, 'bold'), command=self.start_typing_test, bd=0, height=2,
                                   highlightbackground='black', activebackground='black', bg='black')
        self.typing_label = Label(frame, text='hello', fg='Black', bg='yellow',
                                  textvariable=self.words_to_type, font=TEXT_LABEL_FONT)
        self.user_entry = Entry(frame, width=80, fg='Black', bg='Gray', font=TEXT_LABEL_FONT)
        self.total_count_label = Label(frame, text='Total Errors', fg='red', bg=BACKGROUND_COLOR, height=1, bd=0, font=TEXT_LABEL_FONT,
                                       textvariable=self.total_counts_string)
        self.total_char_label = Label(frame, text='Total Chars', fg='red', bg=BACKGROUND_COLOR, height=2, bd=0, font=TEXT_LABEL_FONT_TWO,
                                      textvariable=self.total_chars_string)

        self.error_rate_label = Label(frame, textvariable=self.error_rate)
        self.accuracy_label = Label(frame, textvariable=self.accuracy)
        self.wpm_label = Label(frame, textvariable=self.wpm)


        self.start_button.grid()

    def start_typing_test(self):
        self.start_time = time()
        self.start_button.grid_remove()
        self.user_entry.bind('<Return>', self.compare_entries)
        self.original_word_list = words.words_to_type(all_word_list)
        # Show words you should match
        new_string = ' '.join(self.original_word_list)
        self.words_to_type.set(new_string)
        self.typing_label.grid()
        self.user_entry.grid(pady=5)
        self.user_entry.focus_set()
        self.total_count_label.grid(pady=5)
        self.total_char_label.grid()

    def compare_entries(self, event):
        user_words = self.user_entry.get().upper().split(' ')
        self.total_typed_words += len(user_words)
        self.user_entry.delete(0, 'end')
        self.error_count += words.count_errors(self.original_word_list, user_words)[0]
        self.char_count += words.count_errors(self.original_word_list, user_words)[1]
        self.total_count_label.config(bg='White')
        self.total_char_label.config(bg='White')
        self.total_counts_string.set('Errors / Total Characters')
        self.total_chars_string.set(f'{self.error_count} / {self.char_count}')
        self.next_line()


    def next_line(self):
        self.rounds += 1
        if self.rounds == 3:
            self.print_final_score()
            self.user_entry.unbind('<Return>')
        else:
            self.original_word_list = words.words_to_type(all_word_list)
            new_string = ' '.join(self.original_word_list)
            self.words_to_type.set(new_string)

    def print_final_score(self):
        print(self.error_count, self.char_count)
        total_time = round(time() - self.start_time, 2)
        time_seconds = total_time / 60
        self.wpm.set(f"WPM: {round((self.total_typed_words / time_seconds), 2)}")
        errors = round((self.error_count / self.char_count) * 100, 2)
        self.error_rate.set(f'Error %: {errors}')
        self.error_rate_label.grid()
        self.accuracy.set(f'Accuracy %: {100 - errors}')
        self.accuracy_label.grid()
        self.wpm_label.grid()
        print(self.wpm)


