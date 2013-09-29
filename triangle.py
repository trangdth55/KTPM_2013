import math
from decimal import Decimal
def tamgiac(a,b):
	return a+b
def detect_triangle(a,b,c):
	if ((type(a) in [float, int, long]) and (type(b) in [float, int, long]) and (type(c) in [float, int, long]) 
		and (a >= 0 and a <= 2**32-1 ) and (b >= 0 and b <= 2**32-1) and (c >= 0 and c <= 2**32-1)):
		if((tamgiac(Decimal(a),Decimal(b)) > Decimal(c) and tamgiac(Decimal(a),Decimal(c)) > Decimal(b) and tamgiac(Decimal(b),Decimal(c)) > Decimal(a))):
			if(a == b) and (b == c):
				return "Tam giac deu"
			elif ((abs(a*a - b*b - c*c) < 10**-9) and (c==b)) or ((abs(c*c - b*b - a*a) < 10**-9) and (a == b)) or ((abs(b*b - c*c - a*a) < 10**-9) and (a==c)):	
				return "Tam giac vuong can"
			elif (((a == b) and ( b!= c)) or ((a == c) and (c != b)) or((b == c) and (c != a))):
				return "Tam giac can"
			elif (math.fabs(c*c - b*b - a*a) < 1e-10) or (math.fabs(b*b - c*c - a*a) < 1e-10) or (math.fabs(a*a - b*b - c*c) < 1e-10):
				return "Tam giac vuong"		
			else: return "Tam giac thuong"
		else: return "Khong phai la tam giac"
	else:
		return "Loi bien dau vao"
