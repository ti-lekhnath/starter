from odoo import models, fields


class Student(models.Model):
    _name = "school.student"
    _description = "Student Information"

    profile = fields.Image(string="Profile Image")
    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age", required=True)
    score = fields.Float(string="Score", required=True)
    gender = fields.Selection([("Male", "male"), ("Female", "female")])
    age = fields.Integer(string="Age", store=True)
    roll_number = fields.Char(string="Roll Number")

    course = fields.Many2one('school.course', string="Course", required=True)


