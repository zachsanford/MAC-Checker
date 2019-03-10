# MAC-Checker
Used to find MAC Addresses that are **not** on a list.

# Backstory

Some routers have the ablility to send the Administrator logs.  These logs can be received daily, weekly, monthly.
Some routers may give you the ability to create a custom schedule of when you receive these logs. My goal was to 
check through the logs that my router provided for me and to see if there was any "*unsavory*" devices on my LAN.

# What You Need

The script will require two files: a **master list** of MAC Addresses that are approved to be on your LAN, and
the **log** that your router gives you.
