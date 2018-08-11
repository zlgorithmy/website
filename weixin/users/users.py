# -*- coding: utf-8 -*-
# filename: media.py
import sys
sys.path.append('..')
from basic import *

import urllib.request
import urllib

class User(object):
    def get_userlist(self):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=" % accessToken
        urlResp = urllib.request.urlopen(postUrl)
        print (urlResp.read())

    def get_userInfo(self,openid):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=" %(accessToken, openid)
        urlResp = urllib.request.urlopen(postUrl)
        print (urlResp.read().decode("utf-8"))
if __name__ == '__main__':
    myUser = User()
    myUser.get_userlist()
    myUser.get_userInfo("oLzcz1oHrKVsbGgQ2w72Gu7R-CEY")