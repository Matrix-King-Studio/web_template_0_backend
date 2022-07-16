import requests
from rest_framework.decorators import api_view

from web_template_0 import settings


@api_view(["GET"])
def wx_login(request):
    # 微信扫码登录接口
    params = {
        "appid": settings.WeiXinWebAppID,
        "appsecret": settings.WeiXinWebAppSecret,
        "code": request.GET.get("code"),
    }
    res = requests.get("https://api.weixin.qq.com/sns/oauth2/access_token", params=params)
    res = res.json()
    print(f"res 1: {res}")
    access_token = res["access_token"]
    openid = res["openid"]
    # 获取用户信息
    params = {
        "access_token": access_token,
        "openid": openid,
    }
    res = requests.get("https://api.weixin.qq.com/sns/userinfo", params=params)
    res = res.json()
    print(f"res 2: {res}")
    return res
