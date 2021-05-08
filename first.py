from re import *
def func(first,sec,c):
	r = 0
	f = 0
	while sec:
		if findall("[/]",sec):
			sec1 = int(sec[0:sec.find('/')])
			sec2 = sec.replace(str(sec1) + '/',"") 
		elif findall("[x]",sec):				   
			sec1 = int(sec[0:sec.find('x')])       
			sec2 = sec.replace(str(sec1) + 'x',"") 
		elif findall("[\-]",sec):
			sec1 = int(sec[0:sec.find('-')])
			sec2 = sec.replace(str(sec1) + '-',"")
		elif findall("[+]",sec):
			sec1 = int(sec[0:sec.find('+')])
			sec2 = sec.replace(str(sec1) + '+',"")
		else :
			sec1 = int(sec)


		if c == "+":
			
			if f == 0 :
				r = first + sec1
				f = 1
			else:
				r = r + sec1
		elif c == "-":
			if f == 0 :
				if first <= sec1:
					return "Not divided"
				else:
					r = first - sec1
					f = 1
			else:
				if r <= sec1:
					return "Not divided"
				else:
					r = r - sec1
		elif c == "x":
			if f == 0 :
				r = first * sec1
				f = 1
			else:
				r = r * sec1
		elif c == "/" or c == "\\":
			if f == 0 :
				if first == 0:
					return "Invalid Division"
				elif sec1 == 0:
					return "Invalid Division"
				else:
					r = first / sec1
					f = 1
			else:
				if r == 0:
					return "Invalid Division"
				elif sec1 == 0:
					return "Invalid Division"
				else :
					r = r / sec1


		if findall("[/]",sec):
			sec = sec2
		elif findall("[x]",sec):
			sec = sec2
		elif findall("[+]",sec):
			sec = sec2
		elif findall("[-]",sec):
			sec = sec2
		else :
			break
	
	return r
