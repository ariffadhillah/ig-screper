import requests

count = 0
end_cursor = ''
while True:
    url1 = 'https://www.instagram.com/explore/tags/baksobuah/?__a=1&max_id={}'.format(end_cursor)
    r1 = requests.get(url1).json()
    short_codes = r1['graphql']['hashtag']['edge_hashtag_to_media']['edges']

    for sc in short_codes:
        short_codes = sc['node']['shortcode']
        url2 = 'https://www.instagram.com/p/{}/?__a=1'.format(short_codes)
        r2 = requests.get(url2).json()
        username = r2['graphql']['shortcode_media']['owner']['username']
        print(username)
        count += 1
        file_name_image = '{} {}.jpg'.format(count, username)
        file_name_vidoe = '{} {}.mp4'.format(count, username)
        path_image = 'media_dowload/{}'.format(file_name_image)
        path_vidoe = 'media_dowload/{}'.format(file_name_vidoe)
        url_media_image = r2['graphql']['shortcode_media']['display_url']
        is_video = r2['graphql']['shortcode_media']['is_video']

        if is_video == True:
            url_media_vidoe = r2['graphql']['shortcode_media']['video_url']
            r_url_media_video = requests.get(url_media_vidoe).content
            open(path_vidoe, 'wb').write(r_url_media_video)
        if is_video == False:
            r_url_media_image = requests.get(url_media_image).content
            open(path_image, 'wb').write(r_url_media_image)
        print(count, short_codes)
    end_cursor = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    has_next_page = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    if has_next_page == False: break


