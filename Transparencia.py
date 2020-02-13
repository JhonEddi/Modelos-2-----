def potencia(n,m):
	if m==0:
		return 1;
	if m>=1:
		return n*potencia(n,m-1)

def potenciaNT(n,m):
	potencia=1
	while(m>0):
		potencia=potencia*n
		m=m-1
	return potencia