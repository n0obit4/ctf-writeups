#By: n0obit4

def reto(file):
	fuck = []
	a = ""
	caracteres = "<>-[].+"
	with open(file, "r") as ctf:
		ctf = ctf.readline()
		for words in ctf:
			if words in caracteres:
				a += words
	print(a)

if __name__ == '__main__':
	reto("Base_Fuck")
	
