#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewFloat class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewFloat(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (Float)."
        self.label = "New Float"
        self.color = "189:51:164:255"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"float_value",
                       "label":"Float Value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "float_value",
                            "label": "Float Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }]

        self.codes["declaration"] = \
"""
    float $port[float_value]$ = $prop[float_value]$;
"""

# -----------------------------------------------------------------------------
