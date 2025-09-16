class Arrays:

    
    def __init__(self,value: list):

        self.value:list[str]= value
        


    def add_in_list(self, add_item):
        new = [add_item]
        self.value = self.value + new
        return self.value


    def replace_to_index(self, index, value):

        
        for item in range(len(self.value)):
            if item == index:
                self.value[item]= value
        return self.value
    
        
    def remove_last(self):
        if len(self.value) == 0:
            return []
        else:
            new_list=[]
            for item in range(len(self.value)-1):
                new_list+=[self.value[item]]
            self.value = new_list
            
            return self.value
    

    def remove_value(self, char):
        new_list = []
        for item in self.value:
            if item != char:
                new_list += [item]
            self.value = new_list
        return self.value
    

    def poper(self, option = -1):
        
    
        if isinstance(option, int):
            if option > len(self.value):
               return "Index Error Out of Range"
            else:
                now_value=self.value[option]
            
                return self.remove_value( now_value)
        
        
        else:
            return "Invalid pop only works with index"
        
    

                    
            
        
        
    


        
        

    
        
    


