'''
    разделение дампа вики на отдельные статьи.
'''
import os


def split_wiki(input_filename, out_folder='data/out/', kol_files_in_folder=10000):
    """
        :param input_filename: путь до дампа википедии (формат xml)
        :param out_folder: путь куда сохраняются статьи выделенные из дампа
        :param kol_files_in_folder: количество статей в папке
        :return: True, если все прошло хорошо
    """
    number_file = 1
    number_folder = 1
    page_item = ''
    os.mkdir(f"{out_folder}{number_folder}")
    with open(input_filename, 'r') as f:
        for xmlline in f:
            line = xmlline.strip()
            page_item += xmlline

            if (len(line) > 0) and (line in '</page>'):  # конец статьи
                print(f'Detect new article: {number_file}')

                out_filename = f'{out_folder}{number_folder}/{number_file}.xml'
                # print(line)
                with open(out_filename, 'w') as f_out:
                    f_out.write(page_item)
                page_item = ''
                number_file += 1

            if number_file > kol_files_in_folder:
                number_file = 1
                number_folder += 1
                os.mkdir(f"{out_folder}{number_folder}")
    return True


if __name__ == '__main__':
    filename = 'data/ttwiki-20200901-pages-articles-multistream.xml'
    split_wiki(filename)
