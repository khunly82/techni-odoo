from odoo import models, fields, api

class Game(models.Model):
    _name = 'demo.games' # table: demo_games
    _description = 'Games'

    name = fields.Char(string='Nom', required=True)
    release_date = fields.Date(string='Date de sortie', required=False)
    genre = fields.Selection([
        ('RPG', 'RPG'),
        ('FPS', 'FPS'),
        ('RTS', 'RTS'),
        ('PUZZLE GAME', 'Puzzle Game'),
        ('PLATEFORM', 'Plateforme')
    ], string='Genre')
    multi = fields.Boolean(string='Multi', required=True, default=True)
    rating = fields.Integer(string='Note')

    developer_id = fields.Many2one('demo.developers', string='Dev')
    tag_ids = fields.Many2many('demo.tags', string='Tags')

    tags_len = fields.Integer(compute='_compute_tags_len', store=False)

    @api.depends('tag_ids')
    def _compute_tags_len(self):
        self.tags_len = len(self.tag_ids)