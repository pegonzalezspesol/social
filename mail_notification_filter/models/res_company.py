# Copyright 2020 Pesol - Pedro Evaristo Gonzalez Sanchez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models,fields


class MailMail(models.Model):
    _inherit = "res.company"

    def _get_default_fake_server(self):
        return self.env.ref('mail_notification_filter.ir_mail_server_fake')

    fake_mail_server_id = fields.Many2one(
        comodel_name="ir.mail_server",
        string="Disabled Mail Server",
        default=_get_default_fake_server)

    model_enabled_ids = fields.Many2many(
        comodel_name="ir.model", relation="res_company_mail_models",
        column1="company_id", column2="model_id",
        string="Allowed Models")
