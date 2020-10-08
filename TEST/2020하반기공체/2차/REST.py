# 출처: https://devtalk.kakao.com/t/python-rest-api/37809
import requests, json

API_HOST = 'https://httpbin.org'
headers = {'accept': 'application/json'}


def req(path, query, method, data={}):
    url = API_HOST + path
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        return requests.post(url, headers=headers, data=data)
    elif method == 'PUT':
        return requests.post(url, headers=headers)
    elif method == 'PATCH':
        return requests.post(url, headers=headers, data=data)
    elif method == 'DELETE':
        return requests.delete(url, headers=headers)


resp = req('/get', '', 'GET')
resp = req('/base64/SFRUUEJJTiBpcyBhd2Vzb21l', '', 'GET')
print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
print("response body:\n%s" % resp.text)

json_data = json.loads(resp.text)
print(type(json_data))