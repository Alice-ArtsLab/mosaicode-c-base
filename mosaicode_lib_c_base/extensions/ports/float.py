from mosaicode.model.port import Port

class Float(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.type = "mosaicode_lib_c_base.extensions.ports.string"
        self.hint = "STR"
        self.color = "#fc2300"
        self.multiple = True
        self.code = """
    $output$ = (string_callback *) realloc($output$, ($output$_size + 1 ) * sizeof(string_callback));
    $output$[$output$_size] = &$input$;
    $output$_size++;
"""
        self.var_name = "$port[name]$$block[id]$"
