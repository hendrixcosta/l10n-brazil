# -*- coding: utf-8 -*-
# Copyright 2016 KMEE - Luis Felipe Miléo <mileo@kmee.com.br>
# Copyright 2016 KMEE - Hendrix Costa <hendrix.costa@kmee.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import fields, models

_logger = logging.getLogger(__name__)

try:
    from pybrasil.feriado.constantes import (
        TIPO_FERIADO, ABRANGENCIA_FERIADO,
    )
except ImportError:
    _logger.info('Cannot import pybrasil')


class ResourceCalendarLeave(models.Model):
    _inherit = 'resource.calendar.leaves'

    country_id = fields.Many2one(
        comodel_name='res.country',
        string='País',
        related='calendar_id.country_id',
    )

    state_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Estado',
        related='calendar_id.state_id',
        domain="[('country_id','=',country_id)]",
        readonly=True,
    )

    l10n_br_city_id = fields.Many2one(
        comodel_name='res.city',
        string='Município',
        related='calendar_id.l10n_br_city_id',
        domain="[('state_id','=',state_id)]",
        readonly=True,
    )

    leave_type = fields.Selection(
        string=u'Tipo',
        selection=[item for item in TIPO_FERIADO.items()],
    )

    abrangencia = fields.Selection(
        string=u'Abrangência',
        selection=[item for item in ABRANGENCIA_FERIADO.items()],
    )
