import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from Account.models import Account
from web_template_0 import settings


@api_view(["GET"])
def wx_login(request):
	# 微信扫码登录接口
	params = {
		"appid": settings.WeiXinWebAppID,
		"secret": settings.WeiXinWebAppSecret,
		"code": request.GET.get("code"),
		"grant_type": "authorization_code"
	}
	res = requests.get("https://api.weixin.qq.com/sns/oauth2/access_token", params=params)
	res = res.json()
	access_token = res["access_token"]
	openid = res["openid"]
	# 获取用户信息
	params = {
		"access_token": access_token,
		"openid": openid,
	}
	res = requests.get("https://api.weixin.qq.com/sns/userinfo", params=params)
	res = res.json()
	# 判断用户是否存在
	account = Account.objects.filter(openid=openid).first()
	if not account:
		# 如果用户不存在，则创建用户
		account = Account.objects.create(
			openid=openid,
			unionId=res["unionid"],
			nickname=res["nickname"],
			headImgUrl=res["headimgurl"]
		)
	# 根据用户信息生成JWT token
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	payload = jwt_payload_handler(account)
	token = jwt_encode_handler(payload)
	# 返回用户信息 + token
	return Response({
		"token": token,
		"account": {
			"openid": account.openid,
			"nickname": account.nickname,
			"headImgUrl": account.headImgUrl
		}
	})
