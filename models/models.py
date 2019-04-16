# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Curso(models.Model):
    _name = 'rnet.curso'

    name = fields.Char(string="Nombre del curso", required=True, size =50)
    descripcion = fields.Text(string="Descripción")
    responsable_id = fields.Many2one('res.users',
        ondelete = 'set null', string = "Responsable", index=True)
    sesion_ids = fields.One2many('rnet.sesion', 'curso_id', string="Sesiones")


class Sesion(models.Model):
    _name = 'rnet.sesion'

    name = fields.Char(string="Nombre", required=True, default='/')
    inicio = fields.Date()
    duracion = fields.Float(string="Duracion", digits=(6,2), help="Duración en días")
    asientos = fields.Integer(string="Asientos")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    curso_id = fields.Many2one('rnet.curso', ondelete='cascade',string="Curso",
    required=True)
    asistente_ids = fields.Many2many('res.partner','persona_sesion_rel','partner_id',
    'sesion_id',  string="Asistentes")
