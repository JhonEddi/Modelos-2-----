def factransp (f):
	if f==0:
		return 1
	else:
		return f*factransp(f-1)