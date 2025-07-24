from odoo import models, fields


class Day(models.Model):
    _name = "school.day"
    _description = "Day of the Week"

    name = fields.Selection(
        [
            ("mon", "Monday"),
            ("tue", "Tuesday"),
            ("wed", "Wednesday"),
            ("thu", "Thursday"),
            ("fri", "Friday"),
            ("sat", "Saturday"),
            ("sun", "Sunday"),
        ],
        string="Day",
        required=True,
        unique=True,
    )
