from odoo import api, models, fields


class Student(models.Model):
    _name = "estate.student"
    _description = "Student Record"

    profile = fields.Image(string="Profile Image")
    name = fields.Char(string="Name", required=True)
    score = fields.Float(string="Score", required=True)
    dob = fields.Date(string="Date of Birth", required=True)
    gender = fields.Selection([("Male", "male"), ("Female", "female")])
    age = fields.Integer(compute="_compute_age", string="Age", store=True)

    @api.depends("dob")
    def _compute_age(self):
        if not self.dob:
            self.age = 0
        if self.dob:
            today = fields.Date.today()
            self.age = int(
                today.year
                - self.dob.year
                - ((today.month, today.day) < (self.dob.month, self.dob.day))
            )

    def logger(self):
        return True
