# words-per-min-GUI
# GUI Words per Minute Calculator
# Original Code By: David s. Kuhs
# Prject Name: Python GUI WPM Calculator
# v1.0 currently works in text based terminal only timer starts when you start the program
# Road Map to v2.0: GUI interface where user will press start button, timer will start while generating words for the user to type
# v2.0 features Return user score after they have finished the test and display on screen

Working v1.0 features:
Main.py will call the word_check.py function's to start generating words from the english language txt file, 
it will display a list of 10 words at a time for 10 rounds or 100 words total
In the terminal user can start typing their input and hit enter to get their next line of text
word_checker will take original list, and users list  and compare the length if they're are missing words 
it will start at that index and increase the error_count by one for each char for missiing words, 
next it checks that the words being compared are the same index and if they match, do nothing. 
If their is no match it will check to make sure it's the correct index and if YES 
it will go through character by charcter and count errors for typos, extras and missing chars
main.py tracks total errors and characters from the test and than calculates WPM based on timer's eplasped time 
from the first set of words generated, it will display error rate and accuracy with WPM in terminal prompt
