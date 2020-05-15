#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatToInteger class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class FloatToInteger(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Float to integer"
        self.label = "FloatToInteger"
        self.color = "167:167:143:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"input0",
                       "label":"Float value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"result",
                       "label":"Integer value",
                       "conn_type":"Output"}]
        self.group = "Conversion"
        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[result]$;
int $port[result]$_size = 0;
float $label$_$id$_value0 = 0;

void $port[input0]$(float value){
    $label$_$id$_value0  = value;
}

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[result]$_size ; i++){
        // Call the stored functions
        (*($port[result]$[i]))((int)$label$_$id$_value0);
    }
}
"""

# -----------------------------------------------------------------------------
