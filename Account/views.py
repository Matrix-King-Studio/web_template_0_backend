from allauth.socialaccount.providers.weixin.client import WeixinOAuth2Client
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class WeixinLogin(SocialLoginView):
    adapter_class = WeixinOAuth2Adapter
    callback_url = "https://www.template.matrix-studio.top/"
    client_class = WeixinOAuth2Client
