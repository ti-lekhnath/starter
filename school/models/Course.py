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

    group_ids = fields.One2many("school.group", "course", string="Groups")


    @api.ondelete(at_uninstall=False)
    def _ondelete_course(self):
        for course in self:
            if course.group_ids:
                raise models.ValidationError(
                    "Cannot delete course with existing groups."
                )
