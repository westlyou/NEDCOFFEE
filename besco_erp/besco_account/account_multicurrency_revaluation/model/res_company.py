# -*- coding: utf-8 -*-
from openerp import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    revaluation_loss_account_id = fields.Many2one(
        comodel_name='account.account',
        string='Revaluation loss account',
        domain=[('type', '=', 'other')],
    )
    revaluation_gain_account_id = fields.Many2one(
        comodel_name='account.account',
        string='Revaluation gain account',
        domain=[('type', '=', 'other')],
    )
    revaluation_analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Revaluation Analytic account'
    )
    
    provision_bs_loss_account_id = fields.Many2one(
        comodel_name='account.account',
        string='Provision B.S loss account',
        domain=[('type', '=', 'other')]
    )
    provision_bs_gain_account_id = fields.Many2one(
        comodel_name='account.account',
        string='Provision B.S gain account',
        domain=[('type', '=', 'other')]
    )
    provision_pl_loss_account_id = fields.Many2one(
        comodel_name='account.account',
        string='Provision P&L loss account',
        domain=[('type', '=', 'other')]
    )
    provision_pl_gain_account_id = fields.Many2one(
        comodel_name='account.account',
        string='Provision P&L gain account',
        domain=[('type', '=', 'other')]
    )
    provision_pl_analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Provision P&L Analytic account'
    )
    default_currency_reval_journal_id = fields.Many2one(
        comodel_name='account.journal',
        string='Currency gain & loss Default Journal',
        domain=[('type', '=', 'general')]
    )
    reversable_revaluations = fields.Boolean(
        string='Reversable Revaluations',
        help="Revaluations entries will be created "
             "as \"To Be Reversed\".",
        default=True,
    )
