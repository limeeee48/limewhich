#!/bin/python3

import os 
import sys
from limelib import limechecksys

class CommandNotFound(Exception):
	pass

class colors:
	Error_Color="\033[1;31m"
	banner_color="\033[1;33m"
	Sucess_Color="\033[1;32m"
	End_Line="\033[0m"


def banner():
	print(f"""{colors.banner_color}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣀⡴⠛⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠬⣷⠄⠀⠀⠀⠀⢰⣆⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⠀⠀⠀⠐⢿⣬⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠧⠀⠀⠀⠀⠀⠀⠀⢤⠀⠀⢠⣤⡀⠀⠙⣆⠀⠀⠀⠀⠙⠀⠀⠀⠀
⠀⠀⣸⡄⠀⠀⠀⢀⡏⠀⠀⣀⡀⠀⠀⠀⠛⠀⠀⠈⣯⠀⠀⢞⣛⣯⡉⠀⠀⠀⣸⢦⣄⡀
⠀⠺⢿⡿⠛⠀⠀⢸⡇⠀⡀⣿⠟⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠉⢉⡏⠁⠀⠈⠛⡾⠋⠀
⠀⢀⠈⠁⠀⠀⢀⣹⡷⣶⠂⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀
⢀⡾⢦⡄⠀⠰⠋⣹⡷⠛⠁⠀⠀⠀⠀⠀⣠⣤⡤⠤⣄⠀⠀⠀⠸⣧⡀⠀⣴⠛⣦⠀⠀⠀
⠈⠻⠟⠁⠀⠀⠘⠋⠻⢶⣤⣀⠀⠀⠀⠾⠡⠸⣇⠀⠀⠀⠀⠀⠀⠈⠳⣆⡿⠀⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠐⠏⠃⠀⠀⠀⠀⠀⠀⠀⠙⣇⣸⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		
	   Author : Lime 
	   {colors.End_Line}""")
first_tree=[]
new_first_tree=[]
def know_system()-> str :
	check_system = limechecksys.sys_know()
	return check_system

def folder_file_check(lista) -> int :
	for one_dir in lista :
		try :
			open(one_dir , "r")
			return(0) 
		except IsADirectoryError : 
			return(1) 

def get_first_tree() -> None :
	get_path = os.getenv("path".upper()).split(":")
	for one_path in get_path :
		#Check Folder Exitsts 
		if os.path.exists(one_path):
			first_tree.append(one_path)

def check_if_folders()->None:
	get_first_tree()
	for check_folder in first_tree :
		if folder_file_check(check_folder):
			new_first_tree.append(check_folder)
					

last_tree=[]
def get_all_files()-> int :
	check_if_folders()
	for oneitem in new_first_tree:
		files = os.listdir(oneitem)	
		for one_file in files :
			last_tree.append(one_file)

def main() ->None :
	get_all_files()
	if len(sys.argv) == 2 or len(sys.argv) > 2  :
		if sys.argv[1] in last_tree :
			print(f"{colors.Sucess_Color}[+] Command: {sys.argv[1]} Found{colors.End_Line}\n")
			exit(0)
		else :
			raise CommandNotFound(f"[-] Command: {sys.argv[1]} Not Found") 
	else:
		print(f"{colors.Error_Color}Error: Tool name cannot by empty!{colors.End_Line}")
		exit(1)
if __name__ == "__main__":
	banner()
	try :
		if know_system() == str("linux"):
			main()
		elif know_system() == str("windows"):
			print("Windows soon . . ")
		else:
			print("Error")
	except CommandNotFound as commanderror :
		print(f"{colors.Error_Color}{commanderror}{colors.End_Line}\n")
		exit(1)
