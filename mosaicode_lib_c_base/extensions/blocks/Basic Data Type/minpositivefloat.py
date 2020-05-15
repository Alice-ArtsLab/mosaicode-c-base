#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the MinPositiveFloat class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class MinPositiveFloat(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Min positive float value."
        self.label = "MinPositiveFloat"
        self.color = "78:87:130:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"float_value",
                       "label":"Float value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[float_value]$;
int $port[float_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[float_value]$_size ; i++){
        // Call the stored functions
        // Needs limits.h
        (*($port[float_value]$[i]))(FLT_MIN);
    }
}
"""

# -----------------------------------------------------------------------------
