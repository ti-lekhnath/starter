from odoo import models, fields


class Student(models.Model):
    _name = 'estate.student'
    _description = 'Student Record'

    name = fields.Char(string='Name', required=True)
