from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pinterest_tag = fields.Char(
        related='website_id.pinterest_tag',
        string='Pinterest Tag ID',
        readonly=False,
    )

    @api.depends('website_id')
    def has_pinterest_tag(self):
        self.has_pinterest_tag = bool(self.pinterest_tag)

    def inverse_has_pinterest_tag(self):
        if not self.has_pinterest_tag:
            self.pinterest_tag = False

    has_pinterest_tag = fields.Boolean(
        string='Pinterest Tag',
        compute=has_pinterest_tag,
        inverse=inverse_has_pinterest_tag,
    )

