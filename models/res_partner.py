from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient', string="Related Patient")
    vat = fields.Char(string='Tax ID', required=True)
    @api.constrains('related_patient_id')
    def _check_related_patient_email(self):
        for partner in self:
            if partner.related_patient_id:
                customers = self.search([
                    ('id', '!=', partner.id),
                    ('email', '=', partner.related_patient_id.email)
                ])
                if customers:
                    raise ValidationError("This patient's email is already linked to another customer.")
