import tkinter
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
        frame.config(bg=BACKGROUND_COLOR, )
        frame.pack(fill='both', expand=True)
        # attributes we'll need for the object
        self.words_to_type = StringVar()
        self.total_chars_string = StringVar()
        self.total_counts_string = StringVar()
        self.original_words_list = []
        self.user_word_list = []
        self.start_time = ''
        self.char_count = 0
        self.error_count = 0

        # GUI contrrols and labels
        self.start_button = Button(frame, text="Start Typing Test", height=25, width=50,
                                   font=('Arial', 40, 'bold'), command=self.start_typing_test)
        self.typing_label = Label(frame, text='hello', fg='Black', bg=BACKGROUND_COLOR,
                                  textvariable=self.words_to_type, font=TEXT_LABEL_FONT)
        self.user_entry = Entry(frame, width=80, fg='Black', bg='Gray', font=TEXT_LABEL_FONT)
        self.user_entry.bind('<Return>', self.compare_entries)
        self.total_count_label = Label(frame, text='Total Errors', fg='red', bg='White', height=1, font=TEXT_LABEL_FONT,
                                       textvariable=self.total_counts_string)
        self.total_char_label = Label(frame, text='Total Chars', fg='red', bg='White', height=2, font=TEXT_LABEL_FONT_TWO,
                                      textvariable=self.total_chars_string)
        self.start_button.pack(padx=20, pady=20)


    def start_typing_test(self):
        self.start_time = time()
        self.original_word_list = words.words_to_type(all_word_list)
        # Show words you should match
        new_string = ' '.join(self.original_word_list)
        self.words_to_type.set(new_string)
        self.typing_label.pack(pady=5)
        self.user_entry.pack()
        self.user_entry.focus_set()
        self.start_button.pack_forget()

    def compare_entries(self, event):
        user_words = self.user_entry.get().upper().split(' ')
        self.user_entry.delete(0, 'end')
        self.error_count += words.count_errors(self.original_word_list, user_words)[0]
        self.char_count += words.count_errors(self.original_word_list, user_words)[1]
        self.total_counts_string.set('Errors / Total Characters')
        self.total_chars_string.set(f'{self.error_count} / {self.char_count}')
        self.total_count_label.pack()
        self.total_char_label.pack()
        self.next_line()


    def next_line(self):
        self.original_word_list = words.words_to_type(all_word_list)
        new_string = ' '.join(self.original_word_list)
        self.words_to_type.set(new_string)
