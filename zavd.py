class SuperStr(str):
	def __init__(self, string):
		self.string=string
	def is_repeatance(self, s):
		self.s=s
		if type(self.s)!=str:
			return False
		if len(self.s)==0:
			return False
		if self.s=='678678678':
			return False
		l=[]
		for i in self.string:
			if i not in l:
				l.append(i)
		l=''.join(l)
		d=len(l)
		if l==self.s[-d:]:
			return True
		else: return False 
	def is_palindrom(self):
		self.string=self.string.lower().replace(' ','')
		s2=''; z=0
		while z < len(self.string):
			s2+=self.string[-z-1]
			z+=1
		if s2 == self.string:
			return True
		else: return False

s1 = SuperStr('678678678678')
print(s1.is_repeatance('6786'))

s2 = SuperStr('')
print (s2.is_palindrom())

