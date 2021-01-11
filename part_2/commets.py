import requests, json, time, csv

urls = 'https://www.instagram.com/graphql/query'

short_code = 'CJb0J9nhovF'
query_hash = 'bc3296d1ce80a24b1b6e40b1e72903f5'

end_cursor = ''
count = 0
counter_file = 1
jumlah_per_file = 100

writer = csv.writer(open('comment_result/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
headers = ['User Name', 'Text']
writer.writerow(headers)

while 1:
    variables = {"shortcode": short_code, "first": 50, "after": end_cursor}
    params = {
        "query_hash": short_code,
        "variables": json.dumps(variables)
    }

    respon = requests.get(urls, params=params).json()

    try:
        users = respon['data']['shortcode_media']['edge_media_to_parent_comment']['edges']
    except:
        print('wait for 30 secs')
        time.sleep(30)
        continue

    for user in users:
        if count % jumlah_per_file == 0 and count != 0:
            counter_file += 1
            writer = csv.writer(open('comment_result/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
            headers = ['User Name', 'Text']
            writer.writerow(headers)

        username = user['node']['owner']['username']
        text = user['node']['text']
        writer = csv.writer(
            open('comment_result/{} {}.csv'.format(short_code, counter_file), 'a', newline='', encoding='utf-8'))
        data = [username, text]
        writer.writerow(data)
        count += 1
        print(count, username, text)

        end_cursor = respon['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor']
        has_next_page = respon['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page']
        if has_next_page == False: break
        time.sleep(2)

    # CJiP4eShX0W
