all_emails=dict()
final_count=None
final_id=None

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#to find all the ids
for line in handle:
	if line.startswith('From:'):
		word=line.split()
		mail_id=word[1]

		#make the count of ids
		all_emails[mail_id]=all_emails.get(mail_id,0)+1

#to find the maximum count
for ids,count in all_emails.items():
	if final_count is None or final_count<count:
		final_count=count
		final_id=ids

print(final_id, final_count)
