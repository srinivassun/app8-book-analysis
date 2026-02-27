import re

with open('miracle_in_the_andes.txt','r',encoding="utf-8") as file:
    book = file.read()

def print_findings(findings):
    for finding in findings:
        print('[',finding,']')

#WITH REGULAR EXPRESSIONS TO MATCH THE PATTERNS IN A TEXT FILE

#Single digit pattern 0-9
pattern = re.compile("Chapter [0-9]")
print(re.findall(pattern, book))

#Multi digit pattern fetches Chapter 10 and 11 also
pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book)
print(findings)
print("Number of chapters : ", len(findings))

#Which are the sentences where a word 'love' was used
pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern, book)
#print_findings(findings)

#what are the most used words
pattern = re.compile("[A-Za-z]+")
findings = re.findall(pattern, book.lower())
print(len(findings))
print_findings(findings)