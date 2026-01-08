import random, time, json
import requests, codecs

import brotli #brotlipy

def br_decode(content):
    return json.loads(brotli.decompress(content))


url = "https://www.sravni.ru/proxy-casco-frontend/apigateway/auto-info/"
headers = {}
params = {}


#payload
#body

#103.251.167.151:16972

headers['Content-Type'] = 'application/json'

coockies_1 = '.ASPXANONYMOUS=3Lmnz3ILNEK52gw8ePCoIg; _SLv2_=1405113; _iplv2=1405113; _SL_=6.83.; _ipl=6.83.; __utmz=utmccn%3d(not%20set)%7cutmcsr%3dgoogle%7cutmcmd%3dorganic%7cutmcct%3d(not%20set)%7cutmctr%3d(not%20set); _ym_uid=1767895364686911457; _ym_d=1767895364; _ym_isad=1; systemTheme=guinness; _gcl_au=1.1.762553619.1767895366; _ga=GA1.1.670930820.1767895366; _yasc=X9hjRUqm6h8mKEE/qUq+K8V6ggvXqmEGfHXEyhZt/ImynhsDgJczcucLr9tao9B/6A==; tmr_lvid=9b5794b818a91485fa0e1b5d29c90c68; tmr_lvidTS=1767895367409; tmr_detect=1%7C1767895367434; domain_sid=fShedqJXwVcc6mBVlvFSA%3A1767895368006; mindboxDeviceUUID=de850c12-1a39-4213-a4c0-94a1295618a1; directCrm-session=%7B%22deviceGuid%22%3A%22de850c12-1a39-4213-a4c0-94a1295618a1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ga_WE262B3KPE=GS2.1.s1767895366$o1$g1$t1767895542$j31$l0$h0'
headers['Accept']='application/json, text/plain, */*'
headers['Accept-Encoding']='gzip, deflate, br, zstd'
headers['Accept-Language']="ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
headers['Cache-Control']="no-cache"
headers['Content-length']="29"

headers['Referer'] ="https://www.sravni.ru/kasko/"



def post_plate(plate):
    headers['Content-Type'] = 'application/json'

    coockies_1 = '.ASPXANONYMOUS=3Lmnz3ILNEK52gw8ePCoIg; _SLv2_=1405113; _iplv2=1405113; _SL_=6.83.; _ipl=6.83.; __utmz=utmccn%3d(not%20set)%7cutmcsr%3dgoogle%7cutmcmd%3dorganic%7cutmcct%3d(not%20set)%7cutmctr%3d(not%20set); _ym_uid=1767895364686911457; _ym_d=1767895364; _ym_isad=1; systemTheme=guinness; _gcl_au=1.1.762553619.1767895366; _ga=GA1.1.670930820.1767895366; _yasc=X9hjRUqm6h8mKEE/qUq+K8V6ggvXqmEGfHXEyhZt/ImynhsDgJczcucLr9tao9B/6A==; tmr_lvid=9b5794b818a91485fa0e1b5d29c90c68; tmr_lvidTS=1767895367409; tmr_detect=1%7C1767895367434; domain_sid=fShedqJXwVcc6mBVlvFSA%3A1767895368006; mindboxDeviceUUID=de850c12-1a39-4213-a4c0-94a1295618a1; directCrm-session=%7B%22deviceGuid%22%3A%22de850c12-1a39-4213-a4c0-94a1295618a1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ga_WE262B3KPE=GS2.1.s1767895366$o1$g1$t1767895542$j31$l0$h0'
    headers['Accept']='application/json, text/plain, */*'
    headers['Accept-Encoding']='gzip, deflate, br, zstd'
    headers['Accept-Language']="ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    headers['Cache-Control']="no-cache"
    headers['Content-length']="29"

    headers['Referer'] ="https://www.sravni.ru/kasko/"

    res = requests.post(url, headers=headers, json={"autoNumber": plate})
    code = res.status_code
    if not code in (204, 409, 404):
        print(f"WOW! \n{plate}\n{res.text}")
    return res

res = requests.post(url, headers=headers, json={"autoNumber": "Т312ВМ799"})
print(dir(res))
assert res.status_code == 409, "теперь не 409й код на 1й вариант запроса."



###############################
def gen_random_plate():
    letters = "УКЕНХОРАВСМТ"
    regions = "77, 97, 99, 177, 197, 199, 777, 797, 799, 977".split(", ")
    _1 = random.choice(letters)
    _2 = random.randint(0, 10)
    _3 = random.randint(0, 10)
    _4 = random.randint(0, 10)

    _5 = random.choice(letters)
    _6 = random.choice(letters)
    _7 = random.choice(regions)
    res = _1 + str(_2) + str(_3) + str(_4) + str(_5) + str(_6) + str(_7)
    return res

###########
print(gen_random_plate())
print(gen_random_plate())
print(gen_random_plate())
print(gen_random_plate())
print(gen_random_plate())
print(gen_random_plate())
print(gen_random_plate())



headers['Content-Type'] = "abracadabra."
headers['Referer'] ="shit"
res = requests.post(url, headers=headers, json={"autoNumber": "Т312ВМ799"})
print(res.status_code)
assert res.status_code == 204, "Тут он должен был сказать ОТВАЛИ ЧЁРТ НИЧЕГО НЕ ПОЛУЧИШЬ, вернув 204й код."

headers['Content-Type'] = 'application/json'
headers['Referer'] ="shit"
res = requests.post(url, headers=headers, json={"autoNumber": "Т312ВМ799"})
print(res.status_code)
assert res.status_code == 409, "на норм контент тайм но плохой Реферер куки сервер отвечал 409 ранее."

headers['Content-Type'] = 'application/json'
headers['Referer'] ="https://www.sravni.ru/kasko/"
res = requests.post(url, headers=headers, json={"autoNumber": "Т312ВМ799"})
print(res.status_code)
assert res.status_code in (204, 409) , "not 204\409?..."


headers['Content-Type'] = 'application/json'
headers['Referer'] ="https://www.sravni.ru/kasko/"
res = requests.post(url, headers=headers, json={"autoNumber": "Т1xsВМ799"})
print(res.status_code)
assert res.status_code in (404,) , "not 404??..."


def gen_random_plate():
    letters = "УКЕНХОРАВСМТ"
    regions = "77, 97, 99, 177, 197, 199, 777, 797, 799, 977".split(", ")
    _1 = random.choice(letters)
    _2 = random.randint(0, 10)
    _3 = random.randint(0, 10)
    _4 = random.randint(0, 10)

    _5 = random.choice(letters)
    _6 = random.choice(letters)
    _7 = random.choice(regions)
    res = _1 + str(_2) + str(_3) + str(_4) + str(_5) + str(_6) + str(_7)
    return res

#wow plate: В185РВ799, Т611ЕВ977,К048ОТ797


def get_info_by_plate(plate):
    res = post_plate(plate)
    info = br_decode(res.content)

#plates = [gen_random_plate() for i in range(500)]
plates = ["В185РВ799", "Т611ЕВ977","К048ОТ797"]

plates = ["В185РВ799",]
for plate in plates:
    print(plate)
    res = post_plate(plate)
    time.sleep(0.3 + 0.2*random.randint(0,10))


#with codecs.open("fout.txt", "utf-8", "a+"):
#    fout.write(res.content)




#'XW8******KG027494'
#>>> z['isTaxi']
#False
#z['color']
#>>> z['selectedInsuranceCoverage']
#1200000

# мы можем найти самые дорогие машины москвы))
# или все розовые машины
# илисамые мощные
# или составить статистику автомобильного состава москвы
# категорию машины
# можно собрать статистику по авто в регионах


# статус код 204 == "номер найден но мы ничего не скажем про эту машину"
# 409 - не понятно. Indicates that the request could not be processed because of conflict in the current state of the resource, such as an edit conflict between multiple simultaneous updates.
# 404 - номер не найден.
# 200 - найден.
