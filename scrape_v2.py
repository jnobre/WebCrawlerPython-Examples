
import re, urllib

textfile = file('depth_1.txt','wt')
print "Enter the URL you Wish tto crawl.."
print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
myurl = input("@> ")
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
	print i 
	for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
		print ee
		textfile.write(ee+'\n')
textfile.close()

