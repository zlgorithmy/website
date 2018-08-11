from django.shortcuts import render
from django.http import HttpResponse
from django.utils.six import BytesIO
import qrcode

# Create your views here.
def index(request):
        img = qrcode.make(str("http://weixin.qq.com/r/_S3r8_nEbbQSra2Q93jr"))
        buf = BytesIO()
        img.save(buf)
        image_stream = buf.getvalue()
        response = HttpResponse(image_stream,content_type="image/png")
        #return render(request,'mytest/index.html')
        return response