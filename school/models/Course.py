from odoo import api, models, fields


class Course(models.Model):
    _name = "school.course"
    _description = "Course Information"

    name = fields.Char(string="Course Name", required=True)
    is_active = fields.Boolean(string="Is Active?")
    description = fields.Text(string="Description")

    credits = fields.Integer(string="Credits")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    group_ids = fields.One2many(
        comodel_name="school.group",
        compute="_compute_groups",
        string="Groups",
    )

    active_group_ids = fields.One2many(
        comodel_name="school.group",
        compute="_compute_active_groups",
        string="Active Groups",
    )

    @api.ondelete(at_uninstall=False)
    def _ondelete_course(self):
        for course in self:
            if course.group_ids:
                raise models.ValidationError(
                    "Cannot delete course with existing groups."
                )

    def _compute_groups(self):
        for course in self:
            course.group_ids = self.env["school.group"].search(
                [("course", "=", course.id)]
            )

    def _compute_active_groups(self):
        for course in self:
            course.active_group_ids = course.group_ids.filtered(lambda g: g.is_active)
