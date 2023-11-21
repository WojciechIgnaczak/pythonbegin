import re
txt = "Dopasowuje nie poznieycję, która nie jest nranicą nie słowa."
x = re.findall("nie",txt,1)
print(x)

x =re.split("\s",txt)
print(x)

x =re.sub("\s","WOW",txt)
print(x)


x =re.findall(r'\bnie\b',txt)
print(x)

x =re.findall(r'[\w]',txt)
print(x)

x =re.findall(r'[\w]+',txt)
print(x)

x =re.findall(r'[\w\.]+',txt)
print(x)

mail= "jakub.chmielak@pw.edu.pl"
#x =re.split("@",mail)
x=re.match("^[\w\.]+@[\w\.]+",mail)
print(x)
print(bool(x))

txt1= "Rok 2023 bedzie lepszy."
x= re.sub("\d","X", txt1)
print(x)

x= re.findall(r"\b[n]\w+", txt)
print(x)

kot= "Nasz kot ma 6 lat i waży 4kg."
x=re.findall(r"\d+",kot)
print(x)

x= re.search( r"^nasz",kot, re.IGNORECASE)
print(x)

nr = "Mój numer telefonu to 623-456-789."
#tel =re.search(r"\d{3}-\d{3}-\d{3}",nr)
tel = re.search(r"\b[4-8][0-9]{2}-\d{3}-\d{3}", nr)
print(tel)
domeny="Odwiedz https://www.example.com i http://www.anotherexample.org"
domain_names= re.findall(r'https?://www\.(\w+)',domeny)
print(domain_names)