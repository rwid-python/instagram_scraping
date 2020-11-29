import requests
import json, time, csv

shortcode = input('Please enter id post instagram (shortcode) : ')
query_hash = 'bc3296d1ce80a24b1b6e40b1e72903f5'
url = 'https://www.instagram.com/graphql/query'
end_cursor = ''
count = 0
count_file = 1
max_row = 100
writer = csv.writer(open('comment-extraction-file/{} {}.csv'.format(shortcode, count_file), 'w', newline=''))
headers = ['No', 'Username', 'ID User', 'Full Name', 'Link Profile Pic']
writer.writerow(headers)
while 1:
    variables = {
        'shortcode': shortcode, #'CIGnHwpAAbc',
        'first': 12,
        'after': end_cursor
    }
    headers = {'cookie': 'sessionid=1295926929%3AhPIUC1c69rGxiE%3A29'}
    params = {
        'query_hash': query_hash,
        'variables': json.dumps(variables)
    }
    r = requests.get(url, headers=headers, params=params).json()

    try: users = r['data']['shortcode_media']['edge_media_to_parent_comment']['edges']

    except:
        print('waiting for 20 secs')
        time.sleep(20)
        continue

    for user in users:
        if count % max_row == 0 and count != 0:
            count_file += 1
            writer = csv.writer(open('comment-extraction-file/{} {}.csv'.format(shortcode, count_file), 'w', newline=''))
            headers = ['No', 'Username', 'ID User', 'Full Name', 'Link Profile Pic']
            writer.writerow(headers)
        username = user['node']['owner']['username']
        id_account = user['node']['owner']['id']
        comment = user['node']['text']
        count += 1
        print(count, username, id_account, comment)
        writer = csv.writer(open('comment-extraction-file/{} {}.csv'.format(shortcode, count_file), 'a', newline='', encoding='utf-8'))
        data = [count, username, id_account, comment]
        writer.writerow(data)



    end_cursor = r['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor']
    #print(end_cursor)
    has_next_page = r['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page']
    if has_next_page == False :break
    time.sleep(2)

