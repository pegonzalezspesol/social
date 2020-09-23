# Copyright 2020 Pesol - Pedro Evaristo Gonzalez Sanchez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import re

from odoo import _, api, models


class MailMail(models.Model):
    _inherit = "mail.mail"

    @api.model
    def create(self, values):
        message_id = values.get('mail_message_id', False)
        message = self.env['mail.message'].browse(message_id)
        models = [model.model
                  for model in self.env.user.company_id.model_enabled_ids]
        if message and message.model not in models:
            fake_server_id = self.env.user.company_id.fake_mail_server_id
            values['mail_server_id'] = fake_server_id
        return super(MailMail, self).create(values)
