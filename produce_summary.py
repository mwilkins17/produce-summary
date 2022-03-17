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


def daily_report():
    day_count = 1
    while day_count < 4:
        the_file = open (f"um-deliveries-day-{day_count}.txt")
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
daily_report()