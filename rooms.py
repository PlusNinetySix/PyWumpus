class RoomInfo(object):    
    def __init__(self, roomnum, adj, desc):
        self.roomnum = roomnum
        self.adj = adj
        self.desc = desc
        self.wumpus = False
        self.spider = False
        self.pit = False
        self.arrow = False
        
    def hasWumpus(self):
        return self.wumpus
    
    def hasSpider(self):
        return self.spider
    
    def hasPit(self):
        return self.pit
    
    def arrowRoom(self):
        return self.arrow
    
    def setWumpus(self):
        self.wumpus = True
        
    def setSpider(self):
        self.spider = True
        
    def setPit(self):
        self.pit = True
        
    def setArrow(self):
        self.arrow = True
    
    def isAdj(self, roomnum):
        return roomnum in self.adj
    
    def getDesc(self):
        return self.desc
    
    def roomNum(self):
        return self.roomnum
