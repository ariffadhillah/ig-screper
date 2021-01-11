import csv

import requests, json, time

urls = 'https://www.instagram.com/graphql/query'

# CJzoM8pBOqL
# urls page

short_code = input("plases enter a short code : ")

end_cursor = ''
count = 0
counter_file = 1
jumlah_per_file = 100


writer = csv.writer(open('hasil_like/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
headers = ['User Name', 'Full Name', 'Profile Pic']
writer.writerow(headers)

while 1:
    variables = {
        "shortcode": short_code,
        "first": 50,
        "after": end_cursor
    }

    headers = {'cookie': 'sessionid=45420922183%3ALfWeLZO33GXr2X%3A1'}
    params = {
        "query_hash": "d5d763b1e2acf209d62d22d184488e57",
        "variables": json.dumps(variables)
    }

    respon = requests.get(urls, headers=headers, params=params).json()

    try: users = respon['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('wait for 20 secs')
        time.sleep(20)
        continue

    for user in users:
        if count % jumlah_per_file == 0 and count!=0:
            counter_file +=1
            writer = csv.writer(open('hasil_like/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
            headers = ['User Name', 'Full Name', 'Profile Pic']
            writer.writerow(headers)

        username = user['node']['username']
        full_name = user['node']['full_name']
        profile_pic_url = user['node']['profile_pic_url']
        count += 1
        print(count, username, full_name, profile_pic_url)
        writer = csv.writer(open('hasil_like/{} {}.csv'.format(short_code, counter_file), 'a', newline='', encoding='utf-8'))
        data = [username, full_name, profile_pic_url]
        writer.writerow(data)

    end_cursor = respon['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    has_next_page = respon['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False: break
    time.sleep(2)
