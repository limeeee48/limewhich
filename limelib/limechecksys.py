from pathlib import Path

#empty_list=[]
linux_files_list=[
	"/etc/os-release",


]
windows_files_list=[
	"C:\\Windows\\System32\\drivers\\etc\\hosts",
]

def check_linux()->int:
	for folders in linux_files_list:
		try :
			with open(folders , "r") as linux_folders:
				return 0  
		except PermissionError :
			return 0 
		except FileNotFoundError :
			return 1 

def check_windows()->int:
	for folders in windows_files_list:
		try :
			with open(folders , "r") as windows_folders:
				return 0  
		except PermissionError :
			return 0 
		except FileNotFoundError :
			return 1 

def sys_know()-> str:
	linux_check = check_linux()
	windows_check = check_windows()
	if windows_check == int(0) :
		return("windows")
	elif linux_check == int(0):
		return("linux")
	else :
		return("unknown")
