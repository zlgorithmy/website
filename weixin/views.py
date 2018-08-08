# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import hashlib

from . import receive,reply

def index(request):
    if request.method == "GET":
        data = request.GET

        signature = data.get('signature')
        echostr = data.get('echostr')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')

        token = "helloweixin"

        list = [token, timestamp, nonce]
        list.sort()

        sha1 = hashlib.sha1()
        sha1.update("".join(list).encode('utf-8'))

        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('')

    elif request.method == "POST":
        webData = request.body
        print(webData)
        recMsg = receive.parse_xml(webData)
        fromUserName = recMsg.FromUserName;
        toUserName = recMsg.ToUserName;
        createTime = recMsg.CreateTime;
        msgType = recMsg.MsgType;
        #msgId = recMsg.MsgId;

        print('fromUserName:'+fromUserName)
        print('toUserName:'+toUserName)
        print('createTime:'+createTime)
        print('msgType:'+msgType)
        #print('msgId:'+msgId)

        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        if isinstance(recMsg, receive.Msg):
            if recMsg.MsgType == 'text':
                content = recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif recMsg.MsgType == 'image':
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            elif recMsg.MsgType == 'event':
                content = 'event'.encode("utf-8")
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
        else:
            content = '不懂...'
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return replyMsg.send()