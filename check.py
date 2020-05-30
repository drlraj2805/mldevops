programfile = open('/home/divya/mlopstask/cnncode.py','r')	
code = programfile.read()					

if 'keras' or 'tensorflow' in code:		
	if 'Conv2D' or 'MaxPooling2D' in code:				
		print('CNN code')
	else:
		print('code is not of CNN')
else:
	print('code is not of Deep Learning')
