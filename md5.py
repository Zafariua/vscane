import hashlib, sys, glob, csv, re, os
def HashFile():
        p = "virus.py"
        programList = []
        md5_hash = hashlib.md5()
        a_file = open(p, "rb") 
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        programdata = [digest]
        programList.append(programdata)
        return programList
def WriteFileData(programs):
        with open("SignatureBD","w") as file:
                wr = csv.writer(file)
                wr.writerows(programs) 
WriteFileData(HashFile())# Начало вируса

