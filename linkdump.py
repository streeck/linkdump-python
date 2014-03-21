import urllib2
import sys


def usage():
	print "linkdump.py - a simple tool to dump all hyperlinks from an URL."
	print ""
	print "usage: 'python linkdump.py http://copypastedurl.com/'"


def dump(url):
	page = urllib2.urlopen(url)
	text = page.read().split("</a>")
	tag = "href=\"http"
	endtag = "\""
	file = open("log.txt", "wb")
	for item in text:
		if tag in item:
			try:
			 	ind = item.index(tag)
				item = item[ind + (len(tag) - 4):]
				end = item.index(endtag)
			except: pass
			else:
				file.write(item[:end] + "\n")

def main():
	usage()
	dump(str(sys.argv[1]))

main()