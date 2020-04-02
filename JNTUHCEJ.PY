import requests
from bs4 import BeautifulSoup


fails={}
def get_result(no,dep=0):
	if (no<10):
		no='0'+str(no)
	else:
		no=str(no)
	if (dep==0):
		ht='17JJ1A03'
	else:
		ht='18JJ5A03'
	data={'htno': ht+no,
	'exam': '31dec2019reg',
	'cv': 'AY6GY',
	'course': 'A'}
	headers={'Cookie': "HstCfa3293412=1562255461999; c_ref_3293412=https%3A%2F%2Fwww.google.com%2F; __dtsu=2DE7B66B64201E5D1C7C1C2902FDFC33; HstCmu3293412=1580010951570; __dtsu=6BB6E72D5D1E2064291C7C1C33FCFD02; PHPSESSID=1c363b9ccdb0a6880306b818b40c78fb; __test=b51e86242acbbe99b31c197da109d7c8; HstCnv3293412=4; HstCns3293412=4; HstCla3293412=1581949718547; HstPn3293412=2; HstPt3293412=12",
			  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
			  'X-Requested-With': 'XMLHttpRequest'}
	res=requests.post('http://ebjntuhcej.p4o.net/resultsnew/results2.php',data=data,headers=headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	sub=[]
	#print(res.text)
	details=soup.findAll('strong')
	k=soup.findAll(align='left')
	for i in k:
		sub.append(i.text)
	k=soup.findAll(align='center')
	j=0
	for i in range(len(sub)):
		t=int(k[i*3+2].text)
		if (t==0):
			print(details[0].text,details[1].text,'     ',sub[i])
			if (details[1].text in fails):
				fails[details[1].text].append(sub[i])
			else:
				fails[details[1].text]=[]
				fails[details[1].text].append(sub[i])
	#print(ht+no,':',soup.find(id='sgpa').text)

print('failed details')
for i in range(1,60):
	print(i)
	try:
		get_result(i)
	except Exception:
		pass

for i in range(1,10):
	print(i)
	try:
		get_result(i,1)
	except Exception:
		pass

#print(fails)