import subprocess #for linux commands
import os.path #for check file exist
import urllib.request #download site
import time
def download_to_file(link,file_name):
	source_site = urllib.request.urlopen(link)
	subprocess.call(["touch", file_name])
	source_site_byte = source_site.read()
	source_site_str = source_site_byte.decode('utf-8')
	file = open(file_name, "w")
	file.write(source_site_str)
	file.close
def diff_list(source_site_list,compare_site_list):
	if source_site_list != compare_site_list:
		print("Site has been changed")


def main_function():
	try:
		print("To exit please press Ctrl + C")
		try:
			subprocess.call(["rm", "source_site.txt"])
			print("source_site.txt has been deleted")
		except:
			print("source_site.txt no exist")
		try:
			subprocess.call(["rm", "compare_site.txt"])
			print("compare_site.txt has been deleted")
		except:
			print("compare_site.txt no exist")
		# source_site = urllib.request.urlopen('http://rarez.pl')
		# subprocess.call(["touch", "source_site.txt"])
		# source_site_byte = source_site.read()
		# source_site_str = source_site_byte.decode('utf-8')
		# file = open("source_site.txt", "w")
		# file.write(source_site_str)
		# file.close
		download_to_file('http://rarez.pl','source_site.txt')
		while True:
			# compare_site = urllib.request.urlopen('http://rarez.pl')
			# subprocess.call(["touch", "compare_site.txt"])
			# compare_site_byte = compare_site.read()
			# compare_site_str = compare_site_byte.decode('utf-8')
			# file = open("compare_site.txt", "w")
			# file.write(compare_site_str)
			# file.close
			download_to_file('http://rarez.pl','compare_site.txt')
			# time.sleep(10)
			source_site_list = open("source_site.txt").readlines()
			compare_site_list = open("compare_site.txt").readlines()
			diff_list(source_site_list,compare_site_list)

	except KeyboardInterrupt:
		pass
main_function()
