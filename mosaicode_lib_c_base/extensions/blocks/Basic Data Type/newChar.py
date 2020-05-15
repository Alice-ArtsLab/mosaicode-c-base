#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewChar.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewChar(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (Char)."
        self.label = "NewChar"
        self.color = "78:87:130:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.char",
                       "name":"char_value",
                       "label":"Char value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "char_value",
                            "label": "Char value",
                            "type": MOSAICODE_CHAR,
                            "value": ""}]

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(char value);
$label$_$id$_callback_t* $port[char_value]$;
int $port[char_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[char_value]$_size ; i++){
        // Call the stored functions
        (*($port[char_value]$[i]))(\"$prop[char_value]$\");
    }
}
"""
