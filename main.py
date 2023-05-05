import requests
import json
import time

with open('wallet.txt','r') as f :
    address = f.read().split('\n')
print(address)
for i in address :
    try:
        headers = {'Content-Type': 'application/json'}
        payload = {"address":"%s"%i}
        r = requests.post('https://api.sui-pepe.xyz/api/user-infos/caculator-airdrop', data=json.dumps(payload), headers=headers).json()
        data = r['data']
        if data['success'] == True : 
            print('address :',i)
            print('twitter_screen_name :',data['user_info']['twitter_screen_name'])
            print('tele_user_name :',data['user_info']['tele_user_name'])
            print('twitter_retweet_link :',data['user_info']['twitter_retweet_link'])
            print('CreatedAt :',data['user_info']['createdAt'])
            print('Airdop Amount :',data['user_info']['airdop_amount'])
            print('-----------------------------------')
            time.sleep(5)
        else :
            print(data['message'])
            print('-----------------------------------')
            time.sleep(5)
    except Exception as e:
        print(e)
        time.sleep(5)



