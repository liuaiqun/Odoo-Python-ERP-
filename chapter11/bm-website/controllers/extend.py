from odoo import http
#from odoo.addons.bm-website.controllers.main import Main
#python  不支持减号作为模块的目录名和文件名， 使用如下方法绕过这一限制
import importlib  
Main = importlib.import_module("odoo.addons.bm-website.controllers.main").Main

class MainExtended(Main):
    @http.route()
    def hello(self, name=None, **kwargs):
        response = super(MainExtended, self).hello()
        response.qcontext['name'] = name
        return response