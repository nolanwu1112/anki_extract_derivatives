# -*- coding: utf-8 -*-
""" todo:
#* 1. Build a dict of vocab that needs derivatives
#* 2. Explore the possibility of using data structures
# 3. Explore dictionary.com's web structure
# 4. Extract content with bs4
# 5. Build a dict of vocab with derivative
# 6. Anki import file
"""

import sqlite3
import time
import progressbar
from extract import extracting
# predefined attributes
vocab_list = []
err_log = r"/error_log/log.txt"

# Method: retrieve vocab
def retrVocab(sql_path):
    """ access sql and retrieve a list of vocabulary"""
    with sqlite3.connect(sql_path) as connection:
        c = connection.cursor()
        c.execute("SELECT vocab FROM pho;")
        result = c.fetchall()
        return result


def Main():
    """Main function"""
    dict_der = {}
    # retrieve a list of vocabulary
    # sql_res = retrVocab("./database/vocab.db")
    sql_res = ['glaze', 'abandon']

    for voc in sql_res:
        voc = str(voc)
        try:
            temp_ = extracting(voc)
            dict_der[voc] = temp_
        except:
            dict_der[voc] = None
    for key, value in dict_der.items():
        print(key, dict_der[key])
#     for key, value in dict_der.items():
#         dict_der[key] = extracting(key)
#         print(key, dict_der[key])
    # access dictionary.com and extract content


if __name__ == '__main__':
    Main()
