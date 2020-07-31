import fdb
import time

class FBprodutos():
    def __init__(self, cur):
        self.cur = cur
        
        self.COLUMNS = [column[0].strip() for column in self.cur.execute("""SELECT rdb$field_name 
                                                                        FROM rdb$relation_fields 
                                                                        WHERE rdb$relation_name=\'PRODUTO\' 
                                                                        ORDER BY rdb$field_position""").fetchall()]
        
        self.rowsCount = self.getRowsCount()
                

    def getPaged(self, page = 1, limit = 100):
        data = {}
        data['columns'] = self.COLUMNS
        data['data'] = self.cur.execute(f"SELECT FIRST {limit} SKIP {(page - 1) * limit} * FROM PRODUTO").fetchall()
        return data
    
    def getRowsCount(self):        
        self.rowsCount = self.cur.execute(f"SELECT COUNT(*) FROM PRODUTO").fetchone()[0]
        
        return self.rowsCount