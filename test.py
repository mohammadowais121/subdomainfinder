import requests
from bs4 import BeautifulSoup



domain = input("Enter the domain (like 'example.com'): ")

newdomain = "http://web.archive.org/cdx/search/cdx?url="+"*."+domain+"/*&output=text&fl=original&collapse=urlkey"
print("[[" + "+" *25 + "   Finding subdomains and new endpoints   " + "+" *25+ "]]")
print()

parse = requests.get(newdomain).text
html = BeautifulSoup(parse, 'lxml')
endpoints = html.find('p').text
print(endpoints)
print()
print()
print()
print("Do you also want to write this to a file? Type 'yes' or 'no'")
con = input()
if con == "yes":
	with open('NewSub.txt', 'a') as w:
		w.write(endpoints)
	print("Process Done, please check NewSub.txt file.")

else:
	print("Process Done")