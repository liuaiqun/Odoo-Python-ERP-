from odoo import http
#from odoo.addons.bm-website.controllers.main import Main
#python  ��֧�ּ�����Ϊģ���Ŀ¼�����ļ����� ʹ�����·����ƹ���һ����
import importlib  
Main = importlib.import_module("odoo.addons.bm-website.controllers.main").Main

class MainExtended(Main):
    @http.route()
    def hello(self, name=None, **kwargs):
        response = super(MainExtended, self).hello()
        response.qcontext['name'] = name
        return response