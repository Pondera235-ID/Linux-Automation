#!/usr/bin/python3
##################################################
#       Made with love by : Amadeus Pondera      #
#   This code is for educational purposes only,  #
#   and should not be used for any other reason. #
##################################################

import subprocess

f = open("/usr/share/wordlists/rockyou.txt", "r")
for i in f:
	try:
		# Kode perulangan yang mungkin menghasilkan error
		# ...
		pw = i
		cmd= 'openssl enc -d -a -AES-256-CBC -in drupal.txt.enc -k '+pw
		output = subprocess.getoutput(cmd)
		print('passwod =', pw)
		print('==============================================')
		print(output)
		# Jika tidak terdapat error, keluar dari perulangan
		break
	except Exception:
		# Jika terdapat error, lanjutkan perulangan ke iterasi selanjutnya
		continue


'''
import re
import os


f = open("/usr/share/seclists/Passwords/xato-net-10-million-passwords-1000000.txt", "r")
for i in f:
	#print(i)
	pw= i
	cmd = 'openssl enc -d -a -AES-256-CBC -in drupal.txt.enc -k '+pw
	#cmd = cmd
	output = os.system(cmd)
	os.system('clear')
	#print(output) 
	if output == 0:
		print('password =' + pw)
		print('=====================================================')
		print(os.system(cmd))
		break


output = str(os.system('openssl enc -d -a -AES-256-CBC -in drupal.txt.enc -k friends'))
os.system("clear")
print(type(output))
if re.search('256', output):
	print('next', output)
else:
	print('stop', output)
'''