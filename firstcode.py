'''
说明：测试教程网-->接口测试-->8.第一个用例
'''

#用例描述
'''
获得指定节点的名字，简介，URL 及头像图片的地址。

https://www.v2ex.com/api/nodes/show.json

Method: GET
Authentication: None
接受参数：

name: 节点名（V2EX 的节点名全是半角英文或者数字）
例如：

https://www.v2ex.com/api/nodes/show.json?name=python

# 响应

{
    "id" : 90,
    "name" : "python",
    "url" : "http://www.v2ex.com/go/python",
    "title" : "Python",
    "title_alternative" : "Python",
    "topics" : 7669,
    "stars" : 4870,

        "header" : "这里讨论各种 Python 语言编程话题，也包括 Django，Tornado 等框架的讨论。这里是一个能够帮助你解决实际问题的地方。",


        "footer" : null,

    "created" : 1278683336,
    "avatar_mini" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_mini.png?m=1504279401",
    "avatar_normal" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_normal.png?m=1504279401",
    "avatar_large" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_large.png?m=1504279401"
}
'''

import requests
import unittest

class V2exAPITestCase(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.v2ex.com/api/nodes/show.json"

        self.querystring = {"name": "python"}

        self.headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "503f87cd-de3e-4460-8b38-779f27a43a6d"
        }

    def test_node_api(self):
        s=requests.request("GET",self.url,headers=self.headers,params=self.querystring).json()
        self.assertEqual(s['name'],'python')
        self.assertEqual(s['id'],90)

    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()

