#!/usr/bin/env python

# ---------------------------------------------------------------
#This reducer code will input a line of text and 
#    output <word, total-count>
# ---------------------------------------------------------------
import sys

last_key      = None              #initialize these variables
running_total = 0
has_abc = False

# -----------------------------------
# Loop thru file
#  --------------------------------
for input_line in sys.stdin:
    input_line = input_line.strip()

    # --------------------------------
    # Get Next Word    # --------------------------------
    this_key, value = input_line.split("\t", 1)  #the Hadoop default is tab separates key value
                          #the split command returns a list of strings, in this case into 2 variables
             #int() will convert a string to integer (this program does no error checking)
 
    if last_key != this_key:
        if has_abc:
          print( "{0}\t{1}".format(last_key, running_total) )
        running_total = 0 
        last_key = this_key
        has_abc = False

    if value == 'ABC':
        has_abc = True
    elif value.isdigit():
        running_total += int(value)


if  has_abc:
    print( "{0}\t{1}".format(last_key, running_total)) 
