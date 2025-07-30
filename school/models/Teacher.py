from odoo import api, models, fields


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

    student_ids = fields.Many2many(
        comodel_name="school.student",
        string="Students",
        compute="_compute_teachers_for_student",
    )

    timing_ids = fields.One2many(
        comodel_name="school.timing",
        compute="_compute_teacher_timings",
        string="Timings",
    )

    def _compute_teachers_for_student(self):
        for teacher in self:
            teacher_groups = (
                self.env["school.timing"]
                .search([("teacher", "=", teacher.id)])
                .mapped("group")
            )

            teacher.student_ids = (
                self.env["school.student"]
                .search([("group", "in", teacher_groups.ids)])
                .mapped("id")
            )

    def _compute_teacher_timings(self):
        for teacher in self:
            teacher.timing_ids = (
                self.env["school.timing"].search([("teacher", "=", teacher.id)]).ids
            )
