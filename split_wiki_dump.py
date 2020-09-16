import xml.etree.ElementTree as ET
import os

filename = 'data/ttwiki-20200901-pages-articles-multistream.xml'
out_folder = 'data/out/'

kol_files_in_folder = 10000

# tree = ET.parse(filename)
# root = tree.getroot()
#
# tag = root.tag
#
# print(tag)
#
# print(tag.attrib())

number_file = 1
number_folder = 1
page_item = ""
os.mkdir(f"{out_folder}{number_folder}")
with open(filename, 'r') as f:
    for xmlline in f:
        line = xmlline.strip()
        page_item += xmlline
        # print(line)

        if (len(line)>0) and (line in '</page>'):  # конец статьи+
            print(f'Detect new page: {number_file}')

            out_filename = f'{out_folder}{number_folder}/{number_file}.xml'
            print(line)
            with open(out_filename, 'w') as f_out:
                f_out.write(page_item)
            page_item = ''
            number_file += 1

        if number_file > kol_files_in_folder:
            number_file = 1
            number_folder += 1
            os.mkdir(f"{out_folder}{number_folder}")
