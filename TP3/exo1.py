import sys
s1 = "AGATAGA"
s2 = "AGTTG"
a = []
#init
for i in range(len(s2) + 1):
	a += [[]]
	for j in range(len(s1) + 1):
		a[i] += [0]
for i in range(len(s2) + 1):
	a[i][0] = -1*i
for i in range(len(s1) + 1):
	a[0][i] = -1*i
#calcul
for i in range(1,len(s2)+1):
	for j in range(1, len(s1)+1):
		a[i][j] = max(a[i-1][j]-1, a[i][j-1]-1, a[i-1][j-1]+1 if s1[j-1]==s2[i-1]else a[i-1][j-1]-1)
x = len(s1)
y = len(s2)
s1a = ""
s2a = ""
while x>=0 and y>=0:
	if y>0:
		r = a[y-1][x]-1
	else:
		r = -100
	if x>0 and y>0:
		m = a[y-1][x-1]+(-1 if s1[x-1]!=s2[y-1] else 1)
	else:
		m = -1111
	if x>0:
		b = a[y][x-1]-1
	else:
		b=-100
	if a[y][x] == r:
		s1a = "-" + s2a	
		s2a = s2[y-1] + s2a
		y-=1
	elif a[y][x] == m:
		s1a = s1[x-1] + s1a
		s2a = s2[y-1] + s2a
		x-=1
		y-=1
	else:
		s1a = s1[x-1] + s1a
		s2a = "-" + s2a
		x-=1

#affichage
for i in range(len(s2)+1):
	for j in range(len(s1) + 1):
		sys.stdout.write("%3d"%a[i][j])
	print
print s1a[1:]
print s2a[1:]
