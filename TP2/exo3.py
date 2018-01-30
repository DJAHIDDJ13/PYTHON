ADN=raw_input("Entrer l'adn: ").upper()
for c in 'AGTC':
	print 'Pourcentage de '+c+' est:',(100.0*ADN.count(c)/len(ADN))
print 'Pourtencage de caracteres inconnus: ',sum([100.0*(i not in 'AGTC')/len(ADN) for i in ADN])
