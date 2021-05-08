def checking(self,v):
	if v == 1:
		return self.lineEdit.setText("Type atleast a value after modulus sign")
	else:
		return self.lineEdit.setText("Precedence Unidentified! USE SAME OPERATOR")