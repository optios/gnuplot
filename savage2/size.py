log = open("log", 'r')
out = open("iosize_log.txt", 'w'); 

size = 0
for line in log.readlines():
	if(line.startswith('CPU')):
		break
	split = line.split();
	aa = split[5]
	bb = split[9]
	time = split[3]
#	print bb
	if aa == "D":
		size = size + int(bb)
		out.write(time+'\t'+str(size*512)+'\n')
		continue
	else:
		# write KB
		size = size - int(bb)
		out.write(time+'\t'+str(size*512)+'\n')
		continue

log.close()
out.close()	
