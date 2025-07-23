from odoo import api,models, fields


class Student(models.Model):
    _name = "school.student"
    _description = "Student Information"

    profile = fields.Image(string="Profile Image")
    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    score = fields.Float(string="Score", required=True)
    gender = fields.Selection([("Male", "male"), ("Female", "female")])
    dob = fields.Date(string="Date of Birth", required=True)
    roll_number = fields.Char(string="Roll Number")

    course = fields.Many2one('school.course', string="Course", required=True)

    def calculate_age_from_dob(self):
        if not self.dob:
            self.age = 0
        if self.dob:
            today = fields.Date.today()
            self.age = int(
                today.year
                - self.dob.year
                - ((today.month, today.day) < (self.dob.month, self.dob.day))
            )

    @api.depends("dob")
    def _compute_age(self):
        for st in self:
            st.calculate_age_from_dob()
