import requests, json

urls = 'https://www.instagram.com/graphql/query'

# CJzoM8pBOqL
# urls page

short_code = input("plases enter a short code : ")
variables = {"shortcode":short_code,"include_reel":True,"first":50}

headers = {'cookie': 'sessionid=45420922183%3AqCBAo4Vdn4xkeI%3A23'}
params = {
    "query_hash": "d5d763b1e2acf209d62d22d184488e57",
    "variables": json.dumps(variables)
}

respon = requests.get(urls, headers=headers, params=params).json()

users = respon['data']['shortcode_media']['edge_liked_by']['edges']
count = 0
for user in users:
    username = user['node']['username']
    full_name = user['node']['full_name']
    profile_pic_url = user['node']['profile_pic_url']
    print(username, full_name, profile_pic_url)

    count +=1
    print(count)
    # print(username)
    # print(username)
    # print(profile_pic_url)


