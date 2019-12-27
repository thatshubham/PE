#saving phone and email IDs
import re, pyperclip

#REGEX for Phone
phoneregex = re.compile(r'''
((\d\d\d) | (\(\d\d\d\)))?          #First three digits
(\s|-)                              #space number 1
\d\d\d                              #next three digits
-                                   #space number 2
\d\d\d\d                            #last four digits
(((ext(\.)?\s)|x) (\d{2,5}))?          #extension number part

''', re.VERBOSE)


#Create REGEX for EMAIL
emailregex = re.compile(r'''

[a-zA-Z0-9._+]+ #something._1@something._1.com
@
[a-zA-Z0-9._+]+ ''', re.VERBOSE)

#Access copied text from clipboard
text = pyperclip.paste()

#Search for email and phone numbers

phonenumber = phoneregex.findall(text)
EmailID = emailregex.findall(text)

#copy extracted content to clipboard
print('Phone numbers \n' +str(phonenumber))
print('Email IDs \n' +str(EmailID))
