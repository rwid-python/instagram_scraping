import requests
import json
import time

shortcode = input('Please enter id post instagram (shortcode) : ')

url = 'https://www.instagram.com/graphql/query'
end_cursor = ''
count = 1

while 1:
    variables = {
        'shortcode': shortcode, #'CHmEEc6j0tE',
        'include_reel': True,
        'first': 12,
        'after': end_cursor
    }
    headers = {'cookie': 'sessionid=1295926929%3AhPIUC1c69rGxiE%3A29'}
    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(variables)
    }
    r = requests.get(url, headers=headers, params=params).json()

    try: users = r['data']['shortcode_media']['edge_liked_by']['edges']

    except:
        print('waiting for 20 secs')
        time.sleep(20)
        continue

    for user in users:
        username = user['node']['username']
        id_account = user['node']['id']
        full_name = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        print(count, username, id_account, full_name, profile_pic)
        count += 1

    end_cursor = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    #print(end_cursor)
    has_next_page = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False :break
    time.sleep(2)

