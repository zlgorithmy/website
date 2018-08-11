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
        webData = request.body.decode("utf-8")
        print("")
        print(webData)
        print("")
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg):
            toUserName = recMsg.ToUserName;
            fromUserName = recMsg.FromUserName;
            createTime = recMsg.CreateTime;
            msgType = recMsg.MsgType;
            #msgId = recMsg.MsgId;

            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            return reply.TextMsg(toUser, fromUser, msgType).send()

            '''
            content = {
                    'text': reply.TextMsg(toUser, fromUser, "text"),
                    'image': reply.TextMsg(toUser, fromUser, "image"),
            }.get(msgType, reply.TextMsg(toUser, fromUser, 'Todo...')).send()

            if recMsg.MsgType == 'text':
                return reply.TextMsg(toUser, fromUser, recMsg.Content).send()

            elif recMsg.MsgType == 'image':
                return reply.ImageMsg(toUser, fromUser, recMsg.MediaId).send()

            elif recMsg.MsgType == 'file':
                content = 'file'
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()

            elif recMsg.MsgType == 'event':
                content = 'event'
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                content = 'Todetail'
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            '''
        else:
            content = '不懂...'
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return replyMsg.send()