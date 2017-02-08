import subprocess #for linux commands
import urllib.request #download site
import time
import sys
import smtplib
def send_email(email,password):
	message = 'Subject: {}\n\n{}'.format('SITE HAS BEEN CHANGED', "SITE HAS BEEN CHANGED")
	mail = smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login(email,password)
	mail.sendmail(email,'damian.kuter@gmail.com', message)
	mail.close()

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
		send_email('developer.messenger@gmail.com','***********')
		subprocess.Popen(['notify-send', 'SITE HAS BEEN CHANGED'])
		sys.exit(0) #Close program if site changed


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
		download_to_file('http://rarez.pl','source_site.txt')
		while True:
			download_to_file('http://rarez.pl','compare_site.txt')
			source_site_list = open("source_site.txt").readlines()
			compare_site_list = open("compare_site.txt").readlines()
			diff_list(source_site_list,compare_site_list)
			time.sleep(10)

	except KeyboardInterrupt:
		pass
if __name__ == "__main__":
	main_function()
