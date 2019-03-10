#!/usr/bin/python3

import re

# Create two lists to hold MAC Addresses from
# the two files.

macList = []
logList = []

# Create a list to hold MAC Addresses that are
# NOT a match between the previous two lists.

final = []

# Create the Regex string that searches for
# MAC Addresses.

regStr = re.compile(u'(?:[0-9a-fA-F]:?){12}', re.UNICODE)

# Import the master MAC Address file to
# refer against and place each address into
# the macList list.

with open("mac_addresses.txt", "r") as file1:
    for w in file1:
        col = w.strip().split()
        for z in col:
            macList.append(z.rstrip('\n')) # .rstrip() will remove the newline.

# Import the log.txt file and extract all of
# the MAC Addresses using the Regex variable.

# NOTE: You cannot use the with open() method
# that was used above. You have to save the
# text in the file as a string variable. So
# you have to use the method below.

file2 = open("log.txt").read()
for match in regStr.findall(file2):
    logList.append(match)

# Loop through the logList and check to see if
# the element is a match in your macList.

for b in logList:

    # If it is NOT a match then check to see if
    # it exists in the final list.
    
    if b not in macList:

        # If it does NOT already exist then append
        # it to the final list.
        
        if b not in final:
            final.append(b)
            
"""
# Print out the final list to show what MAC
# Addresses were NOT a match in the master
# file.
"""

# CLI

# Loop through the final list and print it out.

for c in final:
    print(c)

# GUI

# Create the output file with header.

file3 = open("mismatched_macs.txt", "w")
file3.write("These are the MAC Addresses of devices that " +
            "are not recognized on your LAN!!\n\n")

# Loop through the final list and write it to the file.

for d in final:
    file3.write(d + '\n')

# Close the file

file3.close()
    
