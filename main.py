# Задача №1
# Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:
#
# Путь к файлу с текстом;
# Путь к файлу с результатом;
# Язык с которого перевести;
# Язык на который перевести (по-умолчанию русский).
# У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком.
# Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.


import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190827T202940Z.2c49395d596e72e6.b347e4d8ce5e733c54bcbf89895db63e5841a947'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(path_file_text, path_file_result, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    with open(path_file_text, encoding='utf-8') as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': from_lang+'-'+to_lang,
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(path_file_result, 'w', encoding='utf-8') as f:
        f.write(json_['text'][0])


if __name__ == '__main__':
    translate_it('DE.txt', 'DE-RU.txt', 'de', 'ru')
    translate_it('ES.txt', 'ES-RU.txt', 'es', 'ru')
    translate_it('FR.txt', 'FR-RU.txt', 'fr', 'ru')