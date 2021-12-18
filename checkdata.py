import sys, glob, csv, re, os

def GetFile():
	programs = glob.glob("*py")
	programList = []
	for p in programs:
		programSize = os.path.getsize(p)
		programMod = os.path.getmtime(p)
		programData = [p, programSize, programMod]
		programList.append(programData)
	return programList
def WriteFileData(programs):
	with open("fileData","w") as file:
		wr = csv.writer(file)
		wr.writerows(programs) 
WriteFileData(GetFile())
