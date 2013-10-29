# -*- coding: utf8 -*-

# python-diana - Python API for Diana - A Free Meteorological Visualisation Tool
#
# Copyright (C) 2013 met.no
#
# Contact information:
# Norwegian Meteorological Institute
# Box 43 Blindern
# 0313 OSLO
# NORWAY
# email: diana@met.no
#
# This file is part of python-diana
#
# python-diana is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# python-diana is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-diana; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

### TODO: Obtain available options by parsing the relevant sections in a
### specified input file.

class PlotCommand:

    def __init__(self, **kwargs):

        self.options = {}
        self.order = []
        
        for key, value in kwargs.items():
            self.setOption(key, value)

    def _add_command(self, option, value):

        if option not in self.options:
            self.order.append(option)
        
        self.options[option] = value
    
    def getOptions(self):

        return self.available.keys()

    def getAvailable(self, option):

        return self.available.get(option)
    
    def setOption(self, option, value):
    
        available = self.available.get(option)

        # If no information is supplied then the value is a free choice.
        if available is None:
            self._add_command(option, value)
        # Otherwise, the value must be in the sequence found.
        elif available and value in available:
            self._add_command(option, value)

    def text(self):
    
        pieces = [self.command]
        for option in self.order:
            pieces.append(option + "=" + str(self.options[option]))

        return " ".join(pieces)


class Field(PlotCommand):

    command = "FIELD"

    available = {"model": None,
                 "plot": None,
                 "plottype": ("contour", "contour2", "value", "symbol",
                              "alpha_shade", "alarm_box", "fill_cell", "wind",
                              "wind_temp_fl", "wind_value", "vector", "frame",
                              "direction")}


class Map(PlotCommand):

    command = "MAP"

    available = {"backcolour": None,
                 "map": ("Gshhs-Auto", "Euro1", "Euro2", "Euro3", "Fin",
                         "Norkart", "Norkart2", "Regioner", "Banker",
                         "Banker1", "Banker2", "Banker_test", "MinQNH",
                         "FIR", "High.Seas", "skredvarsling", "NVE_flom",
                         "Europa-TVkart", "Wvs-Auto", "Kommuner", "Fylker",
                         "Riksgrense", "Kyst", "Høyde", "Vann", "Vei",
                         "Vei2", "Vei3", "Bane", "World", "Gebco.world",
                         "Vanlig", "Norsea", "Simra_fly", "Flystriper",
                         "Approach-area"),
                 "land": ("on", "off"),
                 "land.colour": None}


class Area(PlotCommand):

    command = "AREA"
    
    available = {"name": ("Europa", "Norge", "Trøndelag", "N-Norge",
                          "S-Norge", "Norge.20W", "VA-Norge", "VV-Norge",
                          "VNN-Norge", "Atlant", "SIGkart", "NyttSigkart4",
                          "SWIkart", "N.halvkule", "S.halvkule",
                          "S.halvkule+180", "N.halvkule-90", "N.halvkule+90",
                          "Hirlam-grid", "Merkator", "Geografisk", "Globalt",
                          "Infosat.1", "Analyse_min", "ENHF", "ENST", "ENHV",
                          "ENNK", "Norge.smal", "Ishav", "N-Europa",
                          "N.halvkule+65", "Troms", "H10-stor", "H10-liten",
                          "Skandinavia", "proj_hirlam", "proj_bonne",
                          "proj_van_der_grinten", "proj_eqc", "proj_obtran",
                          "proj_lambert", "EPSG-4326", "EPSG-32661",
                          "EPSG-32761", "epsg:900913", "epsg:3575")}


class Label(PlotCommand):

    name = "LABEL"

    available = {"text": None,
                 "tcolour": None,
                 "bcolour": None,
                 "fcolour": None,
                 "anno": None,
                 "halign": ("left", "right", "center"),
                 "valign": ("top", "bottom", "center"),
                 "polystyle": ("fill", "border", "both", "none"),
                 "margin": None,
                 "fontname": None,
                 "fontface": None,
                 "fontsize": None}
