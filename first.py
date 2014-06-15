import os
from shutil import *
from time import *
import datetime

src = os.path.dirname(os.path.realpath(__file__)) + '/new'
des = os.path.dirname(os.path.realpath(__file__)) + '/used'
FORMAT = '%Y%m%d%H%M%S'

while(True):
	for file in os.listdir(src):
		f = open("log.txt","a")
		
		src_file = os.path.join(src, file)
		dst_file = os.path.join(des, file)
		f.write(datetime.datetime.now().strftime(FORMAT))
		log = " moving " + src_file + " to " + dst_file + "\n"
		#print log
		f.write(log)
		move(src_file, dst_file)
		f.close()
	import script1
	sleep(1)
