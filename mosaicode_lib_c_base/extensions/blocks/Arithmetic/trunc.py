#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Trunc class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class Trunc(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Trunc value"
        self.label = "Trunc"
        self.color = "103:118:54:230"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"input0",
                       "label":"Float value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"result",
                       "label":"Float value",
                       "conn_type":"Output"}]
        self.group = "Arithmetic"

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[result]$;
int $port[result]$_size = 0;
float $label$_$id$_value0;

void $port[input0]$(float value){
    $label$_$id$_value0  = value;
    for(int i=0 ; i < $port[result]$_size ; i++){
        // Call the stored functions
        (*($port[result]$[i]))(truncf($label$_$id$_value0));
    }
}
"""

# -----------------------------------------------------------------------------
