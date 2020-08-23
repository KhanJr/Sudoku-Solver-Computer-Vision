def order(ar):
	ar1=[[0,0],[0,0],[0,0],[0,0]]
	max=0
	ymax=0
	min=99999
	for i in range (len(ar)):
		if (ar[i][0][0]+ar[i][0][1])>max:
			max=ar[i][0][0]+ar[i][0][1]
			ar1[2][0]=ar[i][0][0]
			ar1[2][1]=ar[i][0][1]
		if (ar[i][0][0]+ar[i][0][1])<min:
			min=ar[i][0][0]+ar[i][0][1]
			ar1[0][0]=ar[i][0][0]
			ar1[0][1]=ar[i][0][1]
	
	for i in range (len(ar)):
		if (ar[i][0][0]+ar[i][0][1])<max and (ar[i][0][0]+ar[i][0][1])>min and ar[i][0][1]>ymax:
			ar1[1][0]=ar[i][0][0]
			ar1[1][1]=ar[i][0][1]
			ymax=ar[i][0][1]
	for i in range (len(ar)):
		if (ar[i][0][0]+ar[i][0][1])<max and (ar[i][0][0]+ar[i][0][1])>min and ar[i][0][1]<ymax:
			ar1[3][0]=ar[i][0][0]
			ar1[3][1]=ar[i][0][1]
	return ar1

