from odoo import models, fields


class Timing(models.Model):
    _name = "school.timing"
    _description = "Class Timing Information"

    group = fields.Char(string="Group", required=True)
    teacher = fields.Char(string="Teacher", required=True)
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")

    days = fields.Many2many("school.day", string="Days")
