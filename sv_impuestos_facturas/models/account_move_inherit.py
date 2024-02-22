from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'


    def action_post(self):
        moves_with_payments = self.filtered('payment_id')
        other_moves = self - moves_with_payments

        if other_moves.move_type not in ('in_invoice', 'in_refund', 'in_receipt'):
            count_lines_without_tax = sum(1 for line in self.invoice_line_ids if not line.tax_ids)

            if count_lines_without_tax > 0:
                raise ValidationError("Falta el impuesto en una línea de la factura")

            else:
                if moves_with_payments:
                    moves_with_payments.payment_id.action_post()
                if other_moves:
                    other_moves._post(soft=False)
                return False
        else:
            if moves_with_payments:
                moves_with_payments.payment_id.action_post()
            if other_moves:
                other_moves._post(soft=False)
            return False
