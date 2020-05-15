#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the IntegerToFloat class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class CharToString(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Char to string"
        self.label = "CharToString"
        self.color = "167:167:143:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.char",
                       "name":"input0",
                       "label":"Char value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"result",
                       "label":"String value",
                       "conn_type":"Output"}]
        self.group = "Conversion"

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(char value);
$label$_$id$_callback_t* $port[result]$;
int $port[result]$_size = 0;
char $label$_$id$_value0[2];
$label$_$id$_value0[1] = \'\\0\';

void $port[input0]$(char value){
    $label$_$id$_value0[0]  = value;
}

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[result]$_size ; i++){
        // Call the stored functions
        (*($port[result]$[i]))($label$_$id$_value0);
    }
}
"""

# -----------------------------------------------------------------------------
