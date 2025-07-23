from odoo import models, fields


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher Information"

    name = fields.Char(string="Teacher Name", required=True)
    employee_id = fields.Char(string="Employee ID")
    course_id = fields.Many2one('school.course', string="Course", required=True)
