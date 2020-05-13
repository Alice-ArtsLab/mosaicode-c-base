#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewFloat class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewFloat(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (Float)."
        self.label = "NewFloat"
        self.color = "189:51:164:255"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"float_value",
                       "label":"Float Value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "float_value",
                            "label": "Float Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }]

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[float_value]$;
int $port[float_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[float_value]$_size ; i++){
        // Call the stored functions
        (*($port[float_value]$[i]))($prop[float_value]$);
    }
}
"""

# -----------------------------------------------------------------------------
