# -*- coding: utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    elif msg_type == 'event':
        return EventMsg(xmlData)
    elif msg_type == 'file':
        return FileMsg(xmlData)
    return Msg(xmlData)

class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text

class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text
        self.MsgId = xmlData.find('MsgId').text

class FileMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Title = xmlData.find('Title').text
        self.Description = xmlData.find('Description').text
        self.FileKey = xmlData.find('FileKey').text
        self.FileMd5 = xmlData.find('FileMd5').text
        self.FileTotalLen = xmlData.find('FileTotalLen').text
        self.MsgId = xmlData.find('MsgId').text

class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MsgId = xmlData.find('MsgId').text
        self.MediaId = xmlData.find('MediaId').text

class EventMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        print('------------------------------------')
        self.Event = xmlData.find('Event').text
        self.EventKey = xmlData.find('EventKey').text