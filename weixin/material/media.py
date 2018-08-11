# -*- coding: utf-8 -*-
# filename: media.py
import sys
sys.path.append('..')
from basic import *

import urllib.request
import requests
import json
import urllib
import pycurl
from io import *
from requests_toolbelt.multipart.encoder import MultipartEncoder
from requests_toolbelt import MultipartEncoder

print(sys.path)
class Media(object):
    def uplaod(self, filePath, mediaType):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)

        body = BytesIO()
        pc = pycurl.Curl()
        pc.setopt(pycurl.WRITEFUNCTION, body.write)
        pc.setopt(pycurl.POST, 1)
        pc.setopt(pycurl.URL, postUrl)
        pc.setopt(pycurl.HTTPPOST, [('media', (pc.FORM_FILE, filePath))])
        pc.perform()
        response = pc.getinfo(pycurl.RESPONSE_CODE)
        pc.close()
        html = body.getvalue().decode("utf-8")
        print(html)

    def download(self, mediaId):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib.request.urlopen(postUrl)

        headers = urlResp.info().__dict__['_headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print (jsonDict)
        else:
            buffer = urlResp.read()
            mediaFile = open("test.jpg", "wb")
            mediaFile.write(buffer)
            print ("get successful")

class Material(object):
    def uplaodImg(self, filePath, mediaType):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (accessToken, mediaType)

        body = BytesIO()
        pc = pycurl.Curl()
        pc.setopt(pycurl.WRITEFUNCTION, body.write)
        pc.setopt(pycurl.POST, 1)
        pc.setopt(pycurl.URL, postUrl)
        pc.setopt(pycurl.HTTPPOST, [('media', (pc.FORM_FILE, filePath))])
        pc.perform()
        response = pc.getinfo(pycurl.RESPONSE_CODE)
        pc.close()
        html = body.getvalue().decode("utf-8")
        print(html)
    def uplaod(self, news):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(postUrl, str.encode(news))
        print (urlResp.read())

    def getmedia(self):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/get_materialcount?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(postUrl)
        print (urlResp.read())

    def get_media_detail(self):
        accessToken = Basic().get_access_token()
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s" % accessToken
        news =(
        {
            "type":"image",
            "offset":0,
            "count":1
        })
        news = json.dumps(news, ensure_ascii=False)
        urlResp = urllib.request.urlopen(postUrl, str.encode(news))
        print (urlResp.read())

if __name__ == '__main__':
    # myMedia = Media()

    # #临时素材上传
    # filePath = "/home/zlgorithmy/image/1.jpeg"
    # mediaType = "image"
    # myMedia.uplaod(filePath, mediaType)

    # #临时素材下载
    # mediaId = "3C2kdx9dnKwrb89Aw3O-JF4e6MS7zK6WmUqEanbulMHcLMMHtghkm3ASQJOPbtV3"
    # myMedia.download(mediaId)

    #永久素材上传
    myMaterial = Material()
    #content = "<p><img src="" alt="" data-width="18" data-ratio="0.5"><br  /><img src="" alt="" data-width="128" data-ratio="0.5"><br  /></p>"
    content = ""
    news =(
    {
        "articles":
        [
            {
            "title": "test",
            "thumb_media_id": "3C2kdx9dnKwrb89Aw3O-JF4e6MS7zK6WmUqEanbulMHcLMMHtghkm3ASQJOPbtV3",
            "author": "vickey",
            "digest": "",
            "show_cover_pic": 1,
            "content": content,
            "content_source_url": "",
            }
        ]
    })
    #news 是个dict类型，可通过下面方式修改内容
    #news['articles'][0]['title'] = u"测试".encode('utf-8')
    #print news['articles'][0]['title']
    news = json.dumps(news, ensure_ascii=False)
    myMaterial.uplaod(news)
    myMaterial.getmedia()
    myMaterial.get_media_detail()
    filePath = "/home/zlgorithmy/image/1.jpeg"
    mediaType = "image"
    myMaterial.uplaodImg(filePath, mediaType)