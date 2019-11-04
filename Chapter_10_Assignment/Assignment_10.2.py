# 10.2 Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)


hour = []
hour_dict = dict()

for line in handle:
    line = line.strip()
    if line.startswith('From '):
        addr = line
        split_addr = addr.split()
        time = split_addr[5]
        hr = time[:2]
        hour.append(hr)
# print(hour)
for hour_count in hour:
    hour_dict[hour_count] = hour_dict.get(hour_count, 0) + 1
# print(hour_dict)
tups = hour_dict.items()
# print(tups)
for k, v in sorted(hour_dict.items()):
    print(k, v)


# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
