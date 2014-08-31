filename='details.csv'

filehandle=open(filename,'a')
name = ''
while name != 'END':
	name = raw_input('Enter your name:')
	enlno = raw_input('Enter Enr. No.:')
	filehandle.write(name+','+enlno+'\n')

filehandle.close()

