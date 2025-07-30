from odoo import models, fields


class Timing(models.Model):
    _name = "school.timing"
    _description = "Class Timing Information"

    group = fields.Many2one("school.group", string="Group", required=True)
    teacher = fields.Many2one(
        comodel_name="school.teacher",
        string="Teacher",
        required=True,
    )

    start_time = fields.Float(string="Start Time")
    end_time = fields.Float(string="End Time")

    days = fields.Many2many("school.day", string="Days")

    def open_group_timing(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Groups",
            "res_model": "school.group",
            "view_mode": "list",
            "view_id": self.env.ref("school.view_school_group_tree").id,
            "target": "new",
            "context": {"create": False, "update": False},
        }

    def open_teacher_timing(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Teachers",
            "res_model": "school.teacher",
            "view_mode": "kanban",
            "view_id": self.env.ref("school.view_school_teacher_kanban").id,
            "target": "new",
            "context": {"create": False, "update": False},
        }
