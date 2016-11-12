class color:
#	
# Part one: To be used as :
# from pylinux-colors import * 
# print color.red + "your-text"
#
	default = '\033[39m'
	black = '\033[30m'
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	blue = '\033[34m'
	magenta = '\033[35m'
	cyan = '\033[36m'
	white = '\033[00m'
#
# Part two: To be used as :
# from pylinux-colors import *
# color.set(green)
#
	def set(colo):
		if colo == "default":
			print default
		elif colo == "black":
			print black
		elif colo == "red":
			print red
		elif colo == "green":
			print green
		elif colo == "yellow":
			print yellow
		elif colo == "blue":
			print blue
		elif colo == "magenta":
			print magenta
		elif colo == "cyan":
			print cyan
		elif colo == "white":
			print white
		else:
			print default
