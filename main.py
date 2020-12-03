import requests


skin_id = input('Enter skin id: ')
request = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/ids', params={'id': skin_id}).json()

def history():
    history_m = request['data'][0]['shopHistory']
    history_l = len(request['data'][0]['shopHistory'])
    print('Item History:')
    for i in range(history_l):
        print(history_m[i].replace('T00:00:00Z', ''))

def check(f_part, s_part):
    try:
        print(f_part, s_part)
    except:
        print(f_part, 'None')

check('Name:', request['data'][0]['name'])
check('ID:', request['data'][0]['id'])
check('Description:', request['data'][0]['description'])
check('Rarity:', request['data'][0]['rarity']['displayValue'])
check('Season:', request['data'][0]['introduction']['season'])
check('Chapter:', request['data'][0]['introduction']['chapter'])
check('Image:', request['data'][0]['images']['icon'])
check('Showcase:', request['data'][0]['showcaseVideo'])
try:
    history()
except:
    print('Item History: None')

input()