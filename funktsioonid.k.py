from Funktsioonid import*
users=["kristina"]
passwords=["12345"]

while True:
	print("Näita kõike -0,Reg-1,AVt-2,Välja")
pasword = ''.join([random.choice(ls) for x in range(12)])
return psword 
return psword
def paskontroll(psword: str)->bool:
	ls=list(psword)
	for e in ls:
		if e.isdigit(): d=True
		if e.isalpha(): a=True
		if e.isupper(): u=True
		if e.islower():l=True
		if e in list(".,:;!_*-+()/#¤%&"): s=True
	if d==True and a==True and u==True and l==True and s==True:
		t=True
	else:
		t=False


