import xml.etree.ElementTree as ET

filename = 'data/ttwiki-20200901-pages-articles-multistream.xml'

# tree = ET.parse(filename)
# root = tree.getroot()
#
# tag = root.tag
#
# print(tag)
#
# print(tag.attrib())

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        print(line)