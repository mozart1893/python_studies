# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of times they appear in the file.
#  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
handle = open(name)
mail_list = []
mail_dict = dict()
highest_mailer = None
highest_mails = None
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        addr = line
        split_addr = addr.split()
        sender = split_addr[1]
        mail_list.append(sender)
for addrs in mail_list:
    mail_dict[addrs] = mail_dict.get(addrs, 0) + 1
for mailer, mails in mail_dict.items():
    if highest_mails is None or mails > highest_mails:
        highest_mailer = mailer
        highest_mails = mails

print(highest_mailer, highest_mails)
# print(mail_list)
# print(mail_dict)


# if len(name) < 1 : name = "mbox-short.txt"


# cwen@iupui.edu 5
