import requests
import json, time, csv

shortcode = input('Please enter id post instagram (shortcode) : ')

url = 'https://www.instagram.com/graphql/query'
end_cursor = ''
count = 0
count_file = 1
max_row = 100
writer = csv.writer(open('like-extraction-file/{} {}.csv'.format(shortcode, count_file), 'w', newline=''))
headers = ['No', 'Username', 'ID User', 'Full Name', 'Link Profile Pic']
writer.writerow(headers)
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
        if count % max_row == 0 and count != 0:
            count_file += 1
            writer = csv.writer(open('like-extraction-file/{} {}.csv'.format(shortcode, count_file), 'w', newline=''))
            headers = ['No', 'Username', 'ID User', 'Full Name', 'Link Profile Pic']
            writer.writerow(headers)
        username = user['node']['username']
        id_account = user['node']['id']
        full_name = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        print(count, username, id_account, full_name, profile_pic)
        writer = csv.writer(open('like-extraction-file/{} {}.csv'.format(shortcode, count_file), 'a', newline='', encoding='utf-8'))
        count += 1
        data = [count, username, id_account, full_name, profile_pic]
        writer.writerow(data)



    end_cursor = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    #print(end_cursor)
    has_next_page = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False :break
    time.sleep(2)

