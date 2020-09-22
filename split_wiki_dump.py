'''
    разделение дампа вики на отдельные статьи.
'''
import os
import argparse


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
    parser = argparse.ArgumentParser(description='Split dump wiki on many article.')
    parser.add_argument('filename', type=str, help='path to file dump wiki')
    parser.add_argument('--out_folder', default='data/out/', type=str,
                        help='output folder(default: data/out/)')
    parser.add_argument('--kol_files_in_folder', type=int, default=10000,
                        help='count article in folder (default: 10000)')
    args = parser.parse_args()

    split_wiki(input_filename=args.filename, out_folder=args.out_folder,
               kol_files_in_folder=args.kol_files_in_folder)
