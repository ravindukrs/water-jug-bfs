class operations:
    # A : Jug with maximum capacity of 4L
    # B : Jug with maximum capacity of 3L

    def __init__(self, A, B):
        # Define maximum capacities of Jars
        # A = 4, B = 3
        self.A = A
        self.B = B

    # Filling A completely
    def fillA(self, x, y):
        x = self.A
        return x,y

    # Filling B completely
    def fillB(self, x, y):
        y = self.B
        return x,y

    # Pour B to A
    def pourFromBtoA(self, x, y):
        # If A can hold entirety of B, empty B and add volume to A
        if x + y <= self.A:
            x = x + y
            y = 0
        else:
            # If A cannot hold entirety of B, fill A and keep excess volume in B
            excess = self.A - x
            y = y - excess
            x = self.A
        return x,y

    # Pour A to B
    def pourFromAtoB(self, x, y):
        # If A can hold entirety of B, empty A and add volume to B
        if x + y <= self.B:
            x = 0
            y = x + y
        else:
            # If B cannot hold entirety of A, fill B and keep excess volume in A
            temp = self.B - y
            x = x - temp
            y = self.B
        return x,y

    def emptyA(self, x, y):
        x=0
        return x,y

    def emptyB(self, x, y):
        y=0
        return x,y
