class RoomInfo(object):
    wumpus = False
    spider = False
    pit = False
    
    def hasWumpus(self):
        global wumpus
        return wumpus
    def hasSpider(self):
        global spider
        return spider
    def hasPit(self):
        global pit
        return pit
    def setWumpus(self):
        wumpus = True
    def setSpider(self):
        spider = True
    def setPit(self):
        pit = True