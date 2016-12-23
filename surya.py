import requests, threading, time, json, math
url = "http://surya-interview.appspot.com/message"
headers = {'X-Surya-Email-Id': 'latheefvkpadi@gmail.com'}
results = {}
def start(num):
	start = time.time()
	res = requests.get(url, headers=headers)
	requests.post(url, data=json.dumps(res.json()), headers=headers)
	end = time.time()
	results[num] = end - start

for i in range(10):
	to = []
	for j in range(1, 11):
	    t = threading.Thread(target=start, args=((i*10) + j,))
	    to.append(t)
	    t.start()
	for k in to:
		k.join()
to_do = [10, 50, 90, 95, 99]
s = 0
d = {}
for i in range(10):
	for j in range(1, 11):
		s += results[(i*10) + j]
		if (i*10) + j in to_do:
			d[(i*10) + j] = s

mean = sum(results.values())/100

print "#"*20+"  STATISTICS  "+ "#"*20
for i,j in sorted(d.items(), key=lambda x:x[0]):
	print "percetile for %s is %s" %(i, j/i)

print "MEAN is %s" %(mean)
print "STD DEVIATION is %s" %math.sqrt(sum([(i - mean)**2 for i in results.keys()])/100)

