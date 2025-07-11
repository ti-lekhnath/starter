from odoo import models, fields


class Course(models.Model):
    _name = 'estate.course'
    _description = 'Course Information'

    name = fields.Char(string='Name', required=True)
