#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import sys
import codecs     
with codecs.open('idiom.json','r',encoding='utf-8') as data_file:
    x = json.loads(data_file.read())
    with open("text.csv","w", newline='', encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter='\t',
                        quotechar='\n', quoting=csv.QUOTE_MINIMAL)
        # 表头
        # f.writerow(["derivation", "example", "explanation", "pinyin", "word", "abbreviation"])
        f.writerow([str(k) for k,v in x.items() ])
        for x in x :
            # f.writerow([
            #     str(x["derivation"]), str(x["example"]), 
            #     str(x["explanation"]), str(x["pinyin"]), 
            #     str(x["word"]), str(x["abbreviation"])
            #     ])
            f.writerow([str(v) for k,v in x.items() ])