#7.1
ch=raw_input("ch = ")
n=input("n = ")
print ch[:n]
#7.2
if n<len(ch):
	print ch[len(ch)-n:]
else:
	print ch
#7.3
choix = input("choix(1 pour 1 er cas 0 pour 2eme) = ")
if choix:
	print ch[:n]
else:
	if n<len(ch):
		print ch[len(ch)-n:]
	else:
		print ch
