class Substitute:
	def getValue(self, key, code):
		tempdict = {}
		j = 0
		a = []
		for i in key:
			j = j + 1
			if j != 10:
				tempdict[i] = j
			else:
				tempdict[i] = 0

		for i in code:
			if i not in key:
				continue
			else:
				a.append(tempdict[i])
				j = j + 1

		num = int(''.join(map(str,a)))

		return num
