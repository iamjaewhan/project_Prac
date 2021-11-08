"""
ASGI config for project_Prac project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_Prac.settings')


#ProtocolTypeRouter를 프로젝트의 루트 애플리케이션으로 설정
application = ProtocolTypeRouter({
    #http 요청을 처리하기 위한 전통적 asgi 애플리케이션
    "http":get_asgi_application(),
    #Web Socket을 처리하기 위한 핸들러
    "websocket":AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
