# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    reason_id = fields.Many2one(
        "account.move.refund.reason", string="Refund Reason", readonly=True
    )

    def _select(self):
        select_str = super()._select()
        return "%s, move.reason_id AS reason_id" % select_str
