#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the MinInt class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class MinInt(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Min Integer value."
        self.label = "MinInteger"
        self.color = "78:87:130:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"integer_value",
                       "label":"Integer value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(int value);
$label$_$id$_callback_t* $port[integer_value]$;
int $port[integer_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[integer_value]$_size ; i++){
        // Call the stored functions
        // Needs limits.h
        (*($port[integer_value]$[i]))(INT_MIN);
    }
}
"""

# -----------------------------------------------------------------------------
