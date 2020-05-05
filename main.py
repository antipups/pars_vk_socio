import datetime
import re

import requests
from pprint import pprint as pp


def get_vk_page(id_of_page):
    data = {
        'act': 'login',
        'role': 'al_frame',
        'expire': '',
        'to': 'aW5kZXgucGhw',
        'recaptcha': '',
        'captcha_sid': '',
        'captcha_key': '',
        '_origin': 'https://vk.com',
        'ip_h': 'ab4dfb826cd66a97ca',
        'lg_h': '4e691fa18b08cf03ac',
        'ul': '',
        'email': '380713522494',
        'pass': 'Nick0713671228',
    }

    headers = {
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        'content-length': '212',
        'cookie': 'remixlang=3; remixbdr=1; remixstid=327724220_i9Z1KY6PvnGzWIzIbJtfRT0RFZml6t63vSLTAuqLqeH; remixlhk=f39f9010dcfad4cfbd; remixflash=0.0.0; remixscreen_width=1536; remixscreen_height=864; remixscreen_dpr=1.25; remixscreen_depth=24; remixscreen_orient=1; remixscreen_winzoom=1; remixgp=1fca2ff0eb5bde9061bd85a586279837; remixdt=0; tmr_lvid=e2a22a20ced131ec4e69fa39af45c606; tmr_lvidTS=1588675607484; tmr_reqNum=1; remixjsp=%7B%22id%22%3A%22k9tsfur0.w2%22%2C%22loc%22%3A%22https%3A//vk.com/%22%2C%22events%22%3A%5B%5B%22TTFCP%22%2C2561%2Cnull%2C%224g%22%2C%2224286%22%5D%2C%5B%22domComplete%22%2C3412%2Cnull%2C%224g%22%2C%2224286%22%5D%2C%5B%22domContentLoadedEventEnd%22%2C2574%2Cnull%2C%224g%22%2C%2224286%22%5D%2C%5B%22loadEventEnd%22%2C3414%2Cnull%2C%224g%22%2C%2224286%22%5D%2C%5B%22TTI%22%2C2576%2Cnull%2C%224g%22%2C%2224286%22%5D%5D%7D',
        'referer': 'https://vk.com/feed',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    s = requests.Session()

    print(s.post('https://login.vk.com/?act=login', headers=headers, data=data).status_code)

    # del headers['cookie']
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'remixbdr=1; remixstid=327724220_i9Z1KY6PvnGzWIzIbJtfRT0RFZml6t63vSLTAuqLqeH; remixflash=0.0.0; remixscreen_width=1536; remixscreen_height=864; remixscreen_dpr=1.25; remixscreen_depth=24; remixscreen_orient=1; remixgp=1fca2ff0eb5bde9061bd85a586279837; remixdt=0; tmr_lvid=e2a22a20ced131ec4e69fa39af45c606; tmr_lvidTS=1588675607484; remixlang=0; remixusid=YjM2OGIzYmQxYzBmOGFmY2FkNzUzOWMy; remixseenads=1; remixsid=3fa7623c51166393a3424a39d14b1aff95934ba9f139fe7b2be10262a548c; remixscreen_winzoom=1.65; tmr_detect=0%7C1588677057737; tmr_reqNum=16',
        'referer': 'https://vk.com/feed',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    return s.get('https://vk.com/' + id_of_page, headers=headers).text


def main():
    # user_id = 'fkirkorov'
    # user_id = 'dm'
    user_id = 'id5979589'
    result_tim = ''
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
             'site,' \
             'relatives,' \
             'city'
    dict_about_user = eval(requests.post(f'https://api.vk.com/method/users.get?user_ids={user_id}&fields={fields}&access_token={token}&v=5.103').text.replace('false', 'False').replace('true', 'True'))['response'][0]

    pp(dict_about_user)

    amount_of_subscribers = dict_about_user.get('followers_count')
    status = dict_about_user.get('status')
    connections = bool(dict_about_user.get('skype') or dict_about_user.get('facebook') or dict_about_user.get('livejournal') or dict_about_user.get('instagram') or dict_about_user.get('twitter'))

    count_of_friends = eval(requests.post(
        f'https://api.vk.com/method/friends.get?user_id={dict_about_user.get("id")}&count=201&access_token={token}&v=5.103').text.replace(
        'false', 'False').replace('true', 'True')).get('response').get('count')

    posts = None
    posts = eval(requests.post(
        f'https://api.vk.com/method/wall.get?owner_id={dict_about_user.get("id")}&count=31&filter=owner,others&access_token={token}&v=5.103').text.replace(
        'false', 'False').replace('true', 'True'))

    if not posts.get('error'):
        posts = posts.get('response')
        count_of_posts = posts.get('count')
    else:
        posts = None

    amount_of_photo = eval(requests.post(
        f'https://api.vk.com/method/photos.get?owner_id={dict_about_user.get("id")}&count=1&album_id=profile&access_token={token}&v=5.103').text.replace(
        'false', 'False').replace('true', 'True')).get('response').get('count')

    # pp(posts)
    if posts:
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

    if posts and count_of_posts < 30:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if not status:
        mark_to_I += 1
    else:
        mark_to_E += 1

    if posts and dict_of_posts.get('capasity').count('small') > dict_of_posts.get('capasity').count('big'):
        mark_to_I += 1
    else:
        mark_to_E += 1

    result_tim += 'I' if mark_to_I >= mark_to_E else 'E'


    ###################################################################

    # сенсорик или интуит

    ###################################################################

    mark_to_S = 0
    mark_to_N = 0

    # if dict_about_user.get('bdate'):
    #
    # else:

    #html_code = get_vk_page(user_id)
    amount_of_videos , amount_of_audios, amount_of_alboms = 0, 0, 0
    with open('test.txt', 'r', encoding='utf-8') as f:
        html_code = f.read()
    for i in re.finditer(r'<span class=\"header_label fl_l\">((?!</div>).)*', html_code, re.DOTALL):
        div = i.group()
        print(div)
        if 'Видеозаписи' in div:
            amount_of_videos = re.search(r'\d{1,6}', div).group()
        elif 'Аудиозаписи' in div:
            amount_of_audios = re.search(r'\d{1,6}', div).group()
        if 'Фотоальбомы' in div:
            amount_of_alboms = re.search(r'\d{1,6}', div).group()

    if int(amount_of_audios) < 100:
        mark_to_S += 1
    else:
        mark_to_N += 1

    if int(amount_of_videos) < 30:
        mark_to_S += 1
    else:
        mark_to_N += 1











if __name__ == '__main__':
    main()
