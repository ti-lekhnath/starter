from odoo import models, fields


class Course(models.Model):
    _name = "estate.course"
    _description = "Course Information"

    string = fields.Char(string="Name")
    decimal = fields.Float(string="Percent")
    boolean = fields.Boolean(string="YES/NO", default=True)
    integer = fields.Integer(string="Integer")
    binary = fields.Binary(string="Binary")
    html = fields.Html(string="HTML")
    image = fields.Image(string="Image")
    text = fields.Text(string="Text")
    date = fields.Date(string="Date")
    datetime = fields.Datetime(string="Datetime")

    selection = fields.Selection(
        [("One", "one"), ("Two", "two"), ("Three", "three")],
        string="Selection",
        required=False,
    )


    # advance
    # monetary = fields.Monetary(currency_field="us", string="Monetary")
    # many2one = fields.Many2one()
    # one2many = fields.One2many()
    # many2many = fields.Many2many()
    # command = fields.Command()
    # reference = fields.Reference()
    # many2one_reference = fields.Many2oneReference()
