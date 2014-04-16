import urllib2
import sys

# Instructions on how to use the script in case there's an error.
def usage():
	print "linkdump.py - a simple tool to dump all hyperlinks from an URL.\n"
	print "usage: 'python linkdump.py http://copypastedurl.com/'"

# The fuction responsible for retrieving the href http links from the URL given.
# It basically looks for the beginning of a href link with the tag variable, and the end
# of it determined by the double quotation marks at the end.
# What it is doing is simply getting the position of the first occurrence of the tag variable
# and reading it all the way to the endtag. After having the whole link it writes to a .txt file.
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
# Main procedure of the script where the other procedures are called from, I organized the code this way
# for two reasons, organization and readability.
def main():
	usage()
	dump(str(sys.argv[1]))

main()