# Code by Raja Shah
import matplotlib.pyplot as plt
import math

# Extract data pnts from the file and place in 2D list P
P=[[]]
del(P[0])
with open ('iris_dataset.txt') as myfile:
    for line in myfile:
        raw=[line[0:3], line[4:7]]
        raw=list(map(float,raw))
        P.append(raw)

# function to calculate Manhatten distance
def findDistance(s1,s2):
	return abs(s1[0]-s2[0])+abs(s1[1]-s2[1])

# function to find new Median
def findNewMedian(clust):
    new_mean=[]
    s0=0
    s1=0
    for row in clust:
        s0=s0+row[0]
        s1=s1+row[1]
    
    new_mean.append(s0/len(clust))
    new_mean.append(s1/len(clust))
    d=[]
    for row in clust:
    	d.append(findDistance(new_mean, row))
    # Nearest to the mean is the new Median
    return clust[d.index(min(d))]
    

clust1=[]      
clust2=[]
clust3=[]

T=P[:]

m1=T[0]
m2=T[1]
m3=T[2]

count=0
while True:
	clust1.clear()
	clust2.clear()
	clust3.clear()
	count=count+1
	for row in T:
		t=[]
		t.append(findDistance(m1, row))
		t.append(findDistance(m2, row))
		t.append(findDistance(m3, row))

		x = t.index(min(t))
		if(x == 0):
			clust1.append(row)
		elif(x==1):
			clust2.append(row)
		elif(x==2):
			clust3.append(row)

	newMed1 = findNewMedian(clust1)
	newMed2 = findNewMedian(clust2)
	newMed3 = findNewMedian(clust3)

	
	if(m1==newMed1 and m2==newMed2 and m3==newMed3):
		print("Data Clustered in {} iteration".format(count))
		break

	m1=newMed1
	m2=newMed2
	m3=newMed3




###############################################################
# Plot the Graph
x1=[]
x2=[]
for row in clust1:
    x1.append(row[0])
for row in clust1:
    x2.append(row[1])
plt.scatter(x1,x2,marker="v", s=23,c="b",)
plt.scatter(m1[0],m1[1],marker="o", s=32,c="b", label='Mean1')

x1=[]
x2=[]
for row in clust2:
    x1.append(row[0])
for row in clust2:
    x2.append(row[1])
plt.scatter(x1,x2,marker="*", c="g", s=25,)
plt.scatter(m2[0],m2[1],marker="o", s=30, c="g", label="mean2")

x1=[]
x2=[]
for row in clust3:
    x1.append(row[0])
for row in clust3:
    x2.append(row[1])
plt.scatter(x1,x2,marker=".", s=25, c="r", )
plt.scatter(m3[0],m3[1],marker="o", s=30, c="r", label="mean3")

# plt.legend(loc=0)
plt.show()
##################################
