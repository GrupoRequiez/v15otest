from odoo import fields, models


class Website(models.Model):
    _inherit = 'website'

    pinterest_tag = fields.Char('Pinterest Tag')
