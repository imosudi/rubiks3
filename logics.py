from flask import session
#import forms
from forms import rubikForm, rubikFormM

class rubikOperation(object):
	#n = int(input('Give N for nXnXn Rubik\'s cube: '))
	def inputNbyNbyN(self):
		#form = forms.rubikForm()
                form = rubikForm()
		#formM = forms.rubikFormM()
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
                pass

	def numCubelets(self):
		n = self.inputNbyNbyN()
		if n < 3 or n > 25:
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
