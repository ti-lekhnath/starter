from odoo import models, fields


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher Information"

    name = fields.Char(string="Teacher Name", required=True)
    subject = fields.Char(string="Subject", required=True)
    profile = fields.Binary(string="Profile Image")
    gender = fields.Selection([("Male", "male"), ("Female", "female")])
    dob = fields.Date(string="Date of Birth", required=False)
    age = fields.Integer(string="Age")

    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    joined_at = fields.Date(string="Joining Date")

    timing_ids = fields.One2many(
        comodel_name="school.timing",
        inverse_name="teacher",
        string="Timings",
    )

    partner_id = fields.Many2one("res.partner", string="Address")
