import subprocess #for linux commands
import os.path #for check file exist
import urllib #download site
try:
	print("To exit please press Ctrl + C")
	if os.path.exists("source_site.txt"):
		subprocess.call(["rm", "source_site.txt"])
	if os.path.exists("compare_site.txt"):
		subprocess.call(["rm", "compare_site.txt"])
	source_site= input("Please provide source site: ")
	source_site_file = urllib.urlretrieve(source_site, "source_site.txt")
	# while True:


except KeyboardInterrupt:
	pass