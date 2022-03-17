# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

from dataclasses import dataclass
from webbrowser import get
import os



# def get_day_count():
#     for file in os.listdir():
#         day_count = []
#         if ".txt" in file:
#             file_tokens = file.split("-")
#             elements_of_file_tokens = file_tokens[3].split(".")
            
#             day_count += elements_of_file_tokens[0]
#             print("day count is:", day_count)
#     return day_count
# get_day_count()
# print(os.listdir())



day_count = 1
def print_daily_report():
    """determines"""
    while day_count < 4:
        the_file = open (f"um-deliveries-day-{day_count}.txt")  #opens the file according to the day count, starting at 1
        for line in the_file:
            line = line.rstrip()
            # print(line)
            words = line.split('|')
            # print(words)

            melon = words[0]
            count = words [1]
            amount = words[2]

            print(f"Day {day_count}: Delivered {count} {melon}s for a total of ${amount}")
        day_count += 1
        the_file.close()
print_daily_report()
