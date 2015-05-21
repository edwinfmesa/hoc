class SymTab:

    def __init__(self, label, parent=None):
        self.name
        self.entries = {}
        self.parent = parent
        if self.parent != None:
            self.parent.children.append(self)
        self.children = []
    
    def add(self, name, value): # agrego simbolo
        self.entries[name] = value

    def get(self, name): # o me retorna el simbolo no me retorna nada
        if self.entries.has_key(name):
            return self.entries[name]
        else:
            if self.parent != None:
                return self.parent.get(name)
            else:
                return None


program_tab = SymTab('Program')

function_tab = SymTabl('Function_name',program )