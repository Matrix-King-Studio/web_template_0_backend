from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.weixin.views import WeixinOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class WeixinLogin(SocialLoginView):
    adapter_class = WeixinOAuth2Adapter
