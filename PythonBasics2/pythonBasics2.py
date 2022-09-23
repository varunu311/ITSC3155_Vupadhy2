# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  x = 0
  if n < 3 and n>-3:
    return 0
  else:
    for i in range(0,n):
      if i%3 == 0:
        x = x+1
      else:
        pass

  return x


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):

  last_char = ""
  current_seq_len = 0
  max_seq_len = 0
  max_char = ''

  for c in s:
    if c == last_char:
      current_seq_len += 1
      if current_seq_len > max_seq_len:
        max_seq_len = current_seq_len
        max_char = c
    else:
      current_seq_len = 1
      last_char = c

  return max_char


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):

  string = s.lower
  fliped = string[::-1]
  print (fliped)
  tf = False

  if fliped == string:
    tf = True
    return tf
  else:
    return tf
