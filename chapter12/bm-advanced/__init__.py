# -*- coding: utf-8 -*-

from . import controllers
from . import models

from odoo import api, SUPERUSER_ID
def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    action = env.ref("bug-manage.action_window")
    action.write({'view_mode': "tree,form"})
