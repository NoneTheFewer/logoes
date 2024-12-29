import re

lisa = open("list.txt", "r")



for line in lisa:
	if line.find("maui college") > -1:
		for ch in line.strip():
			if ord(ch) > 122:
				print(line.strip())
				print(ord(ch))
