# Copyright 2020 Pesol
#   - Pedro Gonzalez <pedro.gonzalez@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Mail Notification Filter",
    "summary": "Filter notifications by model. Wildcard by model to allow the sending",
    "version": "13.0.1.0.0",
    "category": "Social Network",
    "website": "https://github.com/OCA/social/",
    "author": "Pesol, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["mail"],
    "data": ["views/res_company_view.xml",
             "data/ir_mail_server_fake.xml", ],
    "development_status": "Beta",
    "maintainers": ["pedro.gonzalez@pesol.es"],
}
