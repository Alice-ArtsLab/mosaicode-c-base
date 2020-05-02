from mosaicode.model.port import Port

class Integer(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.type = "mosaicode_lib_c_base.extensions.ports.integer"
        self.hint = "INT"
        self.color = "#fc2300"
        self.multiple = True
        self.code = """
    $output$ = realloc($output$, ($output$_size + 1 ) * sizeof($input$));
    $output$[$output$_size] = &$input$;
    $output$_size++;
"""
        self.var_name = "$port[name]$$block[id]$"
