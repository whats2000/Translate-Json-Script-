import os
from typing import TextIO

import googletrans
import json


def translate_text(srcLang, destLang, txt):
    t = googletrans.Translator()

    result = t.translate(txt,
                         src=srcLang,
                         dest=destLang
                         )
    return result.text


# main
out = {}

while True:
    lang = input('輸入目標語言 : ')
    if lang in googletrans.LANGUAGES:
        break
    else:
        print('不存在該語言，請重新輸入')

for inputFileName in os.listdir(os.getcwd() + '/InputLang'):

    print(inputFileName)

    if not inputFileName.endswith('.json'):
        continue

    with open(os.getcwd()
                + '/InputLang/'
                + inputFileName,
              mode='r',
              encoding='utf8'
              ) as textJson:
        textJsonData = json.load(textJson)

    for it in textJsonData:
        print(it)
        translateText = translate_text('auto', lang, textJsonData[it])
        print(textJsonData[it] + ' -> ' + translateText)
        out[it] = translateText

    print(out)

    jsonStr = json.dumps(out, ensure_ascii=False, indent=4)

    with open(os.getcwd()
                + '/OutputLang/'
                + inputFileName[:-5]
                + '_'
                + lang
                + '.json',
              mode='w',
              encoding='utf8'
              ) as outJson:
        outJson.write(jsonStr)
