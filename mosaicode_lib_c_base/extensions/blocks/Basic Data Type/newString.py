#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewString.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewString(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (String)."
        self.label = "NewString"
        self.color = "78:87:130:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"string_value",
                       "label":"String value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "string_value",
                            "label":"String value",
                            "type": MOSAICODE_STRING,
                            "value": ""}]

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(char * value);
$label$_$id$_callback_t* $port[string_value]$;
int $port[string_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[string_value]$_size ; i++){
        // Call the stored functions
        (*($port[string_value]$[i]))(\"$prop[string_value]$\");
    }
}
"""
