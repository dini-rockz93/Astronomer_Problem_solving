class PRODUCTS:
    
    
    
    def __init__(self):
        
        self.__items = {
			'R01' : 32.95,
			'G01' : 24.95,
			'B01' : 7.95,
 		}
        self.basket = {}
        self.sum = 0
    
    @staticmethod
    def ship_costs(costs=0):
                
        if costs > 90:
            charge = 0
        elif costs >= 50 and costs < 90:
            charge = 2.95
        elif costs < 50 and costs >= 0:
            charge = 4.95
        else:
            charge = -1
        return charge 
     
    def add(self, item):
        
        if item not in self.__items:
            return -1
    
        if item in self.basket:
            self.basket[item] += 1
        else:
            self.basket[item] = 1
        
        return 0
    
    def total(self):
        
        if not self.basket:
            return self.sum
        self.offers()
        print(self.basket)
        
        for key in self.basket:
            self.sum += self.basket[key] * self.__items[key]    
     
        self.sum += self.ship_costs(self.sum)
        self.sum = round(self.sum, 2)
        return self.sum
    
    def offers(self):
        red_item = self.basket.get('R01')
        
        if not red_item:
            return 
        
        if red_item > 1 and red_item % 2 == 0:
            self.basket['R01'] = red_item // 2 + 0.5
        elif red_item > 1 and red_item % 2 == 1:
            self.basket['R01'] = red_item // 2 + 0.5 + 1
     