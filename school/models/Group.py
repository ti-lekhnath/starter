from odoo import api, models, fields


class Group(models.Model):
    _name = "school.group"
    _description = "Group Information"

    name = fields.Char(string="Group Name", required=True)
    is_active = fields.Boolean(string="Is Active", default=True)
    classroom_number = fields.Char(string="Classroom Number")
    course = fields.Many2one(
        comodel_name="school.course",
        string="Course",
        required=True,
    )
