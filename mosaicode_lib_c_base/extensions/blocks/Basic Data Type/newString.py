#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewString.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewString(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (String)."
        self.label = "New String"
        self.color = "189:51:164:255"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"string_value",
                       "label":"String Value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "string_value",
                            "label": "String Value",
                            "type": MOSAICODE_STRING,
                            "value": ""}]

# -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
"""
    char ** $port[double]$ = calloc(1, sizeof(char*));
    $port[double]$[0] = calloc(strlen($prop[value]$) + 1, sizeof(char));
    *($port[double]$) = \"$prop[value]$\";
"""

# -----------------------------------------------------------------------------
