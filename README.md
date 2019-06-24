# MAC-Checker
Used to find MAC Addresses that are **not** on a list.

# Backstory

Some routers have the ablility to send logs that contain when devices request DHCP leases and store their MAC Addresses.
These logs can be received daily, weekly, monthly.
Some routers may give you the ability to create a custom schedule of when you receive these logs. My goal was to 
check through the logs that my router provided for me and to see if there was any *unsavory* devices on my LAN.

# What You Need

The script will require two files: a **master list** of MAC Addresses that are approved to be on your LAN, and
the **log** that your router gives you.

The Master List should be a .txt file that looks like this:
```
AA:AA:AA:AA:AA:AA
BB:BB:BB:BB:BB:BB
CC:CC:CC:CC:CC:CC
```
*Note: My router presents MAC Addresses with colons (XX:XX:XX:XX:XX:XX). Yours might not. You can modify the
regex string to your router's format in the script.*

The log file should just be a .txt file of the output from the router.

Make sure both of these files are in the same directory as the script.

*Note: I named my master list "mac_addresses.txt" and the log file "log.txt". These are the two files the script
is looking for. If you want to name your files something else, just change the names to whatever you want in
the script.*

From there just run the script! It will produce a .txt file with the MAC Addresses of the devices that are not 
on your list.


Zach Sanford<br />
(@zachsanford)
