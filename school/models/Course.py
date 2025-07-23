from odoo import models, fields


class Course(models.Model):
    _name = "school.course"
    _description = "Course Information"

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Description")
