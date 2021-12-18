import dearpygui.dearpygui as dpg
import os, re, csv, hashlib,sys, glob

dpg.create_context()
width, height, channels, data = dpg.load_image("alert.png")
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width, height, data, tag="texture_tag")
width, height, channels, data1 = dpg.load_image("clear.jpeg")
with dpg.texture_registry(show=False):    
    dpg.add_static_texture(width, height, data1, tag="texture_tag1")
def signature(path, name):
        md5_hash = hashlib.md5()
        a_file = open(path, "rb") 
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        file_sign = []
        file_sign.append(digest)
        signatures = []
        with  open("SignatureBD") as file:
                wr = file.read().splitlines()
        signbase = []
        for each in wr:
                items = each.split(' ')
                signbase.append(items)
        for i in signbase:
                print(str(i))
                print(str(file_sign))
                if (i == file_sign):
                        with dpg.window(label="ALERT!!!", pos=(400,150),width = 242, height = 285):
                                dpg.add_text(str(name)+" is a virus!")
                                dpg.add_image("texture_tag")
                else:
                        with dpg.window(label="Result",pos=(400,150),width=300,height=230):
                                dpg.add_text(str(name)+" doesn`t contained in BD")
                                dpg.add_image("texture_tag1")
class file_str:
	def __init__(self, name, size, t_mod):
		self.name = name
		self.size = size
		self.t_mod = t_mod
	def __str__(self):
		with dpg.window(label="File info", width = 200, height = 100):
			dpg.add_text("File full path - " + self.name)
			dpg.add_text("File size - " + str(self.size))
			dpg.add_text("Last modification - " + str(self.t_mod))
def callback(sender, app_data):  
	a = file_str(str(app_data["file_path_name"]),os.path.getsize(app_data["file_path_name"]) , os.path.getmtime(app_data["file_path_name"]))
	signature(a.name,app_data["file_name"])
def search():
	programs = glob.glob("*py")
	programList = []
	modlist = []
	nmodlist = []
	Virus = False
	for p in programs:
                programSize = os.path.getsize(p)
                programMod = os.path.getmtime(p)
                programData = [p, programSize, programMod]
                programList.append(programData)
	with open("fileData") as file:
		filelist = file.read().splitlines()
	originalfilelist = []
	for each in filelist:
		items = each.split(',')
		originalfilelist.append(items)
	for a in programList:
		for b in originalfilelist:
			if (a[0] == b[0]):
				if (int(a[1]) != int(b[1])):
					print(a[1],"\n", b[1])
					modlist.append(a[0])
					Virus = True
				else:
					print("1")
					nmodlist.append(a[0])
	if len(nmodlist) < len(modlist):
		for i in range(len(nmodlist), len(modlist)):
			nmodlist.append("-")
	if len(modlist) < len(nmodlist):
                for i in range(len(modlist), len(nmodlist)):
                        modlist.append("-")

	with dpg.window(label="Result of scanning", pos=(250,200),width=500,height=200):
		with dpg.table(header_row=True):
			dpg.add_table_column(label="Modified files")
			dpg.add_table_column(label="Non modified files")
			len1 = max(len(nmodlist),len(modlist))
			for i in range(0, len1):
				with dpg.table_row():
					for j in range(0, 2):
						if(j==0):
                    					dpg.add_text(str((modlist[i])))
						else:
							dpg.add_text(str(nmodlist[i]))
	if Virus:
		with dpg.window(label="Alert!!!!!", width=242,height=285,pos=(1,150)):
			dpg.add_image("texture_tag")
			dpg.add_text("Your directory maybe infected!!!!!")
with dpg.file_dialog(directory_selector=False, show=False, callback=callback, tag="file_dialog_tag"):
    dpg.add_file_extension(".*")
    dpg.add_file_extension("", color=(150, 255, 150, 255))
    dpg.add_file_extension(".py", color=(0, 255, 0, 255))

with dpg.window(label="VSCAN", width=1000, height=1000) as main_w:
   dpg.add_button(label="Scan File",pos=(250,500),width=500,height=70, callback=lambda: dpg.show_item("file_dialog_tag"))
   dpg.add_button(label="Scan directory",pos=(250,600),width=500,height=70,callback=search)
dpg.set_primary_window(main_w, True)
dpg.create_viewport(title='VSCAN', width=1000, height=1000)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

