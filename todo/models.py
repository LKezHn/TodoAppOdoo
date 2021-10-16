from odoo import models, fields

class Todo(models.Model):
    _name = "todo.app"

    name = fields.Char("Nombre")
    description = fields.Text("Descripcion")
    status = fields.Selection(selection=[("por_hacer", "Por Hacer"), ("completado","Completado")], field_name = "Estado")