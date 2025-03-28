# SINCE: 2025-03-21
# SUBJECT: Building very basic sql stmt (CREATE, SELECT, INSERT ...) strings with given data (structures), mainly dicts



class QueryBuilder:

    INSERT_TPL = 'INSERT INTO {}  ({}) VALUES ({})'
    UPDATE_TPL = 'UPDATE {}  SET {} WHERE {}'
    SELECT_TPL = 'SELECT {} FROM {} WHERE {}'

    DELETE_TPL = 'DELETE FROM {} WHERE {}'

    ASSIGN_LINE = '{0} = :{0}'

    def __init__(self, tbl: str = ''):
        self.tbl = tbl

    def select (self, where:str='1', attr:list=['*']):
        """ Generating SELECT stmt - pure sting style

        Args:
            attr (list): _description_
            where (str, optional): _description_. Defaults to '1'.

        Returns:
            _type_: _description_
        """
        return self.SELECT_TPL.format(
            ', '.join(attr),
            self.tbl,
            where
        )

    def insert(self, dta: dict = {}) -> str:
        '''Generating INSERT stmt - qmark style
            INSERT INTO $entity_type (a,s,b) VALUES (?, ?, ?)
        Args:
            dta (dict, optional): _description_. Defaults to {}.

        Returns:
            str: _description_
        '''
        if len(dta) == 0:
            return ''

        return self.INSERT_TPL.format(
            self.tbl,
            ', '.join(dta.keys()),
            ', '.join(['?' for x in range(len(dta))]),
        )

    def update(self, dta: dict = {}, id_key: str = 'id') -> str:
        '''Generating UPDATE stmt - named style
            UPDATE $entity_type SET a=:a, b=:b WHERE c=:c
        Args:
            dta (dict, optional): _description_. Defaults to {}.
            id_key (str, optional): _description_. Defaults to 'id'.

        Returns:
            str: _description_
        '''
        if len(dta) == 0:
            return ''

        where = id_key + ' = :' + id_key

        where_val = dta[id_key]

        assigment_list = []
        # del( dta[id_key])

        for key in dta.keys():
            if key != id_key:
                assigment_list.append(self.ASSIGN_LINE.format(key))

        return self.UPDATE_TPL.format(self.tbl, ', '.join(assigment_list), where)

    def delete(self, where:str):
        ''' Generating DELETE stmt

        Args:
            where (str): _description_

        Returns:
            _type_: _description_
        '''
        return self.DELETE_TPL.format(
            self.tbl,
            where
        )