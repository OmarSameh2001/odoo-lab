from odoo import models, fields, api

class HmsPatient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    birth_date = fields.Date(string="Birth Date")
    history = fields.Html(string="Medical History")
    cr_ratio = fields.Float(string="CR Ratio")
    blood_type = fields.Selection(
        [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), 
         ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')],
        string="Blood Type"
    )
    pcr = fields.Boolean(string="PCR Done")
    image = fields.Binary(string="Image")
    address = fields.Text(string="Address")
    age = fields.Integer(string="Age")

    @api.model
    def create(self, vals):
        # Custom logic during creation
        return super(HmsPatient, self).create(vals)

    def write(self, vals):
        # Custom logic during write
        return super(HmsPatient, self).write(vals)

    def unlink(self):
        # Custom logic during deletion
        return super(HmsPatient, self).unlink()

