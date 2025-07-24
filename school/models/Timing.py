
from odoo import models, fields


class Timing(models.Model):
    _name = "school.timing"
    _description = "Class Timing Information"

    group = fields.Char(string="Group", required=True)
    teacher = fields.Char(string="Teacher", required=True)
