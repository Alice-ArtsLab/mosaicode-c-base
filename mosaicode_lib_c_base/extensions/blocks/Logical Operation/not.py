#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Not class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class Not(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Not"
        self.label = "Not"
        self.color = "236:234:89:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"input0",
                       "label":"Integer value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"result",
                       "label":"Integer value",
                       "conn_type":"Output"}]
        self.group = "Logical Operation"
        self.properties = [{"name": "input0",
                            "label": "Integer value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper":1,
                            "step": 1,
                            "value": 0}]

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[result]$;
int $port[result]$_size = 0;
int $label$_$id$_value = $prop[input0]$;

void $port[input0]$(int value){
    $label$_$id$_value  = value;
    for(int i=0 ; i < $port[result]$_size ; i++){
        // Call the stored functions
        (*($port[result]$[i]))(!$label$_$id$_value);
    }
}
"""

# -----------------------------------------------------------------------------
