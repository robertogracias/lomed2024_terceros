from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Campo relacionado para mostrar las órdenes de trabajo
    workorder_ids = fields.Many2many('mrp.workorder', string='Ordenes de trabajo', compute='_compute_workorder_ids')

    @api.depends('order_line')
    def _compute_workorder_ids(self):
        for order in self:
            if order.state == 'sale':
                workorders = self.env['mrp.workorder'].search([('production_id.origin', '=', order.name)])
                order.workorder_ids = workorders

            else:
                order.workorder_ids = False
