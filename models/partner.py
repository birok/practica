# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Partner(models.Model):
    _inherit = 'res.partner'

    sesion_ids = fields.Many2many('rnet.sesion', 'persona_sesion_rel', 'sesion_id',
    'partner_id', string='Sesiones' )
    instructor = fields.Boolean(string="Es instructor")
