# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class WebsiteSaleShippingOptions(models.Model):
    _name = 'shipping.options'

    name = fields.Char(required=True)
    website_published = fields.Boolean(
        string='Available in the website', copy=False)

