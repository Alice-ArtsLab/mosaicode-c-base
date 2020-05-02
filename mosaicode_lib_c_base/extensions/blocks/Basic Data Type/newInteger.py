#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewInt class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewInteger(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (Integer)."
        self.label = "New Int"
        self.color = "189:51:164:255"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                        "name":"interger_value",
                        "label":"Integer Value",
                        "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "intege_valuer",
                            "label": "Integer Value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":1
                            }
                           ]


        self.codes["declaration"] = \
"""
    int $port[integer_value]$ = $prop[integer_value]$;
"""

# -----------------------------------------------------------------------------
