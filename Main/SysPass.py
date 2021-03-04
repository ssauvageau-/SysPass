# -*- coding: utf-8 -*-
"""
@author: ssauvageau-
"""
import platform
import GPUtil
from hashlib import blake2b
import linecache

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
# Arbitrarily 'builds' a unique text string for the system in question, then hashes it.
def build_sys_uuid(use = ""):
	uname = platform.uname().system
	mach = platform.uname().machine
	gpu_id = GPUtil.getGPUs()[0].uuid
	
	# This is the string that will be hashed. 
	# Change as necessary for whichever definition of computer hardware you wish to use as a unique identifier.
	if not use:
		comb = uname.encode('ascii') + mach.encode('ascii') + gpu_id.encode('ascii')
	else:
		comb = use[:int(len(use)/2)].encode('ascii') + uname.encode('ascii') + mach.encode('ascii') + gpu_id.encode('ascii') + use[int(len(use)/2):].encode('ascii')
	hasher = blake2b()
	hasher.update(comb)
	dig = hasher.hexdigest() + ""
	return [dig[0:32], dig[32:64], dig[64:96], dig[96:128]]
	
# Utility code for pwd_build(). Obtains the length of the password file.
def dictSize():
	with open('words_alpha.txt') as f:
		line_count = 0
		for line in f:
			line_count += 1
	return line_count

# Builds a password out of a hash. See https://xkcd.com/936/ for the rationale.
def pwd_build(use = ""):
	uuid = build_sys_uuid(use)
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