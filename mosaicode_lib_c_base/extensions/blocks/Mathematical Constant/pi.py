#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Euler class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class PI(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "PI constant"
        self.label = "PI"
        self.color = "0:0:0:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"float_value",
                       "label":"Float value",
                       "conn_type":"Output"}]
        self.group = "Mathematical Constant"

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[float_value]$;
int $port[float_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[float_value]$_size ; i++){
        // Call the stored functions
        (*($port[float_value]$[i]))(acos(-1.0));
    }
}
"""

# -----------------------------------------------------------------------------
