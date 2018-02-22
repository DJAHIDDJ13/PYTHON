#dot plot
adn1 = "ACTCGAGCTATCG"
adn2 = "ACTATGAGATATG"
intersections = []
for i in range(len(adn1)):
	intersections+=[[]]
for i in range(len(adn1)):
	for j in range(len(adn1)):
		intersections[j] += [1] if adn1[i]==adn2[j] else [0]
for i in range(len(adn1)):
	print intersections[i]
