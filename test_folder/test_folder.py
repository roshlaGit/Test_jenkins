class testme:
    def __init__(self,buildno,MY_GLOBAL_KEY):
        self.buildno = buildno
        self.MY_GLOBAL_KEY = MY_GLOBAL_KEY
    
    def concat(self):
        return self.buildno.tostring() + self.MY_GLOBAL_KEY.tostring()