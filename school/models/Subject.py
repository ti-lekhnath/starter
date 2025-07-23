from odoo import models, fields


class Subject(models.Model):
    _name = "school.subject"
    _description = "Subject Information"

    name = fields.Char(string="Subject Name", required=True)
    course_id = fields.Many2one('school.course', string="Course", required=True)
    teacher_id = fields.Many2one('school.teacher', string="Subject Teacher")
