"""将接口的字典类型转为json"""

from rest_framework.renderers import JSONRenderer

class MyJsonRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        """
        需要做的是将data的值添加code/msg/data
            'code':0,
            'msg':'成功',
            'data':data
        """
        #
        try:
            msg = data.pop('msg')
        except:
            msg = '成功'

        try:
            code = data.pop('code')
        except:
            code = 0



        try:
            result = data['data']
        except:
            result = data



        res = {
            'code':0,
            'msg': msg,
            'data':data
        }
        return super().render(res)