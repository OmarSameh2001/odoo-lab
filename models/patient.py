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
    image = fields.Image(string="Image")
    address = fields.Text(string="Address")
    age = fields.Integer(string="Age")

    department_id = fields.Many2one('hms.department', domain=[('is_opened', '=', True)])
    doctor_ids = fields.Many2many('hms.doctors', string="Doctors", readonly=True)
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')
    ], default='undetermined')

    log_ids = fields.One2many('hms.patient.log', 'patient_id')

    @api.onchange('state')
    def _onchange_state(self):
        for rec in self:
            if rec.state:
                rec.env['hms.patient.log'].create({
                    'patient_id': rec.id,
                    'description': f"State changed to {rec.state}"
                })

    @api.constrains('pcr', 'cr_ratio')
    def _check_cr_ratio_required(self):
        for rec in self:
            if rec.pcr and not rec.cr_ratio:
                raise ValidationError("CR Ratio must be set if PCR is checked.")
    