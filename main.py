import requests
import random

def generate_answ():
    #Строка со ссылкой на форму
    GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdDDTYzEEq7dJBrWus6JpFRh3iT-ugteni06g-hdnBSEOMbjw'

    urlResponse = GoogleURL+'/formResponse'
    urlReferer = GoogleURL+'/viewform'

    inst_list = ['ИИТиАД', 'ИЭ', 'ИАМиТ', 'ИАСиД', 'ИВТ', 'ИН', 'ИЭУП']

    rast_list = ['30-40 сантиметров', '40-50 сантиметров', '60-70 сантиметров', '70-100 сантиметров', 'Не имеет значения']

    r = random.randint(1, 6)
    if r >= 5:
        glass = 'Да'
    else:
        glass = 'Нет'

    r = random.randint(1, 6)
    if r >= 4:
        filt = 'Да'
    else:
        filt = 'Нет'

    diag_list = ['6 дюймов', '10 дюймов', '17 дюймов', '20 дюймов']

    r = random.randint(1, 6)
    if r >= 5:
        antiblik = 'Да'
    else:
        antiblik = 'Нет'

    night_list = ['Да', 'Использую, но как ночник', 'Нет']

    gimn_list = ['Каждые 10 минут', 'Каждые 30 минут', 'Каждые 45 минут', 'Каждые 60 минут', 'Не нужно']

    pologenie_list = ['Стоя', 'Сидя с прямой спиной', 'Лежа', 'Сидя произвольно']

    r = random.randint(1, 6)
    if r >= 5:
        kapli = 'Да'
    else:
        kapli = 'Нет'

    monitor_list = ['Ниже уровня глаз', 'На уровне глаз', 'Выше уровня глаз', 'Под углом']
    #Подготовка ответов в связки с ключами к вопросам
    form_data = {'entry.17028875': random.choice(inst_list),
                 'entry.1519727847': random.choice(rast_list),
                 'entry.2056483453': glass,
                 'entry.521871620': filt,
                 'entry.1950674401': random.choice(diag_list),
                 'entry.1441385079': antiblik,
                 'entry.548818486': random.choice(night_list),
                 'entry.2094194997': random.choice(gimn_list),
                 'entry.1144299922': random.choice(pologenie_list),
                 'entry.1684983204': kapli,
                 'entry.1726174089': random.choice(monitor_list)}

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