import requests
import pprint

# post request
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)

# # complex post request
# payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
# r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
# payload_dict = {'key1': ['value1', 'value2']}
# r2 = requests.post('https://httpbin.org/post', data=payload_dict)
# print(r1.text)
# r1.text == r2.text


# # direct json posting
# import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))

# # json parameter posting
# # Note, the json parameter is ignored if either data or files is passed.
url = 'https://vapi.verifyme.ng/v1/verifications/identities/nin_phone/1000000001'
payload = {"firstname":"Isaac","lastname":"Adedayo"}
r = requests.post(url, json=payload)
# print(r.json())
headers = {
    'Content-Type': 'application/json',
    'Authorization' : 'Bearer key'
}

resp = requests.post(url, json=payload , headers=headers)

print(resp.json())


# # POST a Multipart-Encoded File
# # Requests makes it simple to upload Multipart-encoded files:
# url = 'https://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
# r.text



# # Response Status Codes
# #We can check the response status code:
# r = requests.get('https://httpbin.org/get')
# r.status_code
# r.status_code == requests.codes.ok


# # Response Headers
# # We can view the server’s response headers using a Python dictionary
# r.headers
# r.headers['Content-Type']
# # 'application/json'

# r.headers.get('content-type')
# # 'application/json'




# # get requests
# url = 'https://vapi.verifyme.ng/v1/verifications/addresses/<id>'
# parameters = {'id':'1'}
# headers = { 
#     'Accepts' :'Application/json',
#     'key':''
# }

# response = requests.get(url , params=parameters , headers=headers)
# response = requests.get(url)

# # print(response.url)
# # print(response.text)
# # print(response.encoding)
# # print(response.content)
# print(response.json())