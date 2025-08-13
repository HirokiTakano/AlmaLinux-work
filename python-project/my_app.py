#!/usr/bin/env python3

import requests #reuestsという「OS外ライブラリ」を利用することを宣言

#取得したいウェブサイトのURL
url = "https://freelance.persol-xtech.co.jp/freelance/lp/002/?utm_source=google&utm_medium=cpc&utm_campaign=pmax_001_001_lp011&gad_source=1&gad_campaignid=21304842603&gbraid=0AAAAACk0lf-5En4fNExjG70s5PYS0gV0p&gclid=CjwKCAjw7rbEBhB5EiwA1V49ndVGLX8MZEIWenHyBlIxa05_9Y8enNVfb3Qw1HnhLoKxkVMBcZkh_hoCHp8QAvD_BwE"

print("ウェブサイトから情報を取得します...")

#requestsライブラリのget()関数を呼び出し
response = requests.get(url)

#取得した内容を表示
print("取得完了。内容:")
print(response.text)