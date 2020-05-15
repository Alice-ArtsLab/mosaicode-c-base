#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Rand class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class Rand(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Rand"
        self.label = "Rand"
        self.color = "103:118:54:230"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"input0",
                       "label":"Min value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"input1",
                       "label":"Max value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"result",
                       "label":"Integer value",
                       "conn_type":"Output"}]
        self.group = "Arithmetic"
        self.properties = [{"name": "input0",
                            "label": "Min value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": sys.maxint,
                            "step": 1,
                            "value": 0},
                           {"name": "input1",
                            "label": "Max value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": sys.maxint,
                            "step": 1,
                            "value": 0}]

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(int value);
$label$_$id$_callback_t* $port[result]$;
int $port[result]$_size = 0;
int $label$_$id$_value0 = $prop[input0]$;
int $label$_$id$_value1 = $prop[input1]$;

void $port[input0]$(int value){
    $label$_$id$_value0  = value;
}

void $port[input1]$(int value){
    $label$_$id$_value1  = value;
}

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[result]$_size ; i++){
        // Call the stored functions
        (*($port[result]$[i]))($label$_$id$_value0 + \\
            (rand() % ($label$_$id$_value1 - $label$_$id$_value0)));
    }
}
"""

# -----------------------------------------------------------------------------
