import requests
import random

def generate_answ():
    #Строка со ссылкой на форму
    GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSetnfLfcmjBJbH8O12-107Ha2ebKUGF7barfXIpS9oNerWQTA'

    urlResponse = GoogleURL+'/formResponse'
    urlReferer = GoogleURL+'/viewform'

    inst_list = ['ИИТиАД', 'ИЭ', 'ИАМиТ', 'ИАСиД', 'ИВТ', 'ИН', 'ИЭУП']

    rast_list = ['30-40 сантиметров', '40-50 сантиметров', '70-100 сантиметров', 'Не имеет значения']

    r = random.randint(1,100)
    if r > 60:
        rast = '60-70 сантиметров'
    else:
        rast = random.choice(rast_list)

    r = random.randint(1, 100)
    if r >= 40:
        glass = 'Да'
    else:
        glass = 'Нет'

    r = random.randint(1, 100)
    if r >= 45:
        filt = 'Да'
    else:
        filt = 'Нет'

    diag_list = ['6 дюймов', '10 дюймов', '20 дюймов']
    r = random.randint(1, 100)
    if r >= 61:
        diag = '17 дюймов'
    else:
        diag = random.choice(diag_list)

    r = random.randint(1, 100)
    if r >= 42:
        antiblik = 'Да'
    else:
        antiblik = 'Нет'

    night_list = ['Использую, но как ночник', 'Нет']
    r = random.randint(1, 100)
    if r >= 58:
        night = 'Да'
    else:
        night = random.choice(night_list)

    gimn_list = ['Каждые 10 минут', 'Каждые 30 минут', 'Каждые 60 минут', 'Не нужно']
    r = random.randint(1, 100)
    if r >= 55:
        gimn = 'Каждые 45 минут'
    else:
        gimn = random.choice(gimn_list)

    pologenie_list = ['Лежа', 'Сидя произвольно', 'Стоя']
    r = random.randint(1, 100)
    if r >= 45:
        pologenie = 'Сидя с прямой спиной'
    else:
        pologenie = random.choice(pologenie_list)

    r = random.randint(1, 100)
    if r >= 50:
        kapli = 'Да'
    else:
        kapli = 'Нет'

    monitor_list = ['Ниже уровня глаз', 'Выше уровня глаз', 'Под углом']
    r = random.randint(1, 100)
    if r >= 65:
        monitor = 'На уровне глаз'
    else:
        monitor = random.choice(monitor_list)

    #Подготовка ответов в связки с ключами к вопросам
    form_data = {'entry.17028875': random.choice(inst_list),
                 'entry.1519727847': rast,
                 'entry.2056483453': glass,
                 'entry.521871620': filt,
                 'entry.1950674401': diag,
                 'entry.1441385079': antiblik,
                 'entry.548818486': night,
                 'entry.2094194997': gimn,
                 'entry.1144299922': pologenie,
                 'entry.1684983204': kapli,
                 'entry.1726174089': monitor}

    print(form_data)
    #Сборка ответа и загрузка в форму
    user_agent = {'Referer':urlReferer,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    req = requests.post(urlResponse, data=form_data, headers=user_agent)

def main():
    text = input("Введите количество человек для генерации: ")
    count = int(text)
    i = 0
    while i < count:
        generate_answ()
        i+=1

if __name__ == '__main__':
    main()
