from rest_framework.response import Response
from rest_framework.views import APIView


class TestVersion(APIView):

    def get(self, request, *args, **kwargs):
        print("版本：", kwargs['version'])
        print("版本控制信息：", request.versioning_scheme)
        if request.version == 'v1':
            # 处理版本v1的业务逻辑
            return Response("这是版本v1的信息")
        # 处理版本v2的业务逻辑
        return Response("这是版本v2的信息")
