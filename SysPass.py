# -*- coding: utf-8 -*-
"""
@author: ssauvageau-
"""
import platform
import GPUtil
from hashlib import blake2b
import linecache

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
def build_sys_uuid():
	uname = platform.uname().system
	mach = platform.uname().machine
	gpu_id = GPUtil.getGPUs()[0].uuid
	
	#This is the string that will be hashed. 
	#Change as necessary for whichever definition of computer hardware you wish
	#to use as a unique identifier.
	comb = uname.encode('ascii') + mach.encode('ascii') + gpu_id.encode('ascii')
	hasher = blake2b()
	hasher.update(comb)
	dig = hasher.hexdigest() + ""
	return [dig[0:32], dig[32:64], dig[64:96], dig[96:128]]
	
def dictSize():
	with open('words_alpha.txt') as f:
		line_count = 0
		for line in f:
			line_count += 1
	return line_count

def pwd_build():
	uuid = build_sys_uuid()
	mod_uuid = []
	pwd_l = []
	for chunk in uuid:
		mod_uuid.append(int(chunk, len(chars)) % dictSize())
	for num in mod_uuid:
		pwd_l.append(linecache.getline('words_alpha.txt', num).strip().capitalize())
	return ''.join(pwd_l)

def main():
	print(pwd_build())
	
if __name__ == '__main__':
	main()