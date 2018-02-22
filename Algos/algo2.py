#Alignement de deux squences
adn1 = "AAAATTTTTTGCCCTTTAA"
adn2 = "AAAAGCCCAA"
inter = []
i,j=0,0
temp=""
while i&j<min(len(adn1),len(adn2)):	
	if adn1[i] == adn2[j]:
		temp+=adn1[i]
	else:
		inter+=[temp]
		temp=""
	i+=1

print inter
