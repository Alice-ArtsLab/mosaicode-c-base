#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the IntegerAbsolute class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class IntegerAbsolute(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Integer absolute value"
        self.label = "IntegerAbsolute"
        self.color = "103:118:54:230"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"input0",
                       "label":"Integer value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"result",
                       "label":"Integer value",
                       "conn_type":"Output"}]
        self.group = "Arithmetic"

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(int value);
$label$_$id$_callback_t* $port[result]$;
int $port[result]$_size = 0;
int $label$_$id$_value0 = $prop[input0]$;
int $label$_$id$_value1 = $prop[input1]$;

void $port[input0]$(int value){
    $label$_$id$_value0  = value;
    for(int i=0 ; i < $port[result]$_size ; i++){
        // Call the stored functions
        (*($port[result]$[i]))(abs($label$_$id$_value0));
    }
}
"""

# -----------------------------------------------------------------------------
