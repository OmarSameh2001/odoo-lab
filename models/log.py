from odoo import models, fields
from datetime import datetime

class PatientLog(models.Model):
    _name = 'hms.patient.log'
    _description = 'Patients Logs'

    patient_id = fields.Many2one('hms.patient')
    created_by = fields.Many2one('res.users', default=lambda self: self.env.user)
    date = fields.Datetime(default=datetime.now)
    description = fields.Text()
