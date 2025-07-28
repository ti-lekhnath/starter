from odoo import models, fields


class Course(models.Model):
    _name = "school.course"
    _description = "Course Information"

    name = fields.Char(string="Course Name", required=True)
    is_active = fields.Boolean(string="Is Active?")
    description = fields.Text(string="Description")

    credits = fields.Integer(string="Credits")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    group_ids = fields.One2many("school.group", "course", string="Groups")
