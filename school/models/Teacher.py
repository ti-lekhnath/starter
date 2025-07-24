from odoo import models, fields


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher Information"

    name = fields.Char(string="Teacher Name", required=True)
    subject = fields.Char(string="Subject", required=True)
    profile = fields.Binary(string="Profile Image")

    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    joined_at = fields.Date(string="Joining Date")
