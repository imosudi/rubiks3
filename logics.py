from flask import session, flash
from forms import rubikForm, rubikFormM

class rubikOperation(object):
	"""docstring for rubikOperation"""
	'''def __init__(self, arg):
					super(rubikOperation, self).__init__()
					self.arg = arg'''
	#n = int(input('Give N for nXnXn Rubik\'s cube: '))
	def inputNbyNbyN(self):
		form = rubikForm()
		formM = rubikFormM()
		m = session.get('m')
		#m = formM.m.data
		formM.m.data = ''
		n = session.get('n')
		n = form.n.data
		if m == None:
			m = 0
			n = n
			return n
		else:
			n = m
			return n
		#n = int(n)
		#n = abs(n)
		#return n
		"""if n > 1 and n < 15:
									return n
								elif n > 1:
									flash ('This application will not process that work load. Kindly Provide n more than 1 for nXnXn Rubik\'s Cube ')
									return 3
								else:
									flash ('Provide n more than 1 for nXnXn Rubik\'s Cube ')
									return 3"""
		pass

	def numCubelets(self):
		n = self.inputNbyNbyN()
		if n < 3 or n > 15:
			return 3**3
		else:
			return n**3
		pass

	def nM(self):
		n = self.inputNbyNbyN()
		if n < 3:
			m = 1
			return m
			#return None
		else:
			m = n - 2
			return m
		pass

	def numFacesCubelets(self):
		n = self.inputNbyNbyN()
		m = self.nM()
		#facesCubelets = 6*num*num - 12*num + 8
		if n < 3:
			facesCubelets = 26
			return facesCubelets
		else:
			facesCubelets =  n ** 3 - m ** 3
			return facesCubelets
		pass

	def hiddenCubelets(self):
		n = self.inputNbyNbyN()
		if n < 3:
			hidden = 1
			return hidden
		else:
			m = n -2
			hidden = m ** 3
			return hidden
		pass