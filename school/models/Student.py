from odoo import models, fields


class Student(models.Model):
    _name = "school.student"
    _description = "Student Information"

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age", required=True)
    roll_number = fields.Char(string="Roll Number")

    course_id = fields.Many2one('school.course', string="Course", required=True)


