#!/usr/bin/python

from lxml import etree
import sys

if len(sys.argv) < 2:
	print("Usage: python3 testXml.py <payload_file>")
	exit(1)

f = open(sys.argv[1],"r")
data = f.read()
f.close()

parser = etree.XMLParser(encoding='utf-8', no_network=False)
tree = etree.fromstring(data.encode('utf-8'), parser=parser)
print("Parsed successfully")


