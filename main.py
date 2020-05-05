# import re
#
# import requests
#
#
# def parse(url):
#     headers = {
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         # 'Cookie': 'bankrotcookie=6aae19bb5daea19305cee78d66f7c6c5; ASP.NET_SessionId=5h4oshrwjy3mtzirmznfvr1c; _ym_uid=1588359880601709400; _ym_d=1588359880; _ym_visorc_45311283=w; _ym_isad=2',
#         # 'Host': 'bankrot.fedresurs.ru',
#         # 'Referer': 'http://bankrot.fedresurs.ru/',
#         # 'Referer': 'https://buff.163.com/market/?game=csgo',
#         # 'Host': 'buff.163.com',
#         # 'cookie: remixflash=0.0.0; remixscreen_depth=24; remixscreen_orient=1; tmr_lvid=8f5c31881e7ecabd1b18460c226f4e91; tmr_lvidTS=1579528008521; remixusid=YWRiMGZhOWVhMGQ0YjBkNTMyZjg0OTQ0; remixstid=1479887354_DKmvidLofMnySmXqyXDTFCOpnEQzSHDtmI3EhJbhjQ4; tmr_lvid=8f5c31881e7ecabd1b18460c226f4e91; tmr_lvidTS=1579528008521; tmr_reqNum=770; remixdt=0; remixscreen_width=1536; remixscreen_height=864; remixscreen_dpr=1.25; remixua=37%7C-1%7C162%7C1399413221; remixgp=1fca2ff0eb5bde9061bd85a586279837; remixseenads=1; remixrefkey=c351cafc12a2d1cb5e; remixsid=6164dc2440b34a429182d8000901bec046556307a5dcc11a56def9e84a009; remixcurr_audio=371745461_456387069; remixscreen_winzoom=1.65; remixlang=0; tmr_tcdhn=1588605129601; tmr_detect=0%7C1588605132005; tmr_reqNum=773'
#         'accept-language': 'ru;q=0.8',
#         'referer': 'https://vk.com/friends',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
#     }
#     # html_code = requests.get(url, headers=headers).text
#     with open('test.txt', 'r', encoding='utf-8') as f:
#         html_code = f.read()
#     get_info(html_code)
#
#
# def get_info(html_code):
#     print(html_code)
#     if re.search(r'<aside aria-label="Аудиозаписи">', html_code):
#         print(True)
#
#
#
# if __name__ == '__main__':
#     # input()
#     parse('https://vk.com/fkirkorov')
#     pass
import datetime

import requests
from pprint import pprint as pp


def main():
    # user_id = 'fkirkorov'
    result_tim = ''
    user_id = 'dm'
    token = "f6f177fdf6f177fdf6f177fdd8f680dee1ff6f1f6f177fda8413e8aa1153eaddc74c4cb"  # Сервисный ключ доступа
    fields = 'can_see_audio,' \
             'followers_count,' \
             'status,' \
             'has_mobile,' \
             'about,' \
             'personal,' \
             'bdate,' \
             'books,' \
             'career,' \
             'connections,' \
             'education,' \
             'interests,' \
             'military,' \
             'occupation,' \
             'relation,' \
             'site'
    dict_about_user = eval(requests.post(f'https://api.vk.com/method/users.get?user_ids={user_id}&fields={fields}&access_token={token}&v=5.103').text.replace('false', 'False').replace('true', 'True'))['response'][0]

    pp(dict_about_user)

    amount_of_subscribers = dict_about_user.get('followers_count')
    status = dict_about_user.get('status')
    connections = bool(dict_about_user.get('skype') or dict_about_user.get('facebook') or dict_about_user.get('livejournal') or dict_about_user.get('instagram') or dict_about_user.get('twitter'))

    count_of_friends = eval(requests.post(
        f'https://api.vk.com/method/friends.get?user_id={dict_about_user.get("id")}&count=201&access_token={token}&v=5.103').text.replace(
        'false', 'False').replace('true', 'True')).get('response').get('count')

    posts = eval(requests.post(
        f'https://api.vk.com/method/wall.get?owner_id={dict_about_user.get("id")}&count=31&filter=owner,others&access_token={token}&v=5.103').text.replace(
        'false', 'False').replace('true', 'True')).get('response')

    count_of_posts = posts.get('count')

    amount_of_photo = eval(requests.post(
        f'https://api.vk.com/method/photos.get?owner_id={dict_about_user.get("id")}&count=1&album_id=profile&access_token={token}&v=5.103').text.replace(
        'false', 'False').replace('true', 'True')).get('response').get('count')

    # pp(posts)
    dict_of_posts = {'owner': [],
                     'date': [],
                     'capasity': []}
    for post in posts.get('items'):
        # print(datetime.datetime.fromtimestamp(int(post.get('date'))).strftime('%Y-%m-%d'))
        dict_of_posts.get('owner').append('self' if post.get('owner_id') == dict_about_user.get("id") else post.get('owner_id'))
        dict_of_posts.get('date').append(datetime.datetime.fromtimestamp(int(post.get('date'))).strftime('%Y-%m-%d'))
        dict_of_posts.get('capasity').append('big' if len(post.get('text').split(' ')) > 30 else 'small')

    mark_to_I = 0
    mark_to_E = 0

    if dict_about_user.get('can_see_audio') == 0:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if dict_about_user.get('is_closed'):
        mark_to_I += 1
    else:
        mark_to_E += 1

    if amount_of_photo < 50:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if amount_of_subscribers < 200:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if count_of_friends < 200:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if count_of_posts < 30:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if not status:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if dict_of_posts.get('capasity').count('small') > dict_of_posts.get('capasity').count('big'):
        mark_to_I += 1
    else:
        mark_to_E += 1

    if mark_to_I >= mark_to_E:
        result_tim += 'I'

    


if __name__ == '__main__':
    main()
