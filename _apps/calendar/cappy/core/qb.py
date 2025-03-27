# SINCE: 2025-03-21
# Building  very basic sql query (CREATE, SELECT, INSERT ...) strings with given data (structures), mainly dicts
# SUBJECT: This is for (my) learning purposes only - I am not acting in a strict way (coding style etc.) here


class QueryBuilder:

    INSERT_TPL = "INSERT INTO {}  ({}) VALUES ({})"
    
    
    UPDATE_TPL = "UPDATE {}  SET {} WHERE {}"
    
    ASSIGN_LINE = "{0} = :{0}"

    def __init__(self, ety: str = ""):
        self.entity = ety

    def insert(self, dta: dict = {}) -> str:
        """ Generating INSERT stmt - qmark style

        Args:
            dta (dict, optional): _description_. Defaults to {}.

        Returns:
            str: _description_
        """
        if len(dta) == 0:
            return ''

        return self.INSERT_TPL.format(
            self.entity,
            ", ".join(dta.keys()),
            ", ".join(["?" for x in range(len(dta))]),
        )

    def update(self, dta: dict = {}, id_key='id') -> str:
        """ Generating UPDATE stmt - named style 

        Args:
            dta (dict, optional): _description_. Defaults to {}.
            id_key (str, optional): _description_. Defaults to 'id'.

        Returns:
            str: _description_
        """
        if len(dta) == 0:
            return ''
        
        where = id_key + ' = :' + id_key
        where_val = dta[id_key]
        assigment_list = []
        #del( dta[id_key])
        
        for key in dta.keys():
            if key != id_key:
                assigment_list.append(self.ASSIGN_LINE.format(key))

    

        return self.UPDATE_TPL.format(
            self.entity,
            ", ".join(assigment_list),
            where
        )
