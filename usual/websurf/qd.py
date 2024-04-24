log = open("log", 'r')
out = open("queue_depth.txt", 'w'); 

depth = 0
for line in log.readlines():
	if(line.startswith('CPU')):
		break
	split = line.split();
	aa = split[5]
	time = split[3]
#	print aa
	if aa == "D":
		depth = depth+1
		if depth>31 :
			depth = 31
		out.write(time+'\t'+str(depth)+'\n')
		continue
	else:
		depth = depth-1
		if(depth < 0):
			 depth = 0
		out.write(time+'\t'+str(depth)+'\n')
		continue

log.close()
out.close()	
