from odoo import api, models, fields


class Group(models.Model):
    _name = "school.group"
    _description = "Group Information"

    name = fields.Char(string="Group Name", required=True)

    course = fields.Many2one(
        comodel_name="school.course",
        string="Course",
        required=True,
    )
