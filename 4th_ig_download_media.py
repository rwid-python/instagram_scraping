import requests

headers = {'cookie': 'sessionid=1295926929%3AhPIUC1c69rGxiE%3A29'}
tag = 'bajuanakmurah'
count = 0
end_cursor = ''
while True:
    # get api instagram more simple use link json ([link]/?__a=1
    url1 = 'https://www.instagram.com/explore/tags/{}/?__a=1&max_id={}'.format(tag, end_cursor)
    r1 = requests.get(url1, headers=headers).json()

    short_codes = r1['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    for sc in short_codes:
        short_code = sc['node']['shortcode']
        #get info by post used short_code
        url2 = 'https://www.instagram.com/p/{}/?__a=1'.format(short_code)
        r2 = requests.get(url2, headers=headers).json()
        username = r2['graphql']['shortcode_media']['owner']['username']
        media_url = r2['graphql']['shortcode_media']['display_url']
        is_video = r2['graphql']['shortcode_media']['is_video']
        r_media_url = requests.get(media_url, headers=headers).content
        if is_video == True :
            filename='{} {} {}.mp4'.format(count, short_code, username)
        else:
            filename='{} {} {}.jpg'.format(count, short_code, username)
        path = 'media-download/{}'.format(filename)
        count += 1
        open(path, 'wb').write(r_media_url)

        print(count, short_code, username)
    end_cursor = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    has_next_page = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    if has_next_page == False : break

