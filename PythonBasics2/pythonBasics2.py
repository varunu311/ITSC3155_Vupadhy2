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
  n = list(str(n))
  mydict = {}
  mydict[3] = mydict[6] = mydict[9] = 0

  for i in n:
    j = int(i)
    if j % 3 == 0 and j != 0:
      mydict[j] = mydict[j] + 1

  max = 0
  idx = 0

  for k, v in mydict.items():
    if v > max:
      max = v
      idx = k

  return idx


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  s = list(s)
  c = 1
  mydict = {}

  for i in range(0, len(s) - 1):
    if (s[i] != s[i + 1]):
      if ((s[i] in mydict) and mydict[s[i]] > c):
        continue
      else:
        mydict[s[i]] = c
        c = 1
    else:
      c = c + 1

  mydict[s[len(s) - 1]] = c

  max = -1
  for k, v in mydict.items():
    if v > max:
      max = v

  ls = []
  for k, v in mydict.items():
    if v == max:
      ls.append(k)

  return ls


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):

  string = str.lower(s)
  string = string.replace(" ","")

  reverse = string[::-1]

  if string == reverse:
    return True

  else:
    return False

