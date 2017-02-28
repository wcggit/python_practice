

class Order:

    def __init__(self, id, sid, userId, totalPrice, createDate, completeDate, version):
        self.id = id
        self.sid = sid;
        self.userId = userId
        self.totalPrice = totalPrice
        self.createDate = createDate
        self.completeDate = completeDate
        self.version = version
