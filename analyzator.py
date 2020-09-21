"""
 анализатор текста и создание инвертированного индекса

источник вдохновения: https://habr.com/ru/post/519024/

Ядром FTS является структура данных, которая называется инвертированный индекс.
Он связывает каждое слово с документами, содержащими это слово.

Анализатор текста:

            <raw text> -> <tokenizer> -> <filters> -> <tokens>

1. <tokenizer>  - преобразование текста в список токенов (разбивает текст на гарницах слов и удаление знаков препинания.

2. <filters>    - возможно потребуется дополнительная нормализация данных:
    а. удаление общеупотребительных слов (таких например как a, I, the, таким образом заводим список стоп-слов)
    б. стемминг - из-за грамматических правил в документах встречаются разные формы слов.
                    стемминг сводит их к основной форме

Построение инвертированного индекса - думаю что подойдет словарь, где ключом будет токен (строка),
а значением - список идентификаторов документов

"""

from collections import OrderedDict

"""
инвертированный индекс
 ключ - строка
 значение индекс - массив строк, вида: номер папки, номер файла, номер строки в тексте
"""
invert_index = OrderedDict()


def tokinizer(raw_text):
    """
    преобразование текста в список токенов (разбивает текст на гарницах слов и удаление знаков препинания
    :param raw_text: сырой текст
    :return: возвращает список токенов в тексте text
    """
    result_tokens = None
    return result_tokens


def low_case_filter(tokens):
    """
    приведение токенов к lowcase
    :param tokens:
    :return: возвращает список токенов приведенных к lowcase
    """
    result_tokens = tokens
    return result_tokens


def stop_word_filter(tokens):
    """
    удаление общеупотребительных слов (таких например как a, I, the, таким образом заводим список стоп-слов)
    :param tokens:
    :return: возвраащает список токенов без стоп слов
    """
    result_tokens = tokens
    return result_tokens


def stemmer_filter(tokens):
    """
    из-за грамматических правил в документах встречаются разные формы слов. стемминг сводит их к основной форме
    :param tokens:
    :return: возвращет список токенов приведенных к основной форме
    """
    result_tokens = tokens
    return result_tokens


def analyze(raw_text):
    """
    Анализатор текста
    :param raw_text:
    :return:
    """
    tokens = tokinizer(raw_text)
    tokens = low_case_filter(tokens)
    tokens = stop_word_filter(tokens)
    tokens = stemmer_filter(tokens)
    return tokens


if __name__ == '__main__':
    raw_text=""
    ttokens = analyze(raw_text)
    print(ttokens)