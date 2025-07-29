from odoo import api, models, fields
from datetime import date, timedelta


class Student(models.Model):
    _name = "school.student"
    _description = "Student Information"

    profile = fields.Image(string="Profile Image")
    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        inverse="_inverse_age",
        store=True,
    )

    score = fields.Float(string="Score", required=True)
    gender = fields.Selection([("Male", "male"), ("Female", "female")])
    dob = fields.Date(string="Date of Birth", required=True)
    roll_number = fields.Char(string="Roll Number")
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone")

    teacher_ids = fields.Many2many(
        comodel_name="school.teacher",
        string="Teachers",
        compute="_compute_teachers_for_student",
    )

    group = fields.Many2one("school.group", string="Group", required=True)
    status = fields.Selection(
        [
            ("unknown", "Unknown"),
            ("enrolled", "Enrolled"),
            ("graduated", "Graduated"),
            ("dropped", "Dropped"),
        ],
        string="Unknown",
    )

    @api.depends("group")
    def _compute_teachers_for_student(self):
        for student in self:
            student.teacher_ids = (
                self.env["school.timing"]
                .search([("group", "=", student.group.id)])
                .mapped("teacher")
            )

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

    def calculate_dob_from_age(self):
        if not self.age or self.age <= 0:
            self.dob = False
        else:
            today = fields.Date.today()
            dob = today - timedelta(days=self.age * 365)
            self.dob = date(dob.year, self.dob.month, self.dob.day)

    def check_status_validity(self):
        self.status = self.env.context["student_status"]
        return self

    @api.depends("dob")
    def _compute_age(self):
        for st in self:
            st.calculate_age_from_dob()

    def _inverse_age(self):
        for st in self:
            st.calculate_dob_from_age()

    @api.model
    def write(self, vals):
        if status := vals.get("status"):
            ...
            # self.check_status_validity(status)
        return super().write(vals)

    def hello(self):
        return "Hello, I am a student!"
