from sqlalchemy import create_engine

class DBConnectionHandler:
    """"
    Sqlalchemy database connection 
    """

    def __init__(self, db_config):
        self.__connction_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
        Return connection engine
        params: None
        return: engine
        """
        engine = create_engine(self.__connction_string)
        return engine


